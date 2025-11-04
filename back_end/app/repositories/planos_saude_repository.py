from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas import plano_saude_schema
from app.db.models import planos_saude
class PlanoSaudeRepository:
    
    def get_all(self, db: Session) -> List[planos_saude.PlanoSaude]:
        """ Chama todos os planos de saude registrados"""
        return db.query(planos_saude.PlanoSaude)
    
    def get_by_id(sel, db:Session, plano_id) -> Optional[planos_saude.PlanoSaude]:
        """ Buscar um plano de saude por ID """
        return db.query(planos_saude.PlanoSaude).filter(planos_saude.PlanoSaude.plano_saude_id == plano_id).first()
    
    def create(self, db: Session, plano_saude_data: plano_saude_schema.PlanoSaudeCreate) -> planos_saude.PlanoSaude :
        """ Registrar um novo plano de saúdono banco de dados"""
        novo_plano_saude = planos_saude.PlanoSaude(
            **plano_saude_data.dict()
        )
        db.add(novo_plano_saude)
        db.commit()
        db.refresh(novo_plano_saude)
        return novo_plano_saude
    
planos_saude_repository = PlanoSaudeRepository()