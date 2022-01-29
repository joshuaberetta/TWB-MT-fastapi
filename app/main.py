from fastapi import FastAPI

from config import settings
from api import translate_router

app = FastAPI()

app.include_router(translate_router)

