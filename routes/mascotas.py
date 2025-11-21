from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Mascota
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/mascotas", tags=["Mascotas"])


class MascotaBase(BaseModel):
    id_usuario: int
    nombre: str
    raza: Optional[str] = None
    edad: Optional[int] = None
    tipo: Optional[str] = None
    lipo: Optional[str] = None
    alergias: Optional[str] = None
    estado: Optional[str] = None

    class Config:
        from_attributes = True


class MascotaCreate(MascotaBase):
    pass


class MascotaUpdate(BaseModel):
    nombre: Optional[str] = None
    raza: Optional[str] = None
    edad: Optional[int] = None
    tipo: Optional[str] = None
    lipo: Optional[str] = None
    alergias: Optional[str] = None
    estado: Optional[str] = None


@router.get("/")
def listar_mascotas(db: Session = Depends(get_db)):
    """Listar todas las mascotas"""
    mascotas = db.query(Mascota).all()
    return mascotas


@router.get("/{mascota_id}")
def obtener_mascota(mascota_id: int, db: Session = Depends(get_db)):
    """Obtener una mascota por ID"""
    mascota = db.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.get("/usuario/{usuario_id}")
def listar_mascotas_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Listar mascotas de un usuario"""
    mascotas = db.query(Mascota).filter(Mascota.id_usuario == usuario_id).all()
    return mascotas


@router.post("/", status_code=201)
def crear_mascota(mascota: MascotaCreate, db: Session = Depends(get_db)):
    """Crear una nueva mascota"""
    nueva_mascota = Mascota(**mascota.dict())
    db.add(nueva_mascota)
    db.commit()
    db.refresh(nueva_mascota)
    return nueva_mascota


@router.put("/{mascota_id}")
def actualizar_mascota(mascota_id: int, mascota: MascotaUpdate, db: Session = Depends(get_db)):
    """Actualizar una mascota"""
    db_mascota = db.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()
    if not db_mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    
    datos = mascota.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_mascota, key, value)
    
    db.commit()
    db.refresh(db_mascota)
    return db_mascota


@router.delete("/{mascota_id}", status_code=204)
def eliminar_mascota(mascota_id: int, db: Session = Depends(get_db)):
    """Eliminar una mascota"""
    mascota = db.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    
    db.delete(mascota)
    db.commit()
    return None
