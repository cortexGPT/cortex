import os

def test_directory_structure():
    """
    Verify that all required directories are present in the project.
    """
    required_dirs = ["src", "tests", "docs", "scripts"]
    for directory in required_dirs:
        assert os.path.isdir(directory), f"Missing directory: {directory}"
