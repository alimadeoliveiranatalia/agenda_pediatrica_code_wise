from pydantic import BaseModel
from typing import Optional

class PlanoSaudeBase(BaseModel):
    nome_convenio: str
    limite_consultas_mes: Optional[int] = None

class PlanoSaudeCreate(PlanoSaudeBase):
    pass

class PlanoSaude(PlanoSaudeBase):
    plano_saude_id: int

    class Config:
        orm_mode = True