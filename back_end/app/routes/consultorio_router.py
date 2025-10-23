from fastapi import APIRouter, status, HTTPException
from app.schemas import consultorio_schema
from app.services.consultorio_service import consultorio_service
router = APIRouter(
    prefix="/consultorios",
    tags=["Consultórios"]
)

@router.post(
    "/",
    response_model=consultorio_schema.Consultorio,
    status_code= status.HTTP_201_CREATED
)
def registrar_consultorio(consultorio_data: consultorio_schema.ConsultorioCreate):
    novo_consultorio = consultorio_service.cadastrarConsultorio(consultorio_data)
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
def encontrar_consultorio(consultorio_id: int):
    consultorio = consultorio_service.buscarConsultorio(consultorio_id)
    if not consultorio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este Consultório não Existe"
        )