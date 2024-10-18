# Cortex User Manual - v0.0.0.1

## Overview
Cortex is a locally-hosted, offline chatbot designed to provide rich, interactive conversations while prioritizing privacy. This user manual will help you set up and use Cortex, focusing on version 0.0.0.1, which primarily establishes the development environment and initial infrastructure.

## Getting Started
The setup process for Cortex involves cloning the repository, setting up a virtual environment, and installing the necessary dependencies.

### Prerequisites
- **Python 3.9 or Newer**: Make sure you have Python 3.9 or newer installed.
- **Git**: Git is needed for version control.

### Step-by-Step Setup Instructions
1. **Clone the Repository**
   To get started, clone the repository to your local machine.
   ```sh
   git clone <repository-url>
   cd cortex
   ```

2. **Create and Activate a Virtual Environment**
   To isolate dependencies, create a virtual environment and activate it.
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Use the following command to install all required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. **Verify Setup**
   Run the initial tests to verify that everything is set up correctly.
   ```sh
   pytest
   ```
   All tests should pass, indicating a successful setup.

## Available Functionality

### 1. Health Check Endpoint
- **Description**: Confirms that the Cortex server is running properly.
- **How to Use**:
  - Use the following command to check the server health:
    ```sh
    curl -X GET http://localhost:5000/api/v1/health
    ```
  - **Response**: You should receive:
    ```json
    {
      "status": "healthy"
    }
    ```
  - If the server isn't running, ensure you have activated the virtual environment and have run the server using Flask.

### 2. Echo Endpoint
- **Description**: The `/echo` endpoint echoes back the message provided. It helps test that requests are being processed correctly.
- **How to Use**:
  - Send a message using the following command:
    ```sh
    curl -X POST http://localhost:5000/api/v1/echo -H "Content-Type: application/json" -d '{"message": "Hello, Cortex!"}'
    ```
  - **Response**: You should receive:
    ```json
    {
      "echo": "Hello, Cortex!"
    }
    ```
  - This functionality is useful to confirm that data can be successfully sent to and received from the server.

### Running the Server
- **Flask Development Server**: Once the backend routes are created (starting from version 0.0.0.2), you will need to run the server to interact with the endpoints.
  - Start the server using Flask:
    ```sh
    flask run
    ```
  - By default, this will make the API available at `http://localhost:5000`.

## New Workflows
This version focuses mainly on setting up the infrastructure, but the basic workflow for interacting with Cortex involves:
1. **Activating the virtual environment**.
2. **Starting the Flask server**.
3. **Using available API endpoints** to interact with the backend.

### Example Workflow
1. **Activate Virtual Environment**:
   ```sh
   source venv/bin/activate
   ```
2. **Run Flask Server**:
   ```sh
   flask run
   ```
3. **Check Server Health**:
   ```sh
   curl -X GET http://localhost:5000/api/v1/health
   ```

## Troubleshooting Tips
- **Virtual Environment Issues**: If you encounter errors while creating or activating the virtual environment, ensure Python is correctly installed and accessible via your system's PATH. On Windows, make sure to use the correct path (`venv\Scripts\activate`).
- **Dependency Conflicts**: If you experience dependency issues while running `pip install -r requirements.txt`, try running:
  ```sh
  pip check
  ```
  This command will display any conflicts between installed packages.
- **Server Not Running**: If you cannot access the `/health` endpoint, make sure that the server is running (`flask run`) and that the correct virtual environment is activated.
- **Linting/Formatting Issues**: `pylint` and `black` are used to ensure code quality. If your code fails checks, use the following commands:
  ```sh
  pylint src/
  black src/
  ```

## FAQs
1. **Q: How do I know if my environment is set up correctly?**
   - **A**: Run `pytest`. If all tests pass, your setup is correct.

2. **Q: I am getting an error when running `flask run`. What should I do?**
   - **A**: Ensure your virtual environment is activated. Also, verify that Flask is installed (`pip show flask`).

3. **Q: How do I add new dependencies?**
   - **A**: Add the required library to `requirements.txt` and run `pip install -r requirements.txt` again.

## Summary
In this version (v0.0.0.1), Cortex establishes its development environment, sets up version control, defines project structure, and provides initial API endpoints. These endpoints serve as simple verifications to ensure the server is running and can process basic requests. Future versions will introduce more functionality, such as a basic HTML interface and advanced chatbot capabilities.

## Future Updates
- **Version 0.0.0.2** will introduce a basic Flask application, including simple routes for further interaction with Cortex.
- **Version 0.0.0.3** will include a minimal HTML user interface to allow users to interact with Cortex through a web browser.
