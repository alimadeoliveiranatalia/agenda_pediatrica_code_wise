from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class PacienteBase(BaseModel):
   nome: str
   endereco: str
   telefone: str
   email: str
   data_nascimento: date
   data_primeira_consulta: datetime
   id_plano_saude: Optional[int] = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    paciente_id: int
    
    class Config:
        orm_mode: True