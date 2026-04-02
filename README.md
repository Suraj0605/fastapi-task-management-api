# Task Management Backend API

A production-ready REST API built with FastAPI and MongoDB.

## Tech Stack
- FastAPI
- MongoDB
- Redis (Caching)
- JWT Authentication
- Pydantic
- Python

## Features
- CRUD operations
- JWT Authentication & Authorization
- Redis Caching
- Middleware & Logging
- CORS
- Data Validation

## Installation

1. Clone the repository

git clone https://github.com/Suraj0605/fastapi-task-management-api.git

2. Navigate to the project folder

cd fastapi-task-management-api

3. Install dependencies

pip install -r requirements.txt

4. Run the server

uvicorn main:app --reload

5. Open API documentation

http://localhost:8000/docs

## API Endpoints

Authentication

POST /auth/register  
POST /auth/login  

Tasks

GET /tasks  
POST /tasks  
PUT /tasks/{id}  
DELETE /tasks/{id}