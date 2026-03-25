from fastapi import APIRouter, Depends
from bson import ObjectId
from models.todo_models import Todo
from database import todos_collection
from auth.jwt_handler import verify_token
from redis_client import redis_client
import json
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/items/")
def create_data(data: Todo, user: str = Depends(verify_token)):
    todo_dict = data.dict()
    result = todos_collection.insert_one(todo_dict)
    redis_client.delete("todos")
    logger.info(f"Todo created by {user}")
    return {"message": "Todo created"}

@router.get("/items/")
def get_data(user: str = Depends(verify_token)):
    cached_todos = redis_client.get("todos")
    if cached_todos:
        logger.info(f"Todos fetched from cache by {user}")
        return json.loads(cached_todos)  
    todos = []
    for todo in todos_collection.find():
        todo["_id"] = str(todo["_id"])
        todos.append(todo)

    redis_client.set("todos", json.dumps(todos), ex=60)   
    logger.info(f"Todos fetched from MongoDB by {user}")
    return todos

@router.put("/items/{id}")
def update_data(id: str, data: Todo, user: str = Depends(verify_token)):
    todos_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data.dict()}
    )
    redis_client.delete("todos")
    logger.info(f"Todo updated by {user} | id: {id}")
    return {"message": "Updated successfully"}

@router.delete("/items/{id}")
def delete_data(id: str, user: str = Depends(verify_token)):
    todos_collection.delete_one(
        {"_id": ObjectId(id)}
    )
    redis_client.delete("todos")
    logger.info(f"Todo deleted by {user} | id: {id}")
    return {"message": "Deleted successfully"}


