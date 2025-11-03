import random
from typing import Optional
from datetime import datetime
from ..schemas import funcionario_schema
from sqlalchemy.orm import Session
from ..db.models import funcionario as funcionario_model

class FuncionarioRepository:
    #def create_1(nome, endereco, telefone, email):
    #    pessoa =  pessoa_schema.Pessoa(
    #        pessoa_id = random.randint(150,200), # gerador de valores aleatórios
    #        data_cadastro = datetime.now(),  # cadastrar a data de registro da pessoa
    #        nome,
    #        endereco,
    #        telefone,
    #        email,
    #    )
    def create(self, funcionario_data: funcionario_schema.FuncionarioCreate, db: Session) -> Optional[funcionario_model.Funcionario]: 
        """ Registra um novo funcionario no sistema. """
        novo_funcionario = funcionario_model.Funcionario(            
            **funcionario_data.dict() #Desempacota os dados do schema de criação
        )
        db.add(novo_funcionario)
        db.commit()
        db.refresh(novo_funcionario)
        return novo_funcionario
    
    def find_funcionario_id(self, id_funcionario: int, db: Session) -> Optional[funcionario_model.Funcionario]:
        """ Busca um funcionário pelo seu ID """
        return db.query(funcionario_model.Funcionario).filter(funcionario_model.Funcionario.funcionario_id == id_funcionario).first()

# Exportamos uma instância única do repositório para ser usada em toda a aplicação (Singleton Pattern)
funcionario_repository = FuncionarioRepository()