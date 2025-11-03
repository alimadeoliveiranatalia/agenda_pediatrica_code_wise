from pydantic import BaseModel, EmailStr
#from pydantic import BaseModel, EmailStr
from datetime import datetime
# Schema base com os campos comuns
class FuncionarioBase(BaseModel):
    nome: str
    email: EmailStr
    cargo: str

class FuncionarioCreate(FuncionarioBase):
    pass

class Funcionario(FuncionarioBase):
    funcionario_id: int
    class Config:
        orm_mode = True