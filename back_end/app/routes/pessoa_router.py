from fastapi import APIRouter, status
from app.schemas import pessoa_schema
from app.services.pessoa_service import pessoa_service

router = APIRouter(
    prefix="/pessoas",
    tags=["Pessoas"]
)
@router.post(
    "/",
    response_model=pessoa_schema.Pessoa,
    status_code= status.HTTP_201_CREATED
)
def registrar_pessoa(pessoa_data: pessoa_schema.PessoaCreate):
    pessoa = pessoa_service.cadastrar(pessoa_data)
    return pessoa