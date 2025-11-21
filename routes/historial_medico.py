from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import HistorialMedico
from pydantic import BaseModel
from typing import Optional
from datetime import date

router = APIRouter(prefix="/historial-medico", tags=["Historial Médico"])


class HistorialMedicoBase(BaseModel):
    id_mascota: int
    fecha_consulta: date
    diagnostico: Optional[str] = None
    tratamiento: Optional[str] = None
    medicamentos_receta: Optional[str] = None
    veterinario_responsable: Optional[str] = None

    class Config:
        from_attributes = True


class HistorialMedicoCreate(HistorialMedicoBase):
    pass


class HistorialMedicoUpdate(BaseModel):
    fecha_consulta: Optional[date] = None
    diagnostico: Optional[str] = None
    tratamiento: Optional[str] = None
    medicamentos_receta: Optional[str] = None
    veterinario_responsable: Optional[str] = None


@router.get("/")
def listar_historial_medico(db: Session = Depends(get_db)):
    """Listar todo el historial médico"""
    registros = db.query(HistorialMedico).all()
    return registros


@router.get("/{historial_id}")
def obtener_historial(historial_id: int, db: Session = Depends(get_db)):
    """Obtener un registro de historial médico por ID"""
    historial = db.query(HistorialMedico).filter(HistorialMedico.id_historial == historial_id).first()
    if not historial:
        raise HTTPException(status_code=404, detail="Historial médico no encontrado")
    return historial


@router.get("/mascota/{mascota_id}")
def listar_historial_por_mascota(mascota_id: int, db: Session = Depends(get_db)):
    """Listar historial médico de una mascota"""
    registros = db.query(HistorialMedico).filter(HistorialMedico.id_mascota == mascota_id).all()
    return registros


@router.post("/", status_code=201)
def crear_historial(historial: HistorialMedicoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo registro de historial médico"""
    nuevo_historial = HistorialMedico(**historial.dict())
    db.add(nuevo_historial)
    db.commit()
    db.refresh(nuevo_historial)
    return nuevo_historial


@router.put("/{historial_id}")
def actualizar_historial(historial_id: int, historial: HistorialMedicoUpdate, db: Session = Depends(get_db)):
    """Actualizar un registro de historial médico"""
    db_historial = db.query(HistorialMedico).filter(HistorialMedico.id_historial == historial_id).first()
    if not db_historial:
        raise HTTPException(status_code=404, detail="Historial médico no encontrado")
    
    datos = historial.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_historial, key, value)
    
    db.commit()
    db.refresh(db_historial)
    return db_historial


@router.delete("/{historial_id}", status_code=204)
def eliminar_historial(historial_id: int, db: Session = Depends(get_db)):
    """Eliminar un registro de historial médico"""
    historial = db.query(HistorialMedico).filter(HistorialMedico.id_historial == historial_id).first()
    if not historial:
        raise HTTPException(status_code=404, detail="Historial médico no encontrado")
    
    db.delete(historial)
    db.commit()
    return None
