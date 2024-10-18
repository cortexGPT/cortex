# Cortex

Cortex is a sophisticated, locally-hosted chatbot designed to provide rich and interactive conversations while prioritizing user privacy. The goal of Cortex is to offer advanced natural language understanding, contextual awareness, and multimodal capabilities without requiring an internet connection.

## Project Overview
Cortex aims to serve as a versatile companion, combining empathetic responses, role-playing capabilities, and scenario generation, all while integrating with personal applications like reminders, email, and calendars. This setup guide will help you set up the development environment to begin working on Cortex.

## Features (v0.0.0.1)
- Local Development Environment setup for Cortex using Python 3.9 or newer.
- Version control system via Git for collaboration and change tracking.
- Modular project directory structure for easier maintenance.
- Virtual environment configuration to isolate dependencies.
- Code quality tools (linter and formatter) for consistent code practices.
- Basic documentation for project setup.
- Basic unit testing setup using `pytest`.

## Installation Instructions

### Prerequisites
- Python 3.9 or newer
- Git

### Step-by-Step Setup
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd cortex
   ```

2. **Create and Activate a Virtual Environment**
   Create the virtual environment to keep dependencies isolated.
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install all the necessary libraries listed in `requirements.txt`.
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Git**
   - Make sure to use the appropriate branch structure (`main`, `dev`, `feature/<feature-name>`).
   - Set up your Git credentials and connect to the remote repository.

5. **Run Initial Tests**
   To verify that everything is set up correctly, run the sample tests:
   ```sh
   pytest
   ```
   Ensure all tests pass before proceeding.

### Directory Structure
The project is organized in a modular and maintainable structure:

```
cortex/
├── .venv/                     # Contains virtual environment dependencies
├── docs/                      # Project documentation
├── scripts/                   # Utility or setup scripts
│   └── setup.sh               # Python venv setup script
├── src/                       # Main Python modules for Cortex
├── tests/                     # Unit and integration tests
├── .gitignore                 # Git ignore file
├── .pylintrc                  # Pylint configuration file
├── LICENSE                    # Project license
├── pyproject.toml             # Configuration for Python tools
├── README.md                  # Project overview and setup guide
└── requirements.txt           # List of project dependencies
```

## Usage Notes
- **Running the Virtual Environment**: After activating the virtual environment, all commands must be run in this context to ensure dependencies are correctly used.
- **Code Quality Checks**: Use `pylint` for linting and `black` for code formatting before committing changes. Both tools help ensure consistent code quality across contributors.
  ```sh
  pylint src/   # Linting the source code
  black src/    # Formatting the source code
  ```
- **Running Tests**: All new features should have corresponding unit tests. Use `pytest` for running tests:
  ```sh
  pytest tests/
  ```

## Contribution Guidelines
1. **Branching**: Follow the branch naming conventions (`feature/<feature-name>`, `hotfix/<hotfix-name>`).
2. **Commit Messages**: Use the following format for commit messages: `[Feature/Hotfix] Short description`.
3. **Code Quality**: Ensure code passes all linter checks (`pylint`) and is formatted using `black` before pushing.
4. **Testing**: Every new feature or bug fix should include appropriate unit tests.

## Example Use Case
- To get started, run a simple command to check everything is set up correctly:
  ```sh
  python -m src.example_module  # Replace with a real module as development proceeds
  ```
- All initial tests should pass, indicating a correct setup.

## Dependencies
Dependencies are listed in `requirements.txt`. Run the following command to install them:
```sh
pip install -r requirements.txt
```

Libraries used:
- **Flask**: For backend development (future versions).
- **pytest**: For unit testing framework.
- **pylint and black**: For ensuring code quality and style.

## Troubleshooting
- **Virtual Environment Issues**: If there are problems creating the virtual environment, ensure Python 3.9 or newer is installed and properly configured in your PATH.
- **Dependency Conflicts**: If conflicts occur, try running:
  ```sh
  pip check
  ```
  This command will show any dependency conflicts and provide suggestions.

## Future Plans
- **v0.0.0.2**: Set up a basic Flask application to provide a backend for interacting with Cortex.
- **v0.0.0.3**: Develop a minimal HTML interface for user interaction.

## License
This project is licensed under the terms of the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, feel free to reach out by creating an issue in the repository.

