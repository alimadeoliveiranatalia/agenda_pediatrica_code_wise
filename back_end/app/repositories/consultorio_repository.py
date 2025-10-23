from typing import Optional
import random
from app.schemas import consultorio_schema

db_consultorio = []

class ConsultorioRepository():
    def create(self, consultorio_data: consultorio_schema.ConsultorioCreate ) -> Optional[consultorio_schema.Consultorio]:  
        """ Registra um novo consultorio no banco de Dados. """
        novo_consultorio = consultorio_schema.Consultorio(
            consultorio_id = random.randint(1,250),
            **consultorio_data.dict()
        )
        db_consultorio.append(novo_consultorio)
        return novo_consultorio
    
    def get_consultorio_by_id(id_consultorio: int) -> Optional[consultorio_schema.Consultorio]:
        """ Efetua a busca de um consultorio no banco de dados pelo ID"""
        for consultorio in db_consultorio:
            if(consultorio.consultorio_id == id_consultorio ):
                return consultorio
        return None
consultorio_repository = ConsultorioRepository()