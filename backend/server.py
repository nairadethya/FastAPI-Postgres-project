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

@app.get("/videos", response_model=List[VideoModel])
async def get_videos():
    # Connect to our database
    conn = psycopg2.connect(
        database = "exampledb", user = "docker", password = "docker", host = "0.0.0.0"
    )

    cur = conn.cursor[]
    cur.execute["SELECT * FROM video ORDER BY Id "]
    rows = cur.fetchall()
    formatted_videos = []
    for row in rows:
        formatted_videos.append(
            VideoModel(id=row[0], video_title=row[1], video_url=row[2])
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port="8000", reload=False)