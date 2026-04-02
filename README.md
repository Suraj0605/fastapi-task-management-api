# Task Management Backend API

A RESTful backend service for managing tasks built with **FastAPI**, featuring **JWT authentication**, **Redis caching**, and **MongoDB** integration.

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- Redis
- JWT Authentication
- Pydantic

---

## Features

- CRUD operations for tasks
- JWT Authentication & Authorization
- Redis caching for faster responses
- Request logging middleware
- CORS support
- Data validation with Pydantic

---

## Project Structure

```
auth/           → JWT authentication logic
routes/         → API endpoint definitions
models/         → Pydantic schemas
middleware/     → request logging middleware
database.py     → MongoDB connection setup
redis_client.py → Redis caching configuration
main.py         → FastAPI application entry point
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Suraj0605/fastapi-task-management-api.git
```

### 2. Navigate to the project folder

```bash
cd fastapi-task-management-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Open API documentation

```
http://localhost:8000/docs
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|------|------|------|
| POST | /auth/register | Register a new user |
| POST | /auth/login | Login and get JWT token |

### Tasks

| Method | Endpoint | Description |
|------|------|------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

---

## Author

**Suraj Shrivastava**   
Computer Engineering Student | Backend Developer  
LinkedIn: [https://linkedin.com/in/suraj-shrivastava](https://www.linkedin.com/in/suraj-shrivastava-3a69b0254/)
