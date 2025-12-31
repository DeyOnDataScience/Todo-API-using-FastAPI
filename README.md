# Todo API with FastAPI

A robust and secure RESTful API for managing tasks (Todos), built with [FastAPI](https://fastapi.tiangolo.com/), SQLAlchemy, and SQLite. This application supports user authentication (JWT), allowing users to create, read, update, and delete their own private todo items.

## 🚀 Features

*   **User Authentication**: Secure user registration and login using OAuth2 with Password (and hashing) and Bearer with JWT tokens.
*   **CRUD Operations**: Full Create, Read, Update, and Delete functionality for Todo items.
*   **Data Persistence**: Uses SQLAlchemy ORM for database interactions (SQLite by default).
*   **Validation**: Robust data validation using Pydantic models.
*   **Documentation**: Automatic interactive API documentation via Swagger UI (`/docs`) and ReDoc (`/redoc`).

## 🛠️ Technology Stack

*   **Framework**: FastAPI
*   **Language**: Python 3.10+
*   **Database ORM**: SQLAlchemy
*   **Authentication**: Python-Jose (JWT), Passlib (Bcrypt)
*   **Server**: Uvicorn

## 📂 Project Structure

*   `main.py`: Entry point of the application. Contains API enpoints and dependency injection.
*   `model.py`: SQLAlchemy database models (`User`, `Todo`).
*   `validation.py`: Pydantic schemas for request and response validation.
*   `auth.py`: Authentication logic, password hashing, and token generation.
*   `database.py`: Database connection and session configuration.

## ⚡ Getting Started

### Prerequisites

*   Python 3.10 or higher
*   pip (Python package manager)

### Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd todo-api
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

## 📖 API Documentation

FastAPI provides automatic interactive documentation. Once the server is running, navigate to:

*   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
    Test the API endpoints directly from your browser.
*   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
    Alternative API documentation.

## 🔑 Key Endpoints

### Authentication
*   `POST /users/`: Register a new user.
*   `POST /token`: Login to get an access token.

### Todos (Requires Authentication)
*   `POST /todos/`: Create a new todo item.
*   `GET /todos/`: Retrieve all todo items for the logged-in user.
*   `PUT /todos/{todo_id}`: Update an existing todo.
*   `DELETE /todos/{todo_id}`: Delete a todo.

## ⚠️ Configuration

The application currently uses a default secret key in `auth.py`. For production use, **you must change this** to a secure, random environment variable.

```python
# auth.py
SECRET_KEY = "your-secret-key-keep-it-secret" # Change this!
```
