from pydantic import BaseModel #Pydantic tem como objetivo prover uma maneira mais simples e direta para realizar validação de dados;

class AgroSCRBase(BaseModel):

    nomeempresa: str
    SCORESERASA: int
    CNPJ: int
    CPF: int

class AgroSCRRequest(AgroSCRBase):
    ...

class AgroSCRResponse(AgroSCRBase):
    id: int

    class Config:
        orm_mode = True
