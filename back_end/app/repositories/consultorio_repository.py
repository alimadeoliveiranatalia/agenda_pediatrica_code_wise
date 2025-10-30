from typing import Optional
import random
from sqlalchemy.orm import Session # type: ignore
from app.schemas import consultorio_schema
from ..db.models import consultorio

class ConsultorioRepository():
    def create(self, db: Session , consultorio_data: consultorio_schema.ConsultorioCreate ) -> Optional[consultorio.Consultorio]:  
        """ Registra um novo consultorio no banco de Dados. """
        novo_consultorio = consultorio.Consultorio(
            consultorio_id = random.randint(1,250),
            **consultorio_data.dict()
        )
        db.add(novo_consultorio)
        db.commit()
        db.refresh(novo_consultorio)
        return novo_consultorio
    
    def get_consultorio_by_id(id_consultorio: int, db: Session) -> Optional[consultorio.Consultorio]:
        """ Efetua a busca de um consultorio no banco de dados pelo ID"""
        #for consultorio in db_consultorio:
        #    if(consultorio.consultorio_id == id_consultorio ):
        #        return consultorio
        #return None
        return db.query(consultorio.Consultorio).filter(consultorio.Consultorio.consultorio_id == id_consultorio)
consultorio_repository = ConsultorioRepository()