from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Date, Numeric
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo_electronico = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20))
    contrasena = Column(String(255), nullable=False)
    foto_perfil = Column(String(500))
    pais = Column(String(100))
    ciudad = Column(String(100))
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    rol = Column(String(50), nullable=False, default='usuario')
    estado_cuenta = Column(String(50), default='activo')

    # Relaciones
    mascotas = relationship("Mascota", back_populates="usuario")
    compras = relationship("Compra", back_populates="usuario")
    mensajes_enviados = relationship("Mensaje", foreign_keys="Mensaje.id_remitente", back_populates="remitente")
    mensajes_recibidos = relationship("Mensaje", foreign_keys="Mensaje.id_destinatario", back_populates="destinatario")
    reportes = relationship("Reporte", back_populates="usuario")
    contactos = relationship("Contacto", back_populates="usuario")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Mascota(Base):
    __tablename__ = 'Mascota'
    id_mascota = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    nombre = Column(String(100), nullable=False)
    raza = Column(String(100))
    edad = Column(Integer)
    tipo = Column(String(50))
    lipo = Column(String(50))  # Tipo de lipo/pelaje
    alergias = Column(Text)
    estado = Column(String(50), default='activo')

    # Relaciones
    usuario = relationship("Usuario", back_populates="mascotas")
    historial_medico = relationship("HistorialMedico", back_populates="mascota")
    carnet_vacunacion = relationship("CarnetVacunacion", back_populates="mascota")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class HistorialMedico(Base):
    __tablename__ = 'HistorialMedico'
    id_historial = Column(Integer, primary_key=True)
    id_mascota = Column(Integer, ForeignKey('Mascota.id_mascota'), nullable=False)
    fecha_consulta = Column(Date, nullable=False)
    diagnostico = Column(Text)
    tratamiento = Column(Text)
    medicamentos_receta = Column(Text)
    veterinario_responsable = Column(String(200))

    # Relación
    mascota = relationship("Mascota", back_populates="historial_medico")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CarnetVacunacion(Base):
    __tablename__ = 'CarnetVacunacion'
    id_carnet = Column(Integer, primary_key=True)
    id_mascota = Column(Integer, ForeignKey('Mascota.id_mascota'), nullable=False)
    nombre_vacuna = Column(String(200), nullable=False)
    fecha_aplicacion = Column(Date, nullable=False)
    proxima_dosis = Column(Date)

    # Relación
    mascota = relationship("Mascota", back_populates="carnet_vacunacion")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Servicio(Base):
    __tablename__ = 'Servicio'
    id_servicio = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    categoria = Column(String(100))
    ubicacion = Column(String(500))
    telefono_contacto = Column(String(20))
    horario_atencion = Column(String(200))
    calificacion_promedio = Column(Numeric(3, 2), default=0.0)

    # Relaciones
    productos = relationship("Producto", back_populates="servicio")
    contactos = relationship("Contacto", back_populates="servicio")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Producto(Base):
    __tablename__ = 'Producto'
    id_producto = Column(Integer, primary_key=True)
    id_servicio = Column(Integer, ForeignKey('Servicio.id_servicio'), nullable=False)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric(10, 2), nullable=False)
    categoria = Column(String(100))
    stock = Column(Integer, default=0)
    foto = Column(String(500))

    # Relación
    servicio = relationship("Servicio", back_populates="productos")
    compras = relationship("Compra", back_populates="producto")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Compra(Base):
    __tablename__ = 'Compra'
    id_compra = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    id_producto = Column(Integer, ForeignKey('Producto.id_producto'), nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    fecha_compra = Column(DateTime, default=datetime.utcnow)
    total = Column(Numeric(10, 2), nullable=False)
    estado = Column(String(50), default='pendiente')

    # Relaciones
    usuario = relationship("Usuario", back_populates="compras")
    producto = relationship("Producto", back_populates="compras")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Mensaje(Base):
    __tablename__ = 'Mensaje'
    id_mensaje = Column(Integer, primary_key=True)
    id_remitente = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    id_destinatario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_envio = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(50), default='no_leido')

    # Relaciones
    remitente = relationship("Usuario", foreign_keys=[id_remitente], back_populates="mensajes_enviados")
    destinatario = relationship("Usuario", foreign_keys=[id_destinatario], back_populates="mensajes_recibidos")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Contacto(Base):
    __tablename__ = 'Contacto'
    id_contacto = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    id_servicio = Column(Integer, ForeignKey('Servicio.id_servicio'), nullable=False)
    fecha_contacto = Column(DateTime, default=datetime.utcnow)
    asunto = Column(String(500))
    mensaje = Column(Text)

    # Relaciones
    usuario = relationship("Usuario", back_populates="contactos")
    servicio = relationship("Servicio", back_populates="contactos")
    reportes = relationship("Reporte", back_populates="contacto")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Reporte(Base):
    __tablename__ = 'Reporte'
    id_reporte = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('Usuario.id_usuario'), nullable=False)
    id_contacto = Column(Integer, ForeignKey('Contacto.id_contacto'))
    tipo = Column(String(100), nullable=False)
    contenido = Column(Text, nullable=False)
    motivo = Column(String(500))
    fecha_reporte = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(50), default='abierto')

    # Relaciones
    usuario = relationship("Usuario", back_populates="reportes")
    contacto = relationship("Contacto", back_populates="reportes")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
