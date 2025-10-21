from pydantic import BaseModel
#from pydantic import BaseModel, EmailStr
from datetime import datetime
# Schema base com os campos comuns
class PessoaBase(BaseModel):
    nome: str
    endereco: str
    telefone: str
    email: str #| EmailStr

class PessoaCreate(PessoaBase):
    pass

class Pessoa(PessoaBase):
    pessoa_id: int
    data_cadastro: datetime
    class Config:
        orm_mode = True