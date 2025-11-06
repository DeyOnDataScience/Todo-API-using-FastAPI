# Todo List API
## Project Description
The Todo List API is a simple RESTful API designed to manage a list of todo items. It allows users to create, read, update, and delete (CRUD) todo items.

## Installation Steps
To install and run the Todo List API, follow these steps:

1. **Clone the repository**: Clone the Todo List API repository using Git.
2. **Install dependencies**: Install the required dependencies using pip: `pip install -r requriements.txt`
4. **Run the API**: Run the API using `uvicorn main:app --host 0.0.0.0 --port 8000 or uvicorn main:app --reload`

## Usage Examples
The Todo List API provides the following endpoints:

* **Create Todo**: `POST /todos/` - Create a new todo item
	+ Request Body: `{"title": "Todo Title", "description": "Todo Description"}`
	+ Response: `{"id": 1, "title": "Todo Title", "description": "Todo Description"}`
* **Get Todos**: `GET /todos/` - Get a list of all todo items
	+ Response: `[{"id": 1, "title": "Todo Title", "description": "Todo Description"}]`
* **Update Todo**: `PUT /todos/{todo_id}` - Update a todo item
	+ Request Body: `{"title": "New Todo Title", "description": "New Todo Description"}`
	+ Response: `{"id": 1, "title": "New Todo Title", "description": "New Todo Description"}`
* **Delete Todo**: `DELETE /todos/{todo_id}` - Delete a todo item
	+ Response: `Todo with ID {todo_id} deleted successfully`

## Features
The Todo List API provides the following features:

* **CRUD operations**: Create, read, update, and delete todo items
* **Validation**: Validation of request bodies using Pydantic
* **Database**: SQLite database using SQLAlchemy

## Folder Structure
The Todo List API has the following folder structure:
```markdown
todo_list_api/
|---- database.py
|---- main.py
|---- model.py
|---- validation.py
|---- todo.db
|---- README.md
```
