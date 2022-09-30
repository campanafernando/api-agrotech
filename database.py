#este diretório faz a conexão com o banco de dados SQL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base #importações necessárias
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3" #string de conexão com o bd

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #sessão no banco de dados
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()