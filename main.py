from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import AgroSCR
from database import engine, Base, get_db
from repositories import AgroSCRRepository
from schemas import AgroSCRRequest, AgroSCRResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Rota responsável por adicionar novos clientes a lista > método POST;

@app.post("/api/agroscr", response_model=AgroSCRResponse, status_code=status.HTTP_201_CREATED)
def create(request: AgroSCRRequest, db: Session = Depends(get_db)):
    agroscr = AgroSCRRepository.save(db, AgroSCR(**request.dict()))
    return AgroSCRResponse.from_orm(agroscr)

#Rota que será responsável por listar os clientes cadastrados na aplicação;

@app.get("/api/agroscr", response_model=list[AgroSCRResponse])
def find_all(db: Session = Depends(get_db)):
    agroscr = AgroSCRRepository.find_all(db)
    return [AgroSCRResponse.from_orm(agro) for agro in agroscr]

#Rota responsável por buscar um cliente por ID;

@app.get("/api/agroscr/{id}", response_model=AgroSCRResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    agroscr = AgroSCRRepository.find_by_id(db, id)
    if not agroscr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente/Empresa não encontrada"
        )
    return AgroSCRResponse.from_orm(agroscr)

#Rota de exclusão de cliente por id;

@app.delete("/api/agroscr/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not AgroSCRRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente/Empresa não encontrado"
        )
    AgroSCRRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Rota que será responsável por realizar a atualização de um cliente no banco de dados.

@app.put("/api/agroscr/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not AgroSCRRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente/Empresa não encontrado"
        )
    AgroSCRRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)