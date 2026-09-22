from pylint.lint import Run
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter

test_file = "test.py"

pylint_output = StringIO()
reporter = TextReporter(pylint_output)

# exit=False keeps the python process alive after the linter finishes
Run([test_file], reporter=reporter, exit=False)

# Retrieve the text report
report_content = pylint_output.getvalue()
print(report_content)
