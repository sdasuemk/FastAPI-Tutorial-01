# FastAPI Comprehensive Tutorial

Welcome to this comprehensive **FastAPI** tutorial! This project demonstrates how to build a robust API using FastAPI, covering everything from basic parameter handling to full database integration with SQLite.

## 🚀 Features

- **FastAPI Framework**: Modern, fast (high-performance), web framework for building APIs.
- **SQLite Database**: Persistent storage using `aiosqlite` (async driver) and `databases`.
- **SQLAlchemy Core**: Efficient schema definition and query building.
- **RESTful CRUD**: Full implementation of Create, Read, Update, and Delete operations.
- **core Concepts Covered**:
    - Path Parameters
    - Query Parameters
    - Request Body & Validation (Pydantic)
    - Headers & Cookies
- **Interactive Documentation**: Automatic Swagger UI and ReDoc.

## 🛠️ Prerequisites

- **Python 3.8+** installed on your system.
- Basic understanding of Python and REST APIs.

## 📦 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/sdasuemk/FastAPI-Tutorial-01.git
    cd FastAPI-Tutorial-01
    ```

2.  **Create a Virtual Environment:**
    Recommend using a virtual environment to keep dependencies isolated.
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install all required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    *Alternatively, install manually:*
    ```bash
    pip install fastapi[all] uvicorn[standard] databases[sqlite] sqlalchemy aiosqlite
    ```

## 🏃‍♂️ Running the Applications

This project contains two main application files demonstrating different concepts:

### 1. Basic Concepts (`main.py`)
Run this to learn about Path parameters, Query parameters, and basic request handling.
```bash
uvicorn main:app --reload
```
- **Access Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Database Integration (`inventory-application.py`)
Run this to see a full CRUD application with SQLite database.
```bash
uvicorn inventory-application:app --port 8000 --reload
```
(*Make sure to stop the other server first or use a different port*)

---

## 📚 Part 1: Basic Concepts (`main.py`)

This section demonstrates fundamental FastAPI features.

### Usage Examples

#### 1. Root Endpoint
- **URL**: `http://127.0.0.1:8000/`
- **Method**: `GET`
- **Response**: `{"data": "Hello world!"}`

#### 2. Path Parameter
- **URL**: `http://127.0.0.1:8000/path-parameter-example/John/30`
- **Method**: `GET`
- **Response**: `{"data": "Name is : John, age is: 30"}`

#### 3. Query Parameter
- **URL**: `http://127.0.0.1:8000/query-parameter-example?data_type=users&skip=0&limit=5`
- **Method**: `GET`
- **Response**: `{"data_type": "users", "skip": 0, "limit": 5}`

#### 4. Create Item (Body)
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

---

## 📚 Part 2: Database Integration (`inventory-application.py`)

This section demonstrates how to integrate a **SQLite** database (`db.db`) for persistent storage.

### Code Walkthrough

#### Database Configuration
We use `databases` for async connections and `SQLAlchemy` for defining the table structure.

```python
DATABASE_URL = "sqlite:///./db.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Define the 'items' table
items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
)
```

#### Lifespan Management
FastAPI's `lifespan` context manager handles opening and closing the database connection automatically when the application starts and stops.

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()
```

### API Endpoints (CRUD +)

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/items` | **Create**: Add a new item to the inventory. |
| `GET` | `/items` | **Read**: Retrieve a list of all items. |
| `GET` | `/items/{id}` | **Read**: Retrieve details of a specific item by ID. |
| `PUT` | `/items/{id}` | **Update (Full)**: Completely replace an existing item. Requires all fields. |
| `PATCH` | `/items/{id}` | **Update (Partial)**: Update only specific fields (e.g., just price). |
| `DELETE` | `/items/{id}` | **Delete**: Remove an item from the inventory. |
| `HEAD` | `/items/{id}` | **Headers Only**: Same as GET, but returns only headers (no body). Useful for checking existence or last-modified. |
| `OPTIONS` | `/items/{id}` | **Capabilities**: Returns allowed methods and other options for the resource. |

### HTTP Methods Theory

- **GET**: Retrieve data. Safe and idempotent.
- **POST**: Submit data to be processed. Not idempotent.
- **PUT**: Update/Replace a resource. Idempotent.
- **PATCH**: Partially update a resource. Not necessarily idempotent (but usually is).
- **DELETE**: Remove a resource. Idempotent.
- **HEAD**: Identical to GET but without the response body.
- **OPTIONS**: Describes the communication options for the target resource.
- **CONNECT**: Establishes a tunnel to the server identified by the target resource (rarely used in REST APIs).
- **TRACE**: Performs a message loop-back test along the path to the target resource (often disabled for security).

---

## 🧪 Verification & Testing

You can verify the database application works correctly using the provided scripts:

1.  **Verify API Logic**:
    Runs a test script that performs all CRUD operations against the running API.
    ```bash
    python verify_db.py
    ```

2.  **Inspect Database**:
    Reads the raw SQLite file to show current data using standard libraries.
    ```bash
    python inspect_db.py
    ```

## 📄 License
This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.html).
