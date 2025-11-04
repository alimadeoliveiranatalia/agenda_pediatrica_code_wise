from sqlalchemy.orm import Session
from app.repositories.planos_saude_repository import planos_saude_repository
from app.schemas import plano_saude_schema

class PlanoSaudeService:
   def listarTodosOsPlanos(self, db: Session):
      """Regras de negócio para obter todos os planos listados """
      return planos_saude_repository.get_all(db)
   def buscaPlanoID(self, db, plano_id):
      """Regra de negócio para buscar um plano de saúde por ID """
      return planos_saude_repository.get_by_id(db, plano_id)
   def registarPlanoSaude(self, db: Session, plano_saude_data: plano_saude_schema.PlanoSaudeCreate):
      """Regra de negócio para registrar um plano de saude no banco de dados"""
      return planos_saude_repository.create(db, plano_saude_data)
planos_saude_service = PlanoSaudeService()