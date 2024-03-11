from typing import Union
from fastapi import FastAPI

# creacion de una app fastapi
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
