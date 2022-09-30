from sqlalchemy.orm import Session

from models import AgroSCR

class AgroSCRRepository:
    @staticmethod
    def find_all(db: Session) -> list[AgroSCR]: #método responsável por buscar todos os clientes cadastrados;
        return db.query(AgroSCR).all()

    @staticmethod
    def save(db: Session, scr: AgroSCR) -> AgroSCR: #método responsável por salvar um novo cliente no banco de dados;

        if scr.id:
            db.merge(scr)
        else:
            db.add(scr)
        db.commit()
        return scr

    @staticmethod
    def find_by_id(db: Session, id: int) -> AgroSCR: #método responsável por buscar um cliente no banco de dados com base do id;
        return db.query(AgroSCR).filter(AgroSCR.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:  #método responsável por excluir um curso com base no seu id;
        return db.query(AgroSCR).filter(AgroSCR.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        scr = db.query(AgroSCR).filter(AgroSCR.id == id).first()
        if scr is not None:
            db.delete(scr)
            db.commit()