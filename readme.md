# CodeLlama Python Style Testing

This project uses CodeLlama through Ollama to test AI-generated feedback on Python code style, readability, naming conventions, formatting, and comments.

## 1. Install Ollama

Download and install Ollama from:

https://ollama.com

After installation, open a terminal, Command Prompt, or PowerShell window.

Verify that Ollama is installed:

```bash
ollama --version
```

If Ollama is installed correctly, the command should display the installed version.

## 2. Download CodeLlama

For this project, use the CodeLlama instruction model because it is designed to respond to natural-language instructions.

Run:

```bash
ollama pull codellama:7b-instruct
```

This downloads the 7-billion-parameter CodeLlama instruction model.

The model only needs to be downloaded once.

You can verify that it was downloaded by running:

```bash
ollama list
```

You should see `codellama:7b-instruct` in the list.

## 3. Start CodeLlama

Run:

```bash
ollama run codellama:7b-instruct
```

After the model loads, a prompt should appear where you can enter text.

For a quick test, type:

```text
Hello
```

CodeLlama should respond.

To exit CodeLlama, use:

```text
/bye
```

## 4. Test the Python Code

Start CodeLlama again:

```bash
ollama run codellama:7b-instruct
```

Paste the following instructions into the prompt:

```text
Your role is to help the student improve their code style and comment quality without solving the problem for them.

Strict rules:
- Do NOT rewrite, fix, or show corrected code under any circumstances.
- Do NOT give solutions, even partial ones.
- Be concise. Each point should be one sentence. No elaboration beyond what is necessary.
- Refer to specific line behavior or patterns, not general advice.

Respond in exactly this format with no additional text before or after:

ISSUES
1. [specific issue]
2. [specific issue]
...

SUGGESTIONS
1. [specific, actionable hint -- no solutions]
2. [specific, actionable hint -- no solutions]
...

Evaluate the following areas:
- Naming conventions for the language
- Spacing and formatting
- Comment quality: flag comments that are vague, restate the code, or are missing where needed
- Readability

Evaluate the following Python code:

#ENTER STUDENT CODE HERE
```

Press Enter and allow CodeLlama to generate its review.

## 5. What to Check in the Response

The response should follow this general structure:

```text
ISSUES
1. ...
2. ...
3. ...

SUGGESTIONS
1. ...
2. ...
3. ...
```

The model should identify problems such as:

* Unclear variable names such as `t`, `i`, `qty`, and `msg`.
* Missing spaces around operators.
* Missing spaces after commas.
* Vague comments such as `# loop`.
* Comments that simply restate what the code does.
* General readability problems.

The model should NOT:

* Rewrite the Python program.
* Show corrected code.
* Give replacement lines.
* Solve the program.
* Add new features.
* Provide a complete improved version of the function.

## 6. Running CodeLlama Again

After CodeLlama has already been downloaded, you do not need to run the `pull` command again.

Simply run:

```bash
ollama run codellama:7b-instruct
```

Then paste another prompt and another piece of code.




