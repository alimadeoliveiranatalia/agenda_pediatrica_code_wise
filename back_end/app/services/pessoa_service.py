from typing import Optional
from app.schemas import pessoa_schema
from app.repositories.pessoa_repository import pessoa_repository

class PessoaService():
    def cadastrar(self, pessoa_data: pessoa_schema.PessoaCreate) -> Optional[pessoa_schema.Pessoa]:
        """ Regra de negócio para registrar pessoas no sistema """
        return pessoa_repository.create(pessoa_data)
pessoa_service = PessoaService()