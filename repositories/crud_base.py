from sqlalchemy.orm import Session

class CRUDBase:

    def __init__(self, model):
        self.model = model

    # LISTAR
    def get_all(self, db: Session):
        return db.query(self.model).all()

    # BUSCAR POR ID
    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    # CREAR
    def create(self, db: Session, obj_data: dict):
        obj = self.model(**obj_data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    # ACTUALIZAR
    def update(self, db: Session, id: int, obj_data: dict):
        obj = db.query(self.model).filter(self.model.id == id).first()

        for key, value in obj_data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)
        return obj

    # ELIMINAR
    def delete(self, db: Session, id: int):
        obj = db.query(self.model).filter(self.model.id == id).first()
        db.delete(obj)
        db.commit()
        return obj