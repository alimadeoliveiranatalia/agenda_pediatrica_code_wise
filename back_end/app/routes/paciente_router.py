from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..schemas.paciente_schema import PacienteCreate, Paciente
from ..services.paciente_service import paciente_service
from ..db.database import get_db

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"]
)
@router.post("/", response_model=Paciente, status_code=201)
def registrar_paciente(paciente_data: PacienteCreate, db: Session = Depends(get_db)):
   return paciente_service.registrar_paciente(db, paciente_data) 

@router.get("/", response_model=List[Paciente])
def buscar_todos_pacientes(db:Session = Depends(get_db)):
    return paciente_service.listar_todos_os_pacientes(db)

@router.get("/{paciente_id}", response_model=Paciente)
def buscar_paciente( paciente_id: int, db:Session = Depends(get_db)):
    paciente = paciente_service.buscar_paciente_por_id(db, paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não registrado")
    return paciente
