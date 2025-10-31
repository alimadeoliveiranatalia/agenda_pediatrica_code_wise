from typing import Optional
from app.schemas import consultorio_schema
from sqlalchemy.orm import Session # type: ignore
from app.repositories.consultorio_repository import consultorio_repository


class ConsultorioService():
    def cadastrarConsultorio(self, consultorio_data: consultorio_schema.ConsultorioCreate, db:Session) -> Optional[consultorio_schema.Consultorio]:
        """Regras de negócios para registro de consultorios"""
        return consultorio_repository.create(consultorio_data, db)
    
    def buscarConsultorio(self, id_consultorio: int, db: Session) -> Optional[consultorio_schema.Consultorio]:
        """ Encontrar se o Conultório existe """
        consultorio = consultorio_repository.get_consultorio_by_id(id_consultorio, db)

        if not consultorio:
            raise ValueError('Consultório não Existe')

        return consultorio

consultorio_service = ConsultorioService()