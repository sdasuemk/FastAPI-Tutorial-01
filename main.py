# FastAPI Tutorial - Main Application
# This file serves as the entry point for our FastAPI application.
# It demonstrates various features of FastAPI, including:
# 1. Path Parameters
# 2. Query Parameters
# 3. Request Bodies (Pydantic Models)
# 4. Headers and Cookies
# 5. API Documentation Metadata

# Importing necessary modules
# FastAPI: The main class to create our API.
# Header, Cookie, Path, Query, Body: Helper functions to declare metadata and validation for parameters.
from fastapi import FastAPI, Header, Cookie, Path, Query, Body

# BaseModel, Field: Used to define data shapes (schemas) for request bodies and validation.
from pydantic import BaseModel, Field

# Optional: Used for type hinting optional parameters.
from typing import Optional

# Configuration for API Tags
# Tags help organize endpoints in the Swagger documentation.
tags_metadata = [
    {
        "name": "General",
        "description": "General purpose endpoints.",
    },
    {
        "name": "payload",
        "description": "How backend can get query data from frontend (Path, Query, Body, Headers, Cookies).",
    },
]

# Initialize the FastAPI App
# We provide metadata here that will appear in the Swagger UI (/docs).
app = FastAPI(
    title="FastAPI Demo Application",
    description="This is a sample FastAPI application serving as a tutorial. It demonstrates various ways to pass data to the backend.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Support Team",
        "url": "http://example.com/contact/",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


# --- GENERAL ENDPOINTS ---

@app.get("/", tags=["General"], summary="Root Endpoint", description="Returns a simple greeting message.")
def home():
    """
    **Root Endpoint**
    
    This is the simplest GET endpoint. It returns a JSON response.
    """
    return {"data": "Hello world!"}

@app.post("/homepage", tags=["General"], summary="Homepage Handler", description="A simple POST handler for the homepage.")
def handler():
    """
    **Homepage Handler**
    
    A simple POST endpoint to demonstrate handling POST requests without a body.
    """
    return {"data": "Handler"}

# --- PAYLOAD EXAMPLES (How to send data to Backend) ---

# 1. Path Parameters
# These are parts of the URL path itself. Used to identify a specific resource.
# Example: /path-parameter-example/John/30
@app.get("/path-parameter-example/{name}/{age}", tags=["payload"], summary="Path parameter example", description="Retrieve user information based on name and age path parameters.")
async def get_name(
    # Path(...) is used to add metadata and validation to path parameters.
    name: str = Path(..., title="The Name of the User", description="The name of the user to retrieve", min_length=1),
    age: str = Path(..., title="The Age of the User", description="The age of the user to retrieve")
):
    """
    **Path Parameter Example**
    
    Accesses data embedded directly in the URL path.
    - `name`: String
    - `age`: String
    """
    return {"data": f"Name is : {name}, age is: {age}"}

# 2. Query Parameters
# These appear after the '?' in the URL. Used for filtering, sorting, or pagination.
# Example: /query-parameter-example?data_type=files&skip=0&limit=10
@app.get("/query-parameter-example", tags=["payload"], summary="Query Parameter Example", description="Demonstrates specific query parameters.")
async def get_api_data(
    # Query(...) allows defining default values and validation constraints.
    data_type: str = Query(..., title="Data Type", description="The type of data to retrieve"),
    skip: int = Query(0, title="Skip", description="Number of items to skip (Pagination)", ge=0),
    limit: int = Query(10, title="Limit", description="Max number of items to return (Pagination)", le=100)
):
    """
    **Query Parameter Example**
    
    Simulates retrieving data with pagination and filtering.
    """
    return {
        "data_type": data_type,
        "skip": skip,
        "limit": limit
    }

# 3. Request Body
# Used to send JSON data to the API, typically with POST/PUT/PATCH methods.
# We define a Pydantic model (Item) to validate the structure of the data.
class Item(BaseModel):
    name: str = Field(..., title="Item Name", description="The name of the item", example="Foo")
    price: float = Field(..., title="Item Price", description="The price of the item", gt=0, example=35.5)
    brand: Optional[str] = Field(None, title="Brand", description="The brand of the item", example="BarBrand")

@app.get("/body-parameter-example/item", tags=["payload"], summary="Body Parameter Example", description="Demonstrates receiving an item body.")
async def create_item(
    # Body(..., embed=True) expects the JSON body to be wrapped in a key named 'item'.
    item: Item = Body(..., embed=True)
):
    """
    **Body Parameter Example**
    
    Receives a JSON object in the request body.
    """
    return {"item": item}

# 4. Headers and Cookies
# Headers provide metadata about the request (e.g., User-Agent).
# Cookies are small pieces of data stored by the browser.

@app.get("/item/example-header", tags=["payload"], summary="Header Example", description="Demonstrates reading a header value.")
async def get_item(
    # Header(...) extracts the value from the HTTP headers.
    user_agent: Optional[str] = Header(None, title="User Agent", description="The User-Agent header value")
):
    """
    **Header Example**
    
    Returns the value of the 'User-Agent' header sent by the client.
    """
    return {
        "user_agent": user_agent
    }

@app.get("/items/example-cookie", tags=["payload"], summary="Cookie Example", description="Demonstrates reading a cookie value.")
async def read_items(
    # Cookie(...) extracts the value from the cookies.
    session_token: Optional[str] = Cookie(None, title="Session Token", description="The session token cookie")
):
    """
    **Cookie Example**
    
    Returns the value of the 'session_token' cookie if present.
    """
    return {"session_token": session_token}
