import subprocess




OLLAMA_PATH = r"C:\Users\Ryder\AppData\Local\Programs\Ollama\ollama.exe"




def run_codellama(code, prompt):
    full_prompt = f"""
{prompt}


STUDENT CODE:


{code}
"""


    result = subprocess.run(
        [OLLAMA_PATH, "run", "codellama"],
        input=full_prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )


    if result.returncode != 0:
        return f"ERROR:\n{result.stderr}"


    return result.stdout




if __name__ == "__main__":


    with open("studentcode.py", "r", encoding="utf-8") as file:
        studentcode = file.read()


    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read()


    feedback = run_codellama(studentcode, prompt)


    print(feedback)
