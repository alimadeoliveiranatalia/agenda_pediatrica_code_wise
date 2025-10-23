from pydantic import BaseModel

class ConsultorioBase(BaseModel):
   nome_consultorio: str
   endereco: str

class ConsultorioCreate(ConsultorioBase):
   pass

class Consultorio(ConsultorioBase):
   consultorio_id: int 
   