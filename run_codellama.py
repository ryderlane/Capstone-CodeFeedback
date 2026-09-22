import json
import urllib.request
from pylint.lint import Run
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter

MODEL_NAME = "codellama:7b-instruct"
OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT_FILE = "prompt.txt"
STUDENT_CODE_FILE = "test.py"


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def send_to_ollama(full_prompt):
    data = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    encoded_data = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=encoded_data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]


# deal with linter
pylint_output = StringIO()
reporter = TextReporter(pylint_output)

# exit=False keeps the python process alive after the linter finishes
Run([STUDENT_CODE_FILE], reporter=reporter, exit=False)

linter_output = pylint_output.getvalue()
print(linter_output)

def main():
    prompt_instructions = read_file(PROMPT_FILE)
    student_code = read_file(STUDENT_CODE_FILE)
    student_code += linter_output

    full_prompt = (
        prompt_instructions
        + "\n\n"
        + "Evaluate the following Python code:\n\n"
        + student_code
    )



    print("Sending code to CodeLlama...")
    print()

    feedback = send_to_ollama(full_prompt)

    print("CODELLAMA FEEDBACK")
    print("------------------")
    print(feedback)


if __name__ == "__main__":
    main()