
import json
import urllib.request
import urllib.error
from pathlib import Path

MODEL = "codellama:7b-instruct"
OLLAMA_URL = "http://localhost:11434/api/generate"

BASE_DIR = Path(__file__).resolve().parent


def number_source_lines(code):
    return "\n".join(
        f"{i}: {line}"
        for i, line in enumerate(code.splitlines(), start=1)
    )


def run_codellama(code, prompt):
    numbered_code = number_source_lines(code)

    full_prompt = f"""
{prompt}

BEGIN STUDENT CODE
{numbered_code}
END STUDENT CODE

IMPORTANT:
Analyze only the student code above.
Do not repeat the prompt instructions.
Do not evaluate program correctness.
Do not provide replacement code or identifiers.
Report at most five evidence-based style issues.
Use accurate line numbers.

Return only the required ISSUES and SUGGESTIONS sections.
"""

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_predict": 500
        }
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(
            request, timeout=300
        ) as response:
            result = json.load(response)

    except urllib.error.URLError as error:
        return f"ERROR: Cannot connect to Ollama: {error}"

    return result["response"].strip()


if __name__ == "__main__":
    code = (BASE_DIR / "studentcode.py").read_text(
        encoding="utf-8"
    )

    prompt = (BASE_DIR / "prompt.txt").read_text(
        encoding="utf-8"
    )

    feedback = run_codellama(code, prompt)

    print("\n========== CODELLAMA FEEDBACK ==========\n")
    print(feedback)
    print("\n========================================\n")
