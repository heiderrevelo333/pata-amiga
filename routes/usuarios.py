from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_sql import Usuario
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str
    correo_electronico: str
    telefono: Optional[str] = None
    contrasena: str
    foto_perfil: Optional[str] = None
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    rol: str
    estado_cuenta: Optional[str] = "activo"

    class Config:
        from_attributes = True


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    telefono: Optional[str] = None
    foto_perfil: Optional[str] = None
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    estado_cuenta: Optional[str] = None


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    """Listar todos los usuarios"""
    usuarios = db.query(Usuario).all()
    return usuarios


@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Obtener un usuario por ID"""
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", status_code=201)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    # Validar que el correo no exista
    existe = db.query(Usuario).filter(Usuario.correo_electronico == usuario.correo_electronico).first()
    if existe:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    """Actualizar un usuario"""
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    datos = usuario.dict(exclude_unset=True)
    for key, value in datos.items():
        setattr(db_usuario, key, value)
    
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@router.delete("/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario"""
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    return None
