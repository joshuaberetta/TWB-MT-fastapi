from fastapi import FastAPI

from app.config import settings

def create_app() -> FastAPI:
    app = FastAPI()

    from app.celery_utils import create_celery
    app.celery_app = create_celery()

    from app.api import translate_router
    app.include_router(translate_router)

    return app
