from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Compra
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

router = APIRouter(prefix="/compras", tags=["Compras"])


class CompraBase(BaseModel):
    id_usuario: int
    id_producto: int
    cantidad: Optional[int] = 1
    total: Decimal
    estado: Optional[str] = "pendiente"

    class Config:
        from_attributes = True


class CompraCreate(CompraBase):
    pass


class CompraUpdate(BaseModel):
    cantidad: Optional[int] = None
    total: Optional[Decimal] = None
    estado: Optional[str] = None


@router.get("/")
def listar_compras(db: Session = Depends(get_db)):
    """Listar todas las compras"""
    compras = db.query(Compra).all()
    return compras


@router.get("/{compra_id}")
def obtener_compra(compra_id: int, db: Session = Depends(get_db)):
    """Obtener una compra por ID"""
    compra = db.query(Compra).filter(Compra.id_compra == compra_id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra


@router.get("/usuario/{usuario_id}")
def listar_compras_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Listar compras de un usuario"""
    compras = db.query(Compra).filter(Compra.id_usuario == usuario_id).all()
    return compras


@router.post("/", status_code=201)
def crear_compra(compra: CompraCreate, db: Session = Depends(get_db)):
    """Crear una nueva compra"""
    nueva_compra = Compra(**compra.dict())
    db.add(nueva_compra)
    db.commit()
    db.refresh(nueva_compra)
    return nueva_compra


@router.put("/{compra_id}")
def actualizar_compra(compra_id: int, compra: CompraUpdate, db: Session = Depends(get_db)):
    """Actualizar una compra"""
    db_compra = db.query(Compra).filter(Compra.id_compra == compra_id).first()
    if not db_compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    
    datos = compra.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_compra, key, value)
    
    db.commit()
    db.refresh(db_compra)
    return db_compra


@router.delete("/{compra_id}", status_code=204)
def eliminar_compra(compra_id: int, db: Session = Depends(get_db)):
    """Eliminar una compra"""
    compra = db.query(Compra).filter(Compra.id_compra == compra_id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    
    db.delete(compra)
    db.commit()
    return None
