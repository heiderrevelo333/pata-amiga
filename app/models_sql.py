from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from .database import Base


class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    correo_electronico = Column(String, unique=True, nullable=False)
    telefono = Column(String)
    contrasena = Column(String, nullable=False)
    foto_perfil = Column(String)
    pais = Column(String)
    ciudad = Column(String)
    fecha_registro = Column(String)
    rol = Column(String, nullable=False)
    estado_cuenta = Column(String, default='activo')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Mascota(Base):
    __tablename__ = 'Mascota'
    id_mascota = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    nombre = Column(String, nullable=False)
    raza = Column(String)
    edad = Column(Integer)
    tipo = Column(String)
    historial_medico = Column(String)
    alergias = Column(String)
    estado = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String)
    phone = Column(String)
    created_at = Column(DateTime)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Pets(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String)
    created_at = Column(DateTime)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
