from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Producto
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

router = APIRouter(prefix="/productos", tags=["Productos"])


class ProductoBase(BaseModel):
    id_servicio: int
    nombre: str
    descripcion: Optional[str] = None
    precio: Decimal
    categoria: Optional[str] = None
    stock: Optional[int] = 0
    foto: Optional[str] = None

    class Config:
        from_attributes = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    categoria: Optional[str] = None
    stock: Optional[int] = None
    foto: Optional[str] = None


@router.get("/")
def listar_productos(db: Session = Depends(get_db)):
    """Listar todos los productos"""
    productos = db.query(Producto).all()
    return productos


@router.get("/{producto_id}")
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtener un producto por ID"""
    producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.get("/servicio/{servicio_id}")
def listar_productos_por_servicio(servicio_id: int, db: Session = Depends(get_db)):
    """Listar productos de un servicio"""
    productos = db.query(Producto).filter(Producto.id_servicio == servicio_id).all()
    return productos


@router.post("/", status_code=201)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo producto"""
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    """Actualizar un producto"""
    db_producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    datos = producto.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_producto, key, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto


@router.delete("/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    """Eliminar un producto"""
    producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    return None
