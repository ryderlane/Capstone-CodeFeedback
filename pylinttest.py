from pylint.lint import Run
from ollama import chat

test_file = "test.py"

prompt_content = f"review this code and fix any errors:\n\n```python\n{test_file}\n```"

response = chat(
    model='codellama',
    messages=[{'role': 'user', 'content': prompt_content}],
)
print(response.message.content)

Run([test_file])