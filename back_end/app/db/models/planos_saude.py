from sqlalchemy import Column, Integer, String
from ..database import Base

class PlanoSaude(Base):
    __tablename__ = "planos_saude"
    plano_saude_id=Column(Integer, primary_key=True, index=True)
    nome_convenio=Column(String)
    limite_consultas_mes=Column(Integer)