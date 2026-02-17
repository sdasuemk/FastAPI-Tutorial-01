# FastAPI Tutorial Project

Welcome to this FastAPI tutorial! This project demonstrates how to build a robust API using FastAPI, covering essential concepts like Path Parameters, Query Parameters, Request Bodies, Headers, and Cookies.

## Features

- **Path Parameters**: Retrieve dynamic values from the URL.
- **Query Parameters**: Filter and paginate data using URL query strings.
- **Request Body**: Send and validate JSON data using Pydantic models.
- **Headers**: Read custom headers from requests.
- **Cookies**: Access cookies sent by the client.
- **Swagger UI**: Interactive API documentation (auto-generated).

## Prerequisites

- Python 3.7+ used.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment**:
    - Windows: `.\.venv\Scripts\Activate`
    - Mac/Linux: `source .venv/bin/activate`

4.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn[standard]
    ```

## Running the Application

Start the development server with:

```bash
uvicorn main:app --reload
```

- `main`: The name of the python file (`main.py`).
- `app`: The FastAPI instance inside `main.py`.
- `--reload`: Automatically restarts the server properly when code changes.

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Usage Examples

### 1. Root Endpoint
- **URL**: `http://127.0.0.1:8000/`
- **Method**: `GET`
- **Response**: `{"data": "Hello world!"}`

### 2. Path Parameter
- **URL**: `http://127.0.0.1:8000/path-parameter-example/John/30`
- **Method**: `GET`
- **Response**: `{"data": "Name is : John, age is: 30"}`

### 3. Query Parameter
- **URL**: `http://127.0.0.1:8000/query-parameter-example?data_type=users&skip=0&limit=5`
- **Method**: `GET`
- **Response**: `{"data_type": "users", "skip": 0, "limit": 5}`

### 4. Create Item (Body)
- **URL**: `http://127.0.0.1:8000/body-parameter-example/item`
- **Method**: `POST` (Use Swagger UI to test)
- **Body**:
  ```json
  {
    "item": {
      "name": "Laptop",
      "price": 999.99,
      "brand": "TechBrand"
    }
  }
  ```

### 5. Headers & Cookies
Test these easily using the "Try it out" feature in the Swagger UI.

## License

This project is licensed under the Apache 2.0 License.
