# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to design and implement a small RESTful API using the FastAPI framework. This assignment covers defining routes, request/response models with Pydantic, basic in-memory persistence, and running the app with Uvicorn.

## 📝 Tasks

### 🛠️	Build a Small REST API

#### Description
Create a simple API for managing items (create, read, update, delete). Use FastAPI and Pydantic models for request validation and response serialization. Store data in an in-memory structure (dictionary) for simplicity.

#### Requirements
Completed program should:

- Use FastAPI to define endpoints for CRUD operations
- Define request and response schemas with Pydantic
- Support at least the following endpoints:
  - GET /items/{item_id} — return item details
  - GET /items — list items (optional: pagination/filtering)
  - POST /items — create a new item
  - PUT /items/{item_id} — update an existing item
  - DELETE /items/{item_id} — remove an item
- Validate input and return appropriate HTTP status codes
- Use an in-memory store (e.g., dict) so the app can run without a database
- Provide clear README instructions to run the app locally using Uvicorn

##### Example usage
```
# Create an item
POST /items  -> 201 Created
{
  "id": 1,
  "name": "Sample",
  "description": "A sample item"
}

# Get item
GET /items/1 -> 200 OK
```

### 🛠️	Optional Enhancements

#### Description
Extend the API with extra features to demonstrate deeper understanding.

#### Requirements
Completed enhancements may include one or more of the following:

- Add query parameters for filtering or pagination on `GET /items`
- Persist data to a lightweight file (JSON) between runs
- Add basic authentication (API key) for create/update/delete operations
- Add automated tests using `pytest` and `httpx` or `requests`

---

## How to run (local)

1. Create a virtual environment and install dependencies:

```
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

2. Run the starter app (provided as `starter-code.py`):

```
uvicorn starter-code:app --reload
```

3. Open the interactive API docs at `http://127.0.0.1:8000/docs`.

## Starter code
See `starter-code.py` in this folder — it contains a minimal FastAPI application you can build upon.

Good luck — focus first on correctness and clear API contracts, then add enhancements for extra credit.
