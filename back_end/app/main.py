from typing import Union

from app.routes import consultorio_router
from fastapi import FastAPI

from app.routes import pessoa_router

app = FastAPI()

app.include_router(pessoa_router.router)

app.include_router(consultorio_router.router)
