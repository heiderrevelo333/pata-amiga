from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import CarnetVacunacion
from pydantic import BaseModel
from typing import Optional
from datetime import date

router = APIRouter(prefix="/carnet-vacunacion", tags=["Carnet de Vacunación"])


class CarnetVacunacionBase(BaseModel):
    id_mascota: int
    nombre_vacuna: str
    fecha_aplicacion: date
    proxima_dosis: Optional[date] = None

    class Config:
        from_attributes = True


class CarnetVacunacionCreate(CarnetVacunacionBase):
    pass


class CarnetVacunacionUpdate(BaseModel):
    nombre_vacuna: Optional[str] = None
    fecha_aplicacion: Optional[date] = None
    proxima_dosis: Optional[date] = None


@router.get("/")
def listar_carnets(db: Session = Depends(get_db)):
    """Listar todos los carnets de vacunación"""
    carnets = db.query(CarnetVacunacion).all()
    return carnets


@router.get("/{carnet_id}")
def obtener_carnet(carnet_id: int, db: Session = Depends(get_db)):
    """Obtener un carnet de vacunación por ID"""
    carnet = db.query(CarnetVacunacion).filter(CarnetVacunacion.id_carnet == carnet_id).first()
    if not carnet:
        raise HTTPException(status_code=404, detail="Carnet de vacunación no encontrado")
    return carnet


@router.get("/mascota/{mascota_id}")
def listar_carnets_por_mascota(mascota_id: int, db: Session = Depends(get_db)):
    """Listar carnets de vacunación de una mascota"""
    carnets = db.query(CarnetVacunacion).filter(CarnetVacunacion.id_mascota == mascota_id).all()
    return carnets


@router.post("/", status_code=201)
def crear_carnet(carnet: CarnetVacunacionCreate, db: Session = Depends(get_db)):
    """Crear un nuevo carnet de vacunación"""
    nuevo_carnet = CarnetVacunacion(**carnet.dict())
    db.add(nuevo_carnet)
    db.commit()
    db.refresh(nuevo_carnet)
    return nuevo_carnet


@router.put("/{carnet_id}")
def actualizar_carnet(carnet_id: int, carnet: CarnetVacunacionUpdate, db: Session = Depends(get_db)):
    """Actualizar un carnet de vacunación"""
    db_carnet = db.query(CarnetVacunacion).filter(CarnetVacunacion.id_carnet == carnet_id).first()
    if not db_carnet:
        raise HTTPException(status_code=404, detail="Carnet de vacunación no encontrado")
    
    datos = carnet.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_carnet, key, value)
    
    db.commit()
    db.refresh(db_carnet)
    return db_carnet


@router.delete("/{carnet_id}", status_code=204)
def eliminar_carnet(carnet_id: int, db: Session = Depends(get_db)):
    """Eliminar un carnet de vacunación"""
    carnet = db.query(CarnetVacunacion).filter(CarnetVacunacion.id_carnet == carnet_id).first()
    if not carnet:
        raise HTTPException(status_code=404, detail="Carnet de vacunación no encontrado")
    
    db.delete(carnet)
    db.commit()
    return None
