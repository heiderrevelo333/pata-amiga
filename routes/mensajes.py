from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Mensaje
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/mensajes", tags=["Mensajes"])


class MensajeBase(BaseModel):
    id_remitente: int
    id_destinatario: int
    contenido: str
    estado: Optional[str] = "no_leido"

    class Config:
        from_attributes = True


class MensajeCreate(MensajeBase):
    pass


class MensajeUpdate(BaseModel):
    contenido: Optional[str] = None
    estado: Optional[str] = None


@router.get("/")
def listar_mensajes(db: Session = Depends(get_db)):
    """Listar todos los mensajes"""
    mensajes = db.query(Mensaje).all()
    return mensajes


@router.get("/{mensaje_id}")
def obtener_mensaje(mensaje_id: int, db: Session = Depends(get_db)):
    """Obtener un mensaje por ID"""
    mensaje = db.query(Mensaje).filter(Mensaje.id_mensaje == mensaje_id).first()
    if not mensaje:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    return mensaje


@router.get("/usuario/{usuario_id}/enviados")
def listar_mensajes_enviados(usuario_id: int, db: Session = Depends(get_db)):
    """Listar mensajes enviados por un usuario"""
    mensajes = db.query(Mensaje).filter(Mensaje.id_remitente == usuario_id).all()
    return mensajes


@router.get("/usuario/{usuario_id}/recibidos")
def listar_mensajes_recibidos(usuario_id: int, db: Session = Depends(get_db)):
    """Listar mensajes recibidos por un usuario"""
    mensajes = db.query(Mensaje).filter(Mensaje.id_destinatario == usuario_id).all()
    return mensajes


@router.get("/usuario/{usuario_id}/no-leidos")
def listar_mensajes_no_leidos(usuario_id: int, db: Session = Depends(get_db)):
    """Listar mensajes no leídos de un usuario"""
    mensajes = db.query(Mensaje).filter(
        Mensaje.id_destinatario == usuario_id,
        Mensaje.estado == "no_leido"
    ).all()
    return mensajes


@router.post("/", status_code=201)
def crear_mensaje(mensaje: MensajeCreate, db: Session = Depends(get_db)):
    """Crear un nuevo mensaje"""
    nuevo_mensaje = Mensaje(**mensaje.dict())
    db.add(nuevo_mensaje)
    db.commit()
    db.refresh(nuevo_mensaje)
    return nuevo_mensaje


@router.put("/{mensaje_id}")
def actualizar_mensaje(mensaje_id: int, mensaje: MensajeUpdate, db: Session = Depends(get_db)):
    """Actualizar un mensaje"""
    db_mensaje = db.query(Mensaje).filter(Mensaje.id_mensaje == mensaje_id).first()
    if not db_mensaje:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    
    datos = mensaje.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_mensaje, key, value)
    
    db.commit()
    db.refresh(db_mensaje)
    return db_mensaje


@router.delete("/{mensaje_id}", status_code=204)
def eliminar_mensaje(mensaje_id: int, db: Session = Depends(get_db)):
    """Eliminar un mensaje"""
    mensaje = db.query(Mensaje).filter(Mensaje.id_mensaje == mensaje_id).first()
    if not mensaje:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    
    db.delete(mensaje)
    db.commit()
    return None
