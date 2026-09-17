from fastapi import FastAPI

from database import engine
from models import Base

app = FastAPI(title="Docker")

Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "project is working!"}
