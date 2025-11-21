from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Servicio
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/servicios", tags=["Servicios"])


class ServicioBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    ubicacion: Optional[str] = None
    telefono_contacto: Optional[str] = None
    horario_atencion: Optional[str] = None
    calificacion_promedio: Optional[float] = 0.0

    class Config:
        from_attributes = True


class ServicioCreate(ServicioBase):
    pass


class ServicioUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    ubicacion: Optional[str] = None
    telefono_contacto: Optional[str] = None
    horario_atencion: Optional[str] = None
    calificacion_promedio: Optional[float] = None


@router.get("/")
def listar_servicios(db: Session = Depends(get_db)):
    """Listar todos los servicios"""
    servicios = db.query(Servicio).all()
    return servicios


@router.get("/{servicio_id}")
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    """Obtener un servicio por ID"""
    servicio = db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.get("/categoria/{categoria}")
def listar_servicios_por_categoria(categoria: str, db: Session = Depends(get_db)):
    """Listar servicios por categoría"""
    servicios = db.query(Servicio).filter(Servicio.categoria == categoria).all()
    return servicios


@router.post("/", status_code=201)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo servicio"""
    nuevo_servicio = Servicio(**servicio.dict())
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio


@router.put("/{servicio_id}")
def actualizar_servicio(servicio_id: int, servicio: ServicioUpdate, db: Session = Depends(get_db)):
    """Actualizar un servicio"""
    db_servicio = db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()
    if not db_servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    datos = servicio.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_servicio, key, value)
    
    db.commit()
    db.refresh(db_servicio)
    return db_servicio


@router.delete("/{servicio_id}", status_code=204)
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    """Eliminar un servicio"""
    servicio = db.query(Servicio).filter(Servicio.id_servicio == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    
    db.delete(servicio)
    db.commit()
    return None
