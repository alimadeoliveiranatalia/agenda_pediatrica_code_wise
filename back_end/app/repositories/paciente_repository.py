from typing import List, Optional
from sqlalchemy.orm import Session
from ..schemas.paciente_schema import PacienteCreate
from ..db.models import paciente as paciente_model

class PacienteRepository:
    def get_all(self, db: Session) -> List[paciente_model.Paciente]:
        """Retornar todos os pacientes registrado na base de dados."""
        return db.query(paciente_model.Paciente).all()
    def get_by_id(self, db: Session, paciente_id) -> Optional[paciente_model.Paciente]:
        """ Buscar um Paciente pelo ID"""
        return db.query(paciente_model.Paciente).filter(paciente_model.Paciente.paciente_id == paciente_id).first()
    def create(self, db: Session, paciente_data: PacienteCreate) -> paciente_model.Paciente:
       """Registra um novo paciente no banco de dados"""
       novo_paciente = paciente_model.Paciente(
           **paciente_data.dict()
       )
       db.add(novo_paciente)
       db.commit()
       db.refresh(novo_paciente)
       return novo_paciente
paciente_repository = PacienteRepository()