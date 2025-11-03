from typing import Optional
from sqlalchemy.orm import Session 
from app.schemas import funcionario_schema
from app.repositories.funcionario_repository import funcionario_repository

class FuncionarioService():
    def cadastrar(self, funcionario_data: funcionario_schema.FuncionarioCreate, db: Session) -> Optional[funcionario_schema.Funcionario]:
        """ Regra de negócio para registrar pessoas no sistema """
        return funcionario_repository.create(funcionario_data, db)
    
    def buscar_funcionario(self, id_funcionario: int, db: Session) -> Optional[funcionario_schema.Funcionario]:
        """Regras de Negócios para busca de funcionarios """
        return funcionario_repository.find_funcionario_id(id_funcionario, db)
funcionario_service = FuncionarioService()