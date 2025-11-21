# Routes package for FastAPI
from . import usuarios
from . import mascotas
from . import servicios
from . import productos
from . import historial_medico
from . import carnet_vacunacion
from . import compras
from . import mensajes
from . import contactos
from . import reportes

__all__ = [
    'usuarios',
    'mascotas',
    'servicios',
    'productos',
    'historial_medico',
    'carnet_vacunacion',
    'compras',
    'mensajes',
    'contactos',
    'reportes'
]
