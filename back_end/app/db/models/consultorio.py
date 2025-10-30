from sqlalchemy import Column, Integer, String # type: ignore
from ..database import Base

class Consultorio(Base):
    __tablename__ = "consultorios"
    consultorio_id= Column(Integer, primary_key=True, index=True)
    nome_consultorio= Column(String)
    endereco= Column(String)