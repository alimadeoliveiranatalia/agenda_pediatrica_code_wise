from typing import Union

from app.routes import consultorio_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import funcionario_router, planos_saude_router, paciente_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5641"]
)

app.include_router(funcionario_router.router)

app.include_router(consultorio_router.router)

app.include_router(planos_saude_router.router)

app.include_router(paciente_router.router)
