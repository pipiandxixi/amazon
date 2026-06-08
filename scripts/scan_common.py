import json
import re
import subprocess
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
