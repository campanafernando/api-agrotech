from sqlalchemy import Column, Integer, String #Column: define a posição do conteúdo em colunas
#Integer e String: define o tipo de conteúdo a ser inserido

from database import Base

class AgroSCR(Base):
    __tablename__ = "finançasagro"

    id: int = Column(Integer, primary_key=True, index=True)
    nomeempresa: str = Column(String(100), nullable=False)
    SCORESERASA: int = Column(Integer, nullable=False)
    CNPJ: int = Column(Integer, nullable=False)
    CPF: int = Column(Integer, nullable=False)
