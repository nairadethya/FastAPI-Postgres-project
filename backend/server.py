import boto3
import psycopg2

from typing import List
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI, UploadFile

from fastapi.middleware.cors import CORSMiddleware

class VideoModel(BaseModel):
    id: int
    video_title: str
    video_url: str

app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/status")
async def check_status():
    return "Hello World!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port="8000", reload=False)