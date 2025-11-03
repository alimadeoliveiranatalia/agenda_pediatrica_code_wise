from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import funcionario_schema
from app.services.funcionario_service import funcionario_service

router = APIRouter(
    prefix="/funcionarios",
    tags=["Funcionários"]
)
@router.post(
    "/",
    response_model=funcionario_schema.Funcionario,
    status_code= status.HTTP_201_CREATED
)
def registrar_funcionario(funcionario_data: funcionario_schema.FuncionarioCreate, db: Session = Depends(get_db)):
    return funcionario_service.cadastrar(funcionario_data,db)

@router.get(
    "/{id_funcionario}",
    response_model=funcionario_schema.Funcionario,
    #status = status.HTTP_200_SUCCESS
)
def encontrar_funcionario(id_funcionario: int, db: Session = Depends(get_db)):
    return funcionario_service.buscar_funcionario(id_funcionario, db) 
# padrão REST
# criar -> POST
# ler ou buscar -> GET
# atualizar uma nunica informação -> PATCH
#atualizar toda a estrutura -> PUT
# apagar a informação -> DELETE 
# Recebimento de parâmetros e informaçoes
# body -> corpo da requisição
# query params -> na url
# query -> definir paramentros chave e valor na requisição