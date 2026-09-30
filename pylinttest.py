import subprocess
import sys


def run_pylint(filename):
    result = subprocess.run(
        [sys.executable, "-m", "pylint", filename],
        capture_output=True,
        text=True
    )

    return result.stdout


if __name__ == "__main__":
    print("Running Pylint...")

    output = run_pylint("student_code.py")

    if output.strip():
        print(output)
    else:
        print("Pylint returned no output.")