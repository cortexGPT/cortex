import os
import subprocess
import pytest
import sys

def test_virtual_environment_creation():
    """
    Test if the virtual environment is correctly created by setup.
    """
    if sys.platform == "win32":
        # Windows-specific command to create virtual environment
        result = subprocess.run(["python", "-m", "venv", "venv"], capture_output=True)
    else:
        # Unix-based systems command
        result = subprocess.run(["python3", "-m", "venv", "venv"], capture_output=True)
    venv_exists = os.path.isdir("venv")
    assert venv_exists, "Virtual environment was not created."
    assert result.returncode == 0, f"Virtual environment creation failed: {result.stderr.decode()}"

def test_dependencies_installation():
    """
    Verify if all dependencies are installed as per requirements.txt.
    """
    result = subprocess.run(["pip", "show", "Flask"], capture_output=True)
    assert result.returncode == 0, "Flask is not installed, which means dependency installation failed."

    result = subprocess.run(["pip", "show", "pytest"], capture_output=True)
    assert result.returncode == 0, "pytest is not installed, which means dependency installation failed."

def test_linter_configuration():
    """
    Verify that pylint configuration is correctly set up.
    """
    result = subprocess.run(["pylint", "src/"], capture_output=True)
    assert result.returncode == 0, f"Pylint configuration issues found: {result.stderr.decode()}"
