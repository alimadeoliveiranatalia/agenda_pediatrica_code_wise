# Garante a conecxão com o banco de dados
from dotenv import load_dotenv # type: ignore
import os
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker # t# type: ignore
from sqlalchemy.ext.declarative import declarative_base # t# type: ignore

# Carregar as variaveis de ambiente do arquivo .env
load_dotenv()

SQLALCHEmy_DATABASE_URL = os.getenv("DATABASE_URL")

# Verifica se a variável de ambiente foi carregada
if not SQLALCHEmy_DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não foi carregada") # efetuar lançamento de exceções 

engine = create_engine(SQLALCHEmy_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
