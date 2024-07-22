from fastapi import APIRouter
import os
import requests
from dotenv import load_dotenv
load_dotenv()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ESB main server route listener
esb_router = APIRouter(
    # prefix='/esb',
    tags=['Enterprise Service Bus (ESB)']
)

@esb_router.get("/health/{server_name}")
async def health(server_name: str):
    r = requests.get(os.getenv("ESB_HEALTH_CHECK_" + server_name.upper()))
    return {"status": r.status_code, "message": r.text}

