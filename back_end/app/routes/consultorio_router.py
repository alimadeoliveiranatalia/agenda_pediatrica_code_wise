from fastapi import APIRouter, status, HTTPException, Depends 
from app.schemas import consultorio_schema
from sqlalchemy.orm import Session 
from app.services.consultorio_service import consultorio_service
from ..db.database import get_db
router = APIRouter(
    prefix="/consultorios",
    tags=["Consultórios"]
)

@router.post(
    "/",
    response_model=consultorio_schema.Consultorio,
    status_code= status.HTTP_201_CREATED
)
def registrar_consultorio(consultorio_data: consultorio_schema.ConsultorioCreate, db: Session = Depends(get_db)):
    novo_consultorio = consultorio_service.cadastrarConsultorio(consultorio_data, db)
    if not novo_consultorio:
        raise HTTPException(
            status_code=404,
            detail="Consultório não foi encontrado"
        )
    return novo_consultorio
@router.get(
    "/{consultorio_id}",
    response_model=consultorio_schema.Consultorio
)
def encontrar_consultorio(consultorio_id: int, db:Session = Depends(get_db)):
    consultorio = consultorio_service.buscarConsultorio(consultorio_id, db)
    if not consultorio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este Consultório não Existe"
        )