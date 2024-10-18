# API Specifications - v0.0.0.1

## Overview
This document outlines the API specifications for Cortex version 0.0.0.1. In this version, the initial API endpoints are being set up to facilitate the communication between the front-end and back-end of Cortex. The endpoints provide basic functionality to ensure server readiness, basic routing, and appropriate request/response handling.

## Base URL
The base URL for all API endpoints is:
```
http://localhost:5000/api/v1
```

## Endpoints

### 1. Health Check Endpoint
- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: This endpoint is used to check if the server is up and running.
- **Request**: None.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "status": "healthy"
    }
    ```
- **Error Handling**:
  - **500 Internal Server Error**: Indicates that there was an issue with the server during the health check.

### 2. Example Echo Endpoint
- **Endpoint**: `/echo`
- **Method**: `POST`
- **Description**: Echoes back the input provided in the request body. This is primarily used to verify that POST requests are being received and processed correctly.
- **Request**:
  - **Headers**:
    - `Content-Type: application/json`
  - **Body**:
    ```json
    {
      "message": "Your message here"
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "echo": "Your message here"
    }
    ```
- **Error Handling**:
  - **400 Bad Request**: Indicates that the request body is missing or improperly formatted.
  - **500 Internal Server Error**: General server-side error.

## Input/Output Formats
- **Input Format**: All POST requests should use `application/json` format.
- **Output Format**: All responses will be provided in `application/json` format.

## Request/Response Structure
- **Request Headers**:
  - All requests that send data to the server must include `Content-Type: application/json`.
- **Response Structure**:
  - Successful responses contain a status code and a JSON body.
  - Error responses include the appropriate HTTP status code and an error message.

## Error Handling Improvements
- **General Error Handling**: All endpoints have built-in error handling to provide meaningful messages in case of failure.
  - **400 Bad Request**: Triggered for improperly formatted or missing request data.
  - **500 Internal Server Error**: Generic error for server-side issues that are logged for further investigation.

## Examples

### Example 1: Health Check Request
- **Request**:
  ```sh
  curl -X GET http://localhost:5000/api/v1/health
  ```
- **Response**:
  ```json
  {
    "status": "healthy"
  }
  ```

### Example 2: Echo Request
- **Request**:
  ```sh
  curl -X POST http://localhost:5000/api/v1/echo -H "Content-Type: application/json" -d '{"message": "Hello, Cortex!"}'
  ```
- **Response**:
  ```json
  {
    "echo": "Hello, Cortex!"
  }
  ```

## Future Improvements
- **Additional Endpoints**: The next version will introduce more endpoints to handle user interactions, manage sessions, and add more sophisticated processing capabilities.
- **Validation**: Add more robust input validation for incoming requests to ensure the data is accurate and meets expected formats.
- **Authentication**: Introduce token-based authentication to secure endpoints.

## Summary
Version 0.0.0.1 introduces two simple endpoints to verify that the server is operational and can process basic requests. These foundational endpoints serve as a base for future functionality, including more advanced routing and integration with a front-end interface.
