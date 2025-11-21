# Pata Amiga - Backend API

Backend FastAPI para la plataforma **Pata Amiga**, completamente implementado según el diagrama entidad-relación con soporte para usuarios, mascotas, servicios, productos, historial médico, vacunaciones, compras, mensajes, contactos y reportes.

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- Virtualenv (incluido)

### Instalación y Arranque

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Arrancar el servidor de desarrollo**:
   ```bash
   python run.py
   ```
   
   El servidor estará disponible en `http://127.0.0.1:8000`

3. **Documentación interactiva** (Swagger UI):
   - Abre en tu navegador: `http://127.0.0.1:8000/docs`
   - Allí puedes probar todos los endpoints de forma interactiva

---

## 📋 Estructura del Proyecto

```
pata-amiga/
├── app/
│   ├── __init__.py              # Paquete principal
│   ├── main.py                  # App FastAPI
│   ├── database.py              # Config SQLAlchemy
│   ├── models_sql.py            # Modelos SQLAlchemy (todas las tablas)
│   └── security.py              # Utilidades de seguridad
├── routes/
│   ├── __init__.py
│   ├── usuarios.py              # Endpoints de usuarios
│   ├── mascotas.py              # Endpoints de mascotas
│   ├── servicios.py             # Endpoints de servicios
│   ├── productos.py             # Endpoints de productos
│   ├── historial_medico.py      # Endpoints de historial médico
│   ├── carnet_vacunacion.py     # Endpoints de vacunación
│   ├── compras.py               # Endpoints de compras
│   ├── mensajes.py              # Endpoints de mensajes
│   ├── contactos.py             # Endpoints de contactos
│   └── reportes.py              # Endpoints de reportes
├── database/
│   └── pata_amiga.db            # Archivo SQLite
├── run.py                        # Script para arrancar
├── requirements.txt              # Dependencias Python
└── README.md                     # Este archivo
```

---

## 🔌 Endpoints Disponibles

### **Usuarios** (`/api/usuarios`)
- `GET /api/usuarios` — Listar todos
- `GET /api/usuarios/{usuario_id}` — Obtener por ID
- `POST /api/usuarios` — Crear nuevo
- `PUT /api/usuarios/{usuario_id}` — Actualizar
- `DELETE /api/usuarios/{usuario_id}` — Eliminar

### **Mascotas** (`/api/mascotas`)
- `GET /api/mascotas` — Listar todas
- `GET /api/mascotas/{mascota_id}` — Obtener por ID
- `GET /api/mascotas/usuario/{usuario_id}` — Listar por usuario
- `POST /api/mascotas` — Crear nueva
- `PUT /api/mascotas/{mascota_id}` — Actualizar
- `DELETE /api/mascotas/{mascota_id}` — Eliminar

### **Historial Médico** (`/api/historial-medico`)
- `GET /api/historial-medico` — Listar todos
- `GET /api/historial-medico/{historial_id}` — Obtener por ID
- `GET /api/historial-medico/mascota/{mascota_id}` — Listar por mascota
- `POST /api/historial-medico` — Crear registro
- `PUT /api/historial-medico/{historial_id}` — Actualizar
- `DELETE /api/historial-medico/{historial_id}` — Eliminar

### **Carnet de Vacunación** (`/api/carnet-vacunacion`)
- `GET /api/carnet-vacunacion` — Listar todos
- `GET /api/carnet-vacunacion/{carnet_id}` — Obtener por ID
- `GET /api/carnet-vacunacion/mascota/{mascota_id}` — Listar por mascota
- `POST /api/carnet-vacunacion` — Crear carnet
- `PUT /api/carnet-vacunacion/{carnet_id}` — Actualizar
- `DELETE /api/carnet-vacunacion/{carnet_id}` — Eliminar

### **Servicios** (`/api/servicios`)
- `GET /api/servicios` — Listar todos
- `GET /api/servicios/{servicio_id}` — Obtener por ID
- `GET /api/servicios/categoria/{categoria}` — Listar por categoría
- `POST /api/servicios` — Crear servicio
- `PUT /api/servicios/{servicio_id}` — Actualizar
- `DELETE /api/servicios/{servicio_id}` — Eliminar

### **Productos** (`/api/productos`)
- `GET /api/productos` — Listar todos
- `GET /api/productos/{producto_id}` — Obtener por ID
- `GET /api/productos/servicio/{servicio_id}` — Listar por servicio
- `POST /api/productos` — Crear producto
- `PUT /api/productos/{producto_id}` — Actualizar
- `DELETE /api/productos/{producto_id}` — Eliminar

### **Compras** (`/api/compras`)
- `GET /api/compras` — Listar todas
- `GET /api/compras/{compra_id}` — Obtener por ID
- `GET /api/compras/usuario/{usuario_id}` — Listar por usuario
- `POST /api/compras` — Crear compra
- `PUT /api/compras/{compra_id}` — Actualizar
- `DELETE /api/compras/{compra_id}` — Eliminar

### **Mensajes** (`/api/mensajes`)
- `GET /api/mensajes` — Listar todos
- `GET /api/mensajes/{mensaje_id}` — Obtener por ID
- `GET /api/mensajes/usuario/{usuario_id}/enviados` — Mensajes enviados
- `GET /api/mensajes/usuario/{usuario_id}/recibidos` — Mensajes recibidos
- `GET /api/mensajes/usuario/{usuario_id}/no-leidos` — No leídos
- `POST /api/mensajes` — Crear mensaje
- `PUT /api/mensajes/{mensaje_id}` — Actualizar
- `DELETE /api/mensajes/{mensaje_id}` — Eliminar

### **Contactos** (`/api/contactos`)
- `GET /api/contactos` — Listar todos
- `GET /api/contactos/{contacto_id}` — Obtener por ID
- `GET /api/contactos/usuario/{usuario_id}` — Listar por usuario
- `GET /api/contactos/servicio/{servicio_id}` — Listar por servicio
- `POST /api/contactos` — Crear contacto
- `PUT /api/contactos/{contacto_id}` — Actualizar
- `DELETE /api/contactos/{contacto_id}` — Eliminar

### **Reportes** (`/api/reportes`)
- `GET /api/reportes` — Listar todos
- `GET /api/reportes/{reporte_id}` — Obtener por ID
- `GET /api/reportes/usuario/{usuario_id}` — Listar por usuario
- `GET /api/reportes/estado/{estado}` — Listar por estado
- `POST /api/reportes` — Crear reporte
- `PUT /api/reportes/{reporte_id}` — Actualizar
- `DELETE /api/reportes/{reporte_id}` — Eliminar

### **Salud**
- `GET /api/health` — Verificar estado del servidor
- `GET /` — Raíz (devuelve status)

---

## 📚 Ejemplos de Uso

### Crear un Usuario
```bash
curl -X POST "http://127.0.0.1:8000/api/usuarios" \
  -H "Content-Type: application/json" \
  -d '{
    "nombres": "Juan",
    "apellidos": "Pérez",
    "correo_electronico": "juan@example.com",
    "telefono": "1234567890",
    "contrasena": "pass123",
    "rol": "usuario",
    "pais": "Colombia",
    "ciudad": "Bogotá"
  }'
```

### Crear una Mascota
```bash
curl -X POST "http://127.0.0.1:8000/api/mascotas" \
  -H "Content-Type: application/json" \
  -d '{
    "id_usuario": 1,
    "nombre": "Luna",
    "raza": "Labrador",
    "edad": 3,
    "tipo": "perro",
    "lipo": "pelo largo",
    "alergias": "ninguna",
    "estado": "activo"
  }'
```

### Crear Historial Médico
```bash
curl -X POST "http://127.0.0.1:8000/api/historial-medico" \
  -H "Content-Type: application/json" \
  -d '{
    "id_mascota": 1,
    "fecha_consulta": "2025-11-20",
    "diagnostico": "Chequeo general",
    "tratamiento": "Vitaminas",
    "medicamentos_receta": "Vitaminas A y D",
    "veterinario_responsable": "Dr. García"
  }'
```

### Crear Carnet de Vacunación
```bash
curl -X POST "http://127.0.0.1:8000/api/carnet-vacunacion" \
  -H "Content-Type: application/json" \
  -d '{
    "id_mascota": 1,
    "nombre_vacuna": "Parvovirus",
    "fecha_aplicacion": "2025-11-20",
    "proxima_dosis": "2026-11-20"
  }'
```

### Listar Mascotas de un Usuario
```bash
curl -X GET "http://127.0.0.1:8000/api/mascotas/usuario/1"
```

---

## 🗄️ Base de Datos

La aplicación utiliza **SQLite** con la base de datos `database/pata_amiga.db`.

### Tablas Implementadas
- **Usuario** — Información de usuarios (nombres, correo, teléfono, etc.)
- **Mascota** — Registro de mascotas (nombre, raza, edad, tipo, alergias)
- **HistorialMedico** — Historial médico de mascotas (consultas, diagnósticos, tratamientos)
- **CarnetVacunacion** — Carnets de vacunación (vacunas aplicadas, próximas dosis)
- **Servicio** — Servicios veterinarios (nombre, categoría, ubicación, teléfono)
- **Producto** — Productos/artículos (nombre, precio, stock, categoría)
- **Compra** — Registro de compras (usuario, producto, cantidad, total, estado)
- **Mensaje** — Sistema de mensajería (remitente, destinatario, contenido, estado)
- **Contacto** — Contactos entre usuarios y servicios
- **Reporte** — Reportes de usuarios (tipo, contenido, estado)

---

## 🔄 Relaciones Entre Tablas

```
Usuario
├── 1:N Mascota (usuario - mascota)
├── 1:N Compra (usuario - compra)
├── 1:N Mensaje (remitente, destinatario)
├── 1:N Contacto (usuario - contacto)
└── 1:N Reporte (usuario - reporte)

Mascota
├── 1:N HistorialMedico
└── 1:N CarnetVacunacion

Servicio
├── 1:N Producto
└── 1:N Contacto

Producto
└── 1:N Compra

Contacto
└── 1:N Reporte
```

---

## ⚙️ Configuración

### Base de Datos
Por defecto, la app se conecta a SQLite en `database/pata_amiga.db`.

Para cambiar a PostgreSQL o MySQL, edita `app/database.py`:
```python
# PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost/pata_amiga"

# MySQL
DATABASE_URL = "mysql+pymysql://user:password@localhost/pata_amiga"
```

---

## 🛠️ Desarrollo

### Recargar en Caliente (Hot Reload)
El servidor está configurado con `reload=True` en `run.py`, por lo que cualquier cambio en el código se refleja automáticamente.

### Parar el Servidor
En la terminal donde corre uvicorn, presiona `Ctrl+C`.

---

## 📦 Dependencias

- **FastAPI** — Framework web moderno y rápido
- **Uvicorn** — Servidor ASGI
- **SQLAlchemy** — ORM y herramienta de mapeo relacional
- **Pydantic** — Validación de datos
- **python-dotenv** — Manejo de variables de entorno
- **passlib & bcrypt** — Hash seguro de contraseñas
- **PyJWT** — Tokens JWT para autenticación

---

## 🔐 Notas de Seguridad

⚠️ **IMPORTANTE**: Este servidor es de desarrollo. Para producción:
1. Implementar autenticación JWT completa
2. Usar validación de entrada (Pydantic schemas) ✓
3. Hash de contraseñas con bcrypt ✓
4. Habilitar HTTPS/SSL
5. Variables de entorno para secretos
6. Rate limiting
7. CORS apropiado

---

## 📞 Soporte

Para preguntas o problemas, verifica:
- La documentación de [FastAPI](https://fastapi.tiangolo.com/)
- La documentación de [SQLAlchemy](https://docs.sqlalchemy.org/)
- El estado del servidor en `http://127.0.0.1:8000/api/health`

---

**Última actualización**: Noviembre 2025
