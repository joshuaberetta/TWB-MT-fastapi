from fastapi import APIRouter

translate_router = APIRouter(prefix='/api/v1/translate')

from . import translateAPI, tasks
