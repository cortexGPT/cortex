import subprocess

def test_lint_and_format_integration():
    """
    Ensure that pylint and black can be run without errors.
    """
    lint_result = subprocess.run(["pylint", "src/"], capture_output=True)
    assert lint_result.returncode == 0, f"Pylint failed: {lint_result.stderr.decode()}"

    format_result = subprocess.run(["black", "--check", "src/"], capture_output=True)
    assert format_result.returncode == 0, f"Black formatting issues found: {format_result.stderr.decode()}"