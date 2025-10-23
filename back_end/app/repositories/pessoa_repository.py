import random
from typing import Optional
from datetime import datetime
from app.schemas import pessoa_schema
# Simulação do Banco de dados
# uma lista para guardar os dados de pessoas
db_pessoa = []

class PessoaRepository:
    #def create_1(nome, endereco, telefone, email):
    #    pessoa =  pessoa_schema.Pessoa(
    #        pessoa_id = random.randint(150,200), # gerador de valores aleatórios
    #        data_cadastro = datetime.now(),  # cadastrar a data de registro da pessoa
    #        nome,
    #        endereco,
    #        telefone,
    #        email,
    #    )
    def create(self, pessoa_data: pessoa_schema.PessoaCreate) -> Optional[pessoa_schema.Pessoa]: 
        pessoa = pessoa_schema.Pessoa(
            pessoa_id = random.randint(150,200),
            data_cadastro = datetime.now(),
            **pessoa_data.dict() #Desempacota os dados do schema de criação
        )
        db_pessoa.append(pessoa)
        return pessoa
    
    def find_person_id(self, id_pessoa: int) -> Optional[pessoa_schema.Pessoa]:
        for pessoa in db_pessoa:
            if pessoa.pessoa_id == id_pessoa:
                return pessoa
        return None

# Exportamos uma instância única do repositório para ser usada em toda a aplicação (Singleton Pattern)
pessoa_repository = PessoaRepository()