from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITILE, version=settings.PROJECT_Version)

@app.get('/')
def home():
    return {"name":"Shiva kant Mishra"}