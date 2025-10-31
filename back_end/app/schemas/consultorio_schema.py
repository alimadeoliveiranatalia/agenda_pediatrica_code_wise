# Classes de representação de dados da API, definem a estrutura JSON para as requisições e respostas
from pydantic import BaseModel

class ConsultorioBase(BaseModel):
   nome_consultorio: str
   endereco: str

class ConsultorioCreate(ConsultorioBase):
   pass

class Consultorio(ConsultorioBase):
   consultorio_id: int

   class Config:
      orm_mode = True
   