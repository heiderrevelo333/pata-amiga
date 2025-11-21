from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Contacto
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/contactos", tags=["Contactos"])


class ContactoBase(BaseModel):
    id_usuario: int
    id_servicio: int
    asunto: Optional[str] = None
    mensaje: Optional[str] = None

    class Config:
        from_attributes = True


class ContactoCreate(ContactoBase):
    pass


class ContactoUpdate(BaseModel):
    asunto: Optional[str] = None
    mensaje: Optional[str] = None


@router.get("/")
def listar_contactos(db: Session = Depends(get_db)):
    """Listar todos los contactos"""
    contactos = db.query(Contacto).all()
    return contactos


@router.get("/{contacto_id}")
def obtener_contacto(contacto_id: int, db: Session = Depends(get_db)):
    """Obtener un contacto por ID"""
    contacto = db.query(Contacto).filter(Contacto.id_contacto == contacto_id).first()
    if not contacto:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    return contacto


@router.get("/usuario/{usuario_id}")
def listar_contactos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Listar contactos de un usuario"""
    contactos = db.query(Contacto).filter(Contacto.id_usuario == usuario_id).all()
    return contactos


@router.get("/servicio/{servicio_id}")
def listar_contactos_servicio(servicio_id: int, db: Session = Depends(get_db)):
    """Listar contactos de un servicio"""
    contactos = db.query(Contacto).filter(Contacto.id_servicio == servicio_id).all()
    return contactos


@router.post("/", status_code=201)
def crear_contacto(contacto: ContactoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo contacto"""
    nuevo_contacto = Contacto(**contacto.dict())
    db.add(nuevo_contacto)
    db.commit()
    db.refresh(nuevo_contacto)
    return nuevo_contacto


@router.put("/{contacto_id}")
def actualizar_contacto(contacto_id: int, contacto: ContactoUpdate, db: Session = Depends(get_db)):
    """Actualizar un contacto"""
    db_contacto = db.query(Contacto).filter(Contacto.id_contacto == contacto_id).first()
    if not db_contacto:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    datos = contacto.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_contacto, key, value)
    
    db.commit()
    db.refresh(db_contacto)
    return db_contacto


@router.delete("/{contacto_id}", status_code=204)
def eliminar_contacto(contacto_id: int, db: Session = Depends(get_db)):
    """Eliminar un contacto"""
    contacto = db.query(Contacto).filter(Contacto.id_contacto == contacto_id).first()
    if not contacto:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    db.delete(contacto)
    db.commit()
    return None
