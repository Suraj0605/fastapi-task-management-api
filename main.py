from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.task_routes import router as task_router
from routes.auth_routes import router as auth_router
from middleware.logger_middleware import log_middleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.middleware("http")(log_middleware)

app.include_router(task_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Welcome to Task API!"}

