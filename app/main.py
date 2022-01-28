from fastapi import FastAPI
from api.translateAPI import translate

app = FastAPI()

app.include_router(translate, prefix='/api/v1/translate')
