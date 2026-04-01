from fastapi import APIRouter, Depends
from bson import ObjectId
from models.task_models import Task
from database import tasks_collection
from auth.jwt_handler import verify_token
from redis_client import redis_client
import json
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/tasks/")
def create_data(data: Task, user: str = Depends(verify_token)):
    task_dict = data.dict()
    tasks_collection.insert_one(task_dict)
    redis_client.delete("tasks")
    logger.info(f"Task created by {user}")
    return {"message": "Task created"}

@router.get("/tasks/")
def get_data(user: str = Depends(verify_token)):
    cached_tasks = redis_client.get("tasks")
    if cached_tasks:
        logger.info(f"Tasks fetched from cache by {user}")
        return json.loads(cached_tasks)
    tasks = []
    for task in tasks_collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    redis_client.set("tasks", json.dumps(tasks), ex=60)
    logger.info(f"Tasks fetched from MongoDB by {user}")
    return tasks

@router.put("/tasks/{id}")
def update_data(id: str, data: Task, user: str = Depends(verify_token)):
    tasks_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data.dict()}
    )
    redis_client.delete("tasks")
    logger.info(f"Task updated by {user} | id: {id}")
    return {"message": "Updated successfully"}

@router.delete("/tasks/{id}")
def delete_data(id: str, user: str = Depends(verify_token)):
    tasks_collection.delete_one({"_id": ObjectId(id)})
    redis_client.delete("tasks")
    logger.info(f"Task deleted by {user} | id: {id}")
    return {"message": "Deleted successfully"}
