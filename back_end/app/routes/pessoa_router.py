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

@router.get(
    "/{id_pessoa}",
    response_model=pessoa_schema.Pessoa,
    #status = status.HTTP_200_SUCCESS
)
def encontrar_pessoa(id_pessoa: int):
    pessoa = pessoa_service.buscar_pessoa(id_pessoa)
    return pessoa 
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