from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from passlib.context import CryptContext
from models.user_models import User
from database import db
from auth.jwt_handler import create_token
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"])
user_collection = db["users"]

@router.post("/auth/register")
def register(user: User):
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail= "Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    user_collection.insert_one({
        "email": user.email,
        "password": hashed_password
    })
    logger.info(f"New user registered: {user.email}")
    return {"message": "User registered successfully"}


@router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = user_collection.find_one({"email": form_data.username})
    if not db_user:
        logger.warning(f"Login failed - user not found: {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not pwd_context.verify(form_data.password, db_user["password"]):
        logger.warning(f"Login failed - wrong password: {form_data.username}")
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_token({"email": form_data.username})
    logger.info(f"User logged in: {form_data.username}")
    return {"access_token": token, "token_type": "bearer"}
    