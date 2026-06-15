import json
import re
import subprocess
import sys
import time
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"


def dated_results_dir(date_str: str = "") -> Path:
    """Return and create the results directory. date_str is kept for API compat but ignored."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return RESULTS_DIR


class OpenCliError(RuntimeError):
    pass


def run_opencli_cmd(args, timeout=45):
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise OpenCliError(f"Command timed out after {timeout}s: {' '.join(args[:4])}") from exc
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "unknown error"
        raise OpenCliError(f"Command failed ({result.returncode}): {message}")
    return result.stdout.strip()


def clear_popups(timeout=10) -> int:
    """统一清除页面弹窗（如 Element UI 对话框、Modal 遮罩、通知栏等）"""
    js = (
        "(() => {\n"
        "  let count = 0;\n"
        "  // 1. 直接隐藏指引和独立消息小组件\n"
        "  const simpleSelectors = [\n"
        "    '.el-notification',\n"
        "    '.el-message',\n"
        "    '.guide-popup',\n"
        "    '.modal-backdrop'\n"
        "  ];\n"
        "  simpleSelectors.forEach(sel => {\n"
        "    try {\n"
        "      document.querySelectorAll(sel).forEach(el => {\n"
        "        el.style.display = 'none';\n"
        "        count++;\n"
        "      });\n"
        "    } catch (e) {}\n"
        "  });\n"
        "  \n"
        "  // 2. 精准移除阻碍交互的可见广告/温馨提示 Dialog 和遮罩层\n"
        "  const dialogSelectors = [\n"
        "    '.el-dialog__wrapper',\n"
        "    '.el-message-box__wrapper',\n"
        "    '.v-modal',\n"
        "    '.modal'\n"
        "  ];\n"
        "  \n"
        "  dialogSelectors.forEach(sel => {\n"
        "    try {\n"
        "      document.querySelectorAll(sel).forEach(el => {\n"
        "        // ⚠️ 极其关键：如果元素当前不可见，绝对不要处理它，防止误杀隐藏的功能弹窗！\n"
        "        const isVisible = el.offsetParent !== null && el.offsetWidth > 0 && el.offsetHeight > 0;\n"
        "        if (!isVisible) return;\n"
        "        \n"
        "        const tagName = el.tagName.toLowerCase();\n"
        "        const safeTags = ['html', 'body', 'main', 'section', 'header', 'footer', 'app', '#app', 'div#app', 'div#layout'];\n"
        "        if (safeTags.includes(tagName) || el.querySelector('main') || el.querySelector('#app')) return;\n"
        "        \n"
        "        // 如果包含功能性白名单关键字，不可删除/隐藏\n"
        "        const hasCategorySearch = !!el.querySelector('input[placeholder*=\"Node ID\"]') || \n"
        "                                  !!el.querySelector('input[placeholder*=\"类目\"]');\n"
        "        const hasCategoryTitle = el.textContent.includes('选择类目') || \n"
        "                                 el.textContent.includes('选择一个或多个类目');\n"
        "        if (hasCategorySearch || hasCategoryTitle) {\n"
        "          return;\n"
        "        }\n"
        "        \n"
        "        // 对可见的 Dialog，若其包含续费、套餐、温馨提示等广告和阻碍文案，执行彻底删除\n"
        "        const text = el.textContent || '';\n"
        "        const badWords = ['续费', '升级', '套餐', '充值', '特惠', '引导', '广告', '活动', '折扣', '限时', '客服', '顾问', 'VIP', '温馨提示'];\n"
        "        const isAd = badWords.some(word => text.includes(word));\n"
        "        \n"
        "        // 对于遮罩层背景，只有在未打开类目搜索时才允许清理\n"
        "        const isMask = sel === '.v-modal' || sel === '.modal';\n"
        "        \n"
        "        if (isAd || (isMask && !document.querySelector('input[placeholder*=\"Node ID\"]'))) {\n"
        "          el.remove(); // 对可见的阻碍 Dialog 和 Modal 背景执行 remove()\n"
        "          count++;\n"
        "        }\n"
        "      });\n"
        "    } catch (e) {}\n"
        "  });\n"
        "  return count;\n"
        "})()"
    )
    try:
        out = run_opencli_cmd(["opencli", "browser", "ss", "eval", js], timeout=timeout)
        if out:
            match = re.search(r'\d+', out)
            if match:
                val = int(match.group())
                if val > 0:
                    print(f"  [POPUP] Cleared {val} blocking element(s) from page.")
                    return val
    except Exception:
        pass
    return 0



def eval_browser(js, timeout=45):
    try:
        return run_opencli_cmd(["opencli", "browser", "ss", "eval", js], timeout=timeout)
    except OpenCliError as exc:
        print(f"  [EVAL WARNING] Command failed: {exc}. Attempting to clear popups and retry...")
        clear_popups()
        time.sleep(1.5)
        return run_opencli_cmd(["opencli", "browser", "ss", "eval", js], timeout=timeout)


def open_browser(url):
    res = run_opencli_cmd(["opencli", "browser", "ss", "open", url])
    time.sleep(2)
    clear_popups()
    return res


def check_browser_ready() -> None:
    """Verify the SellerSprite browser session is accessible and logged in.

    Exits with a clear Chinese-language error message if:
    - the session is not bound to any tab
    - the bound tab is a chrome-extension:// page (extension popup)
    - eval_browser() fails with an attach error
    - the current sellersprite.com page shows a login form
    """
    # 1. Check that the session is bound and responsive
    result = subprocess.run(
        ["opencli", "browser", "ss", "state"],
        capture_output=True, text=True, timeout=15,
    )
    if result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip()
        print(f"\n❌ 卖家精灵浏览器会话未连接: {err}")
        print("请在 Chrome 中打开卖家精灵网站，然后运行以下命令绑定标签页：")
        print("  opencli browser ss bind")
        sys.exit(1)

    # Parse current URL from state output
    url = ""
    for line in result.stdout.splitlines():
        if line.startswith("url:"):
            url = line.split(":", 1)[1].strip()
            break

    if url.startswith("chrome-extension://"):
        print("\n❌ 当前绑定的是卖家精灵扩展弹窗，无法在此执行自动化")
        print("请切换到卖家精灵网站页面 (https://www.sellersprite.com/)，然后重新绑定：")
        print("  opencli browser ss bind")
        sys.exit(1)

    # 2. Confirm the extension context works (catches "attach failed" errors)
    try:
        eval_browser("typeof window !== 'undefined'", timeout=10)
    except OpenCliError as exc:
        err = str(exc)
        if "attach failed" in err or "chrome-extension" in err:
            print("\n❌ 卖家精灵扩展上下文不可用")
            print("请将 Chrome 切换到卖家精灵标签页，然后重新绑定：")
            print("  opencli browser ss bind")
        else:
            print(f"\n❌ 浏览器扩展错误: {exc}")
            print("请确认卖家精灵已打开并登录后重试。")
        sys.exit(1)

    # 3. If already on sellersprite.com, do a best-effort login check
    if "sellersprite.com" in url:
        try:
            out = eval_browser(
                """(() => {
                  const isLoginPage = !!document.querySelector(
                    '.login-form, form[action*="login"], input[type="password"]'
                  );
                  const hasUser = !!document.querySelector(
                    '.user-info, .el-avatar, [class*="nickname"], [class*="username"]'
                  );
                  return JSON.stringify({ isLoginPage, hasUser });
                })()""",
                timeout=10,
            )
            state = extract_json_object(out)
            if state.get("isLoginPage") and not state.get("hasUser"):
                print("\n❌ 卖家精灵未登录，请先在浏览器中登录账号后重试。")
                sys.exit(1)
        except (OpenCliError, ValueError, json.JSONDecodeError):
            pass  # best-effort; auth errors will surface naturally in the scripts


def extract_json_array(output):
    start_idx = output.find("[")
    end_idx = output.rfind("]")
    if start_idx == -1 or end_idx < start_idx:
        raise ValueError("Browser output did not contain a JSON array")
    return json.loads(output[start_idx:end_idx + 1])


def extract_json_object(output):
    start_idx = output.find("{")
    end_idx = output.rfind("}")
    if start_idx == -1 or end_idx < start_idx:
        raise ValueError("Browser output did not contain a JSON object")
    return json.loads(output[start_idx:end_idx + 1])


def wait_for_query_result(expected_term="", previous_first_keyword="", attempts=12, interval=2):
    expected_json = json.dumps(expected_term.lower())
    previous_json = json.dumps(previous_first_keyword)
    js = f"""
    (() => {{
      const table = document.querySelector('table#table-condition-search');
      const rows = table ? table.querySelectorAll('tbody tr').length : 0;
      const input = document.querySelector('input[name=includeKeywords]');
      const inputValue = input ? input.value.trim().toLowerCase() : '';
      const expected = {expected_json};
      const previousFirstKeyword = {previous_json};
      const firstRow = table ? table.querySelector('tbody tr') : null;
      const firstKeyword = firstRow ? firstRow.innerText : '';
      const loading = !!document.querySelector('.el-loading-mask, .loading, [aria-busy=true]');
      return JSON.stringify({{
        rows, inputValue, expected, loading, firstKeyword,
        ready: rows > 0 && !loading && inputValue === expected && firstKeyword !== previousFirstKeyword
      }});
    }})()
    """
    last_state = {}
    for _ in range(attempts):
        output = eval_browser(js)
        try:
            last_state = extract_json_object(output)
            if last_state.get("ready"):
                return last_state
        except (ValueError, json.JSONDecodeError):
            pass
        time.sleep(interval)
    return last_state
