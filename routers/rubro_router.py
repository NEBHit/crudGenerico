from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.rubro_repositori import rubro_repositori

router = APIRouter(
    prefix="/rubros",
    tags=["rubros"]
)


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return rubro_repositori.get_all(db)


@router.get("/{id}")
def ver(id: int, db: Session = Depends(get_db)):
    return rubro_repositori.get(db, id)


@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    return rubro_repositori.create(db, data)


@router.put("/{id}")
def actualizar(id: int, data: dict, db: Session = Depends(get_db)):
    return rubro_repositori.update(db, id, data)


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return rubro_repositori.delete(db, id)



