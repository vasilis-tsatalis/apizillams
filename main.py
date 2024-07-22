# Initializes the FastAPI application

#!/usr/bin/python

from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import starlette.status as status
import os

# Import separated routes - Contains router modules
from .routes.root import root_router
from .routes.esb import esb_router

from dotenv import load_dotenv
load_dotenv()

GLOBAL_VAR_URL = os.getenv("API_URL")

app = FastAPI(
    title=os.getenv("API_TITLE"),
    description=os.getenv("API_DESC"),
    version = os.getenv("API_VERSION"),
    openapi_url=GLOBAL_VAR_URL + os.getenv("API_OPENAPI"),
    docs_url=GLOBAL_VAR_URL + os.getenv("API_DOCS"), 
    redoc_url=GLOBAL_VAR_URL + os.getenv("API_REDOC"),
)

# # # BASE ON ROOT DOMAIN # # #

@app.get("/")
async def main():
    # Redirect to {{base}}/ (relative URL)
    return RedirectResponse(url=GLOBAL_VAR_URL + "/home", status_code=status.HTTP_302_FOUND)

@app.get("/openapi")
async def openapi():
    # Redirect to {{base}}/ (relative URL)
    return RedirectResponse(url=GLOBAL_VAR_URL + os.getenv("API_OPENAPI"), status_code=status.HTTP_302_FOUND)

@app.get("/docs")
async def docs():
    # Redirect to {{base}}/ (relative URL)
    return RedirectResponse(url=GLOBAL_VAR_URL + os.getenv("API_DOCS"), status_code=status.HTTP_302_FOUND)

@app.get("/redoc")
async def redoc():
    # Redirect to {{base}}/ (relative URL)
    return RedirectResponse(url=GLOBAL_VAR_URL + os.getenv("API_REDOC"), status_code=status.HTTP_302_FOUND)


# API Engine routes
app.include_router(root_router, prefix=GLOBAL_VAR_URL)
app.include_router(esb_router, prefix=GLOBAL_VAR_URL + '/esb')