# https://github.com/hogeline/sample_fastapi
from datetime import datetime, date

import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends, Header, HTTPException
from typing import List

from sqlalchemy import TIMESTAMP, and_
from sqlalchemy.orm import Session
from starlette import status
from starlette.background import BackgroundTasks
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from checklist import checklist
# from VR20_SYSTEM import system
# from recipe import recipe
# from server import server
# from result import result
# from machinemodel import machinemodel




app = FastAPI(
    title="Get data from DB",
    description="get from api BELOW",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(checklist.checklist,
                    tags=["CHECKLIST"],
                    responses={200: {"message": "OK"}}
                    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8082, log_level="info")
