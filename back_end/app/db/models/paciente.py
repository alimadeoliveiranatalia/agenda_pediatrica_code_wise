from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from ..database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    paciente_id= Column(Integer, primary_key=True, index=True)
    nome= Column(String, nullable=False)
    endereco = Column(String)
    telefone= Column(String, nullable= False)
    email=Column(String, unique=True, index=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    data_primeira_consulta = Column(DateTime, nullable=False)
    id_plano_saude = Column(Integer, ForeignKey("planos_saude.plano_saude_id"))
