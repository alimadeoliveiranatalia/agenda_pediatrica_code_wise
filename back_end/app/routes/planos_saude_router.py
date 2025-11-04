from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import plano_saude_schema
from app.services.planos_saude_service import planos_saude_service
router = APIRouter(
    prefix="/planos_saude",
    tags=["Planos de Saúde"]
)
@router.post(
    "/",
    response_model=plano_saude_schema.PlanoSaude,
    status_code= status.HTTP_201_CREATED
)
def registrar_plano_saude(plano_saude_data: plano_saude_schema.PlanoSaudeCreate, db: Session = Depends(get_db)):
    return planos_saude_service.registarPlanoSaude(db, plano_saude_data)

@router.get(
        "/list_all_planos",
    response_model=List[plano_saude_schema.PlanoSaude]
)
def list_all_planos(db:Session = Depends(get_db)):
    return planos_saude_service.listarTodosOsPlanos(db)

@router.get(
    "/{plano_id}",
    response_model=plano_saude_schema.PlanoSaude,
    #status = status.HTTP_200_SUCCESS
)
def encontrar_plano_saude(plano_id: int, db: Session = Depends(get_db)):
    return planos_saude_service.buscaPlanoID(db,plano_id)