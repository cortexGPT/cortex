# Technical Documentation - v0.0.0.1

## Overview
This document provides detailed technical information regarding the architectural structure, modules, and dependencies of Cortex version 0.0.0.1. This version focuses on setting up the foundation, including the local development environment, project structure, virtual environment, Git version control, and basic testing capabilities.

## Architecture Overview
Cortex is designed with a modular architecture to ensure easy maintainability, scalability, and extensibility. The following sections outline the architectural components introduced in this version.

### 1. Development Environment
- **Python Version**: Cortex is developed using Python 3.9 or newer. This specific version ensures compatibility with key libraries and maintains support for modern language features.
- **Local Environment Setup**: The project uses a virtual environment (`venv`) to manage dependencies and ensure isolation from other projects or system-level packages. This makes it easy to maintain consistent development across different machines.

### 2. Project Directory Structure
The following modular directory structure has been set up to facilitate organized development and separation of concerns:

```
cortex/
├── .venv/                     # Contains virtual environment dependencies
├── docs/                      # Contains project documentation
├── scripts/                   # Stores utility or setup scripts
│   └── setup.sh               # Python venv setup script
├── src/                       # Contains the main Python modules for Cortex
├── tests/                     # Stores unit and integration tests
├── .gitignore                 # Defines files for Git to ignore
├── .pylintrc                  # Configures Pylint rules
├── LICENSE                    # Terms for project usage
├── pyproject.toml             # Centralized configuration for Python tools
├── README.md                  # Project overview and setup guide
└── requirements.txt           # List of project dependencies
```

### 3. Version Control System (Git)
- **Branching Strategy**: A structured branching model has been implemented for efficient development and collaboration.
  - `main`: Stable branch containing production-ready code.
  - `dev`: Ongoing development and integration branch.
  - `feature/<feature-name>`: Separate branches for specific features or bug fixes.
- **Commit Guidelines**: Commit messages follow the format `[Feature/Hotfix] Short description` for better traceability.

### 4. Module-Level Descriptions

#### a. `src/`
The `src/` directory contains all the main modules of the Cortex project.
- **Current State**: No specific modules have been developed in version 0.0.0.1. Future versions will introduce application logic, including natural language processing, interaction handling, and backend services.

#### b. `scripts/`
The `scripts/` directory includes utility scripts to simplify routine tasks.
- **`setup.sh`**: Automates the creation and activation of the virtual environment. It installs dependencies defined in `requirements.txt`.
  - **Usage**: Run the script after cloning the repository to ensure the development environment is correctly configured.

#### c. `tests/`
The `tests/` directory houses unit and integration tests.
- **Current Tests**: A sample test file (`test_sample.py`) has been provided to verify the basic environment setup. Future versions will have unit tests that verify individual modules and integrated functionality.

### 5. Code Quality and Standards
- **Linter**: `pylint` has been configured to enforce PEP 8 standards and ensure that the codebase is consistent and maintainable.
- **Formatter**: `black` is used to automatically format the code and ensure that all contributors adhere to a unified style.
- **Configuration Files**: The following files have been added to support code quality tools:
  - **`.pylintrc`**: Configures rules for `pylint`.
  - **`pyproject.toml`**: Configures settings for `black` and other Python tools.

### 6. Flow Diagrams

#### a. Environment Setup Flow
```plaintext
+-------------------------+
| Clone the Repository    |
+-----------+-------------+
            |
            v
+-----------+-------------+
| Create Virtual Env      |
| (python -m venv venv)   |
+-----------+-------------+
            |
            v
+-----------+-------------+
| Activate Virtual Env    |
| (source venv/bin/activate) |
+-----------+-------------+
            |
            v
+-----------+-------------+
| Install Dependencies    |
| (pip install -r requirements.txt) |
+-------------------------+
```
This flow diagram shows the step-by-step process of setting up the development environment, ensuring that every developer starts from a consistent base.

### 7. Third-Party Dependencies
- **Flask**: Flask will be used for backend development starting from version 0.0.0.2.
- **pytest**: Installed to support the writing and execution of unit tests.
- **pylint**: Configured as a linter to maintain code quality.
- **black**: Configured as the code formatter for consistency.

Dependencies are managed via the `requirements.txt` file to ensure that all developers and CI/CD systems use the same package versions. The following command installs these dependencies:
```sh
pip install -r requirements.txt
```

### 8. Known Issues and Limitations
- **Python Version Compatibility**: Python 3.9 or newer is required, and compatibility issues may arise if an older version is used.
- **Environment Setup on Different Operating Systems**: Setting up the virtual environment (`venv`) may behave differently on Windows, macOS, and Linux. The `setup.sh` script is intended to help automate this step, but manual intervention might be required in some cases.
- **Linting and Formatting Conflicts**: Conflicts between `pylint` and `black` can occur, especially where strict linting rules conflict with automatic formatting. This is addressed by fine-tuning `.pylintrc` and formatting settings in `pyproject.toml`.

### 9. Future Architectural Updates
- **Backend Application Development**: In the next version (v0.0.0.2), the basic backend using Flask will be developed. This will include defining API routes, managing sessions, and interacting with a front-end.
- **API Specifications**: The initial API endpoints (`/health` and `/echo`) will be defined to verify server readiness and basic request-response mechanisms.
- **Modularization**: Code will be broken down into more modules for different functionalities such as NLU processing, session management, and role-playing capabilities as outlined in the Cortex Roadmap.

### 10. Changes to Third-Party Libraries
- **New Libraries Added**:
  - **pytest**: For initial testing setup.
  - **pylint and black**: For code quality and formatting.
- **Future Dependencies**: The introduction of Flask in the next version will extend the capability to develop the Cortex backend.

### 11. Conclusion
The technical foundation laid in version 0.0.0.1 ensures that Cortex can be developed efficiently with consistency across contributions. The architectural design, modular structure, version control, and integrated quality tools all work together to make Cortex maintainable, scalable, and easy to extend as new features are introduced in future versions.
