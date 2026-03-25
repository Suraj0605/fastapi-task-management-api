import time, logging
from fastapi import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s, %(message)s"
)
logger = logging.getLogger(__name__)

async def log_middleware(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    end_time = time.time()
    duration = round(end_time - start_time, 4)
    logger.info(f"response: {response.status_code} | Time: {duration}s")

    return response




    