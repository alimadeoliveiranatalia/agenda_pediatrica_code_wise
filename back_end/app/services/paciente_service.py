from typing import List, Optional
from sqlalchemy.orm import Session
from app.repositories.paciente_repository import paciente_repository
from app.schemas.paciente_schema import PacienteCreate, Paciente

class PacienteService:
    def listar_todos_os_pacientes(self, db: Session) -> List[Paciente]:
        return paciente_repository.get_all(db)
    def registrar_paciente(self, db:Session, paciente_data: PacienteCreate) -> Paciente :
       return paciente_repository.create(db, paciente_data)
    def buscar_paciente_por_id(self, db:Session, id_paciente) -> Optional[Paciente]:
        return paciente_repository.get_by_id(db, id_paciente)

paciente_service = PacienteService()