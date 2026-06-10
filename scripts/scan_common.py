import json
import re
import subprocess
import sys
import time
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"


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


def eval_browser(js, timeout=45):
    return run_opencli_cmd(["opencli", "browser", "ss", "eval", js], timeout=timeout)


def open_browser(url):
    return run_opencli_cmd(["opencli", "browser", "ss", "open", url])


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
