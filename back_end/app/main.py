from typing import Union

from app.routes import consultorio_router
from fastapi import FastAPI

from app.routes import funcionario_router

app = FastAPI()

app.include_router(funcionario_router.router)

app.include_router(consultorio_router.router)
