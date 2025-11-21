from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Reporte
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/reportes", tags=["Reportes"])


class ReporteBase(BaseModel):
    id_usuario: int
    id_contacto: Optional[int] = None
    tipo: str
    contenido: str
    motivo: Optional[str] = None
    estado: Optional[str] = "abierto"

    class Config:
        from_attributes = True


class ReporteCreate(ReporteBase):
    pass


class ReporteUpdate(BaseModel):
    tipo: Optional[str] = None
    contenido: Optional[str] = None
    motivo: Optional[str] = None
    estado: Optional[str] = None


@router.get("/")
def listar_reportes(db: Session = Depends(get_db)):
    """Listar todos los reportes"""
    reportes = db.query(Reporte).all()
    return reportes


@router.get("/{reporte_id}")
def obtener_reporte(reporte_id: int, db: Session = Depends(get_db)):
    """Obtener un reporte por ID"""
    reporte = db.query(Reporte).filter(Reporte.id_reporte == reporte_id).first()
    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return reporte


@router.get("/usuario/{usuario_id}")
def listar_reportes_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Listar reportes de un usuario"""
    reportes = db.query(Reporte).filter(Reporte.id_usuario == usuario_id).all()
    return reportes


@router.get("/estado/{estado}")
def listar_reportes_por_estado(estado: str, db: Session = Depends(get_db)):
    """Listar reportes por estado"""
    reportes = db.query(Reporte).filter(Reporte.estado == estado).all()
    return reportes


@router.post("/", status_code=201)
def crear_reporte(reporte: ReporteCreate, db: Session = Depends(get_db)):
    """Crear un nuevo reporte"""
    nuevo_reporte = Reporte(**reporte.dict())
    db.add(nuevo_reporte)
    db.commit()
    db.refresh(nuevo_reporte)
    return nuevo_reporte


@router.put("/{reporte_id}")
def actualizar_reporte(reporte_id: int, reporte: ReporteUpdate, db: Session = Depends(get_db)):
    """Actualizar un reporte"""
    db_reporte = db.query(Reporte).filter(Reporte.id_reporte == reporte_id).first()
    if not db_reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    
    datos = reporte.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_reporte, key, value)
    
    db.commit()
    db.refresh(db_reporte)
    return db_reporte


@router.delete("/{reporte_id}", status_code=204)
def eliminar_reporte(reporte_id: int, db: Session = Depends(get_db)):
    """Eliminar un reporte"""
    reporte = db.query(Reporte).filter(Reporte.id_reporte == reporte_id).first()
    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    
    db.delete(reporte)
    db.commit()
    return None
