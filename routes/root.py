from fastapi import APIRouter
import os
from dotenv import load_dotenv
load_dotenv()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Health check main server route listener
root_router = APIRouter(
    tags=['Root']
)

@root_router.get("/home")
async def read_root():
    return {"apizillams": "up and running"}