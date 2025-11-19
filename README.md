# Pata Amiga - Backend API

Backend FastAPI para la plataforma **Pata Amiga**, conectado a base de datos SQLite con soporte para usuarios, mascotas, servicios, productos y más.

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- Virtualenv (incluido)

### Instalación y Arranque

1. **Instalar dependencias** (si aún no lo has hecho):
   ```bash
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

2. **Arrancar el servidor de desarrollo**:
   ```bash
   .venv\Scripts\python.exe run.py
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
│   ├── __init__.py              # Paquete (vacío para evitar conflictos)
│   ├── main.py                  # App FastAPI
│   ├── database.py              # Config SQLAlchemy, engine y sesión
│   ├── models_sql.py            # Modelos SQLAlchemy (tablas)
│   ├── fast_routes.py           # Rutas/endpoints FastAPI
│   └── ...                       # Otros módulos legados
├── database/
│   └── pata_amiga.db            # Archivo SQLite
├── run.py                        # Script para arrancar con uvicorn
├── requirements.txt              # Dependencias Python
└── README.md                     # Este archivo
```

---

## 🔌 Endpoints Disponibles

Todos los endpoints están bajo `/api`.

### **Usuarios** (`/api/Usuario`)
- `GET /api/Usuario` — Listar todos los usuarios
- `GET /api/Usuario/{id}` — Obtener usuario por ID
- `POST /api/Usuario` — Crear nuevo usuario
- `PUT /api/Usuario/{id}` — Actualizar usuario
- `DELETE /api/Usuario/{id}` — Eliminar usuario

### **Mascotas** (`/api/Mascota`)
- `GET /api/Mascota` — Listar mascotas
- `GET /api/Mascota/{id}` — Obtener mascota por ID
- `POST /api/Mascota` — Crear mascota
- `PUT /api/Mascota/{id}` — Actualizar mascota
- `DELETE /api/Mascota/{id}` — Eliminar mascota

### **Users (Legacy)** (`/api/users`)
- `GET /api/users` — Listar usuarios
- `GET /api/users/{id}` — Obtener usuario
- `POST /api/users` — Crear usuario
- `PUT /api/users/{id}` — Actualizar usuario
- `DELETE /api/users/{id}` — Eliminar usuario

### **Pets (Legacy)** (`/api/pets`)
- `GET /api/pets` — Listar mascotas
- `GET /api/pets/{id}` — Obtener mascota
- `POST /api/pets` — Crear mascota
- `PUT /api/pets/{id}` — Actualizar mascota
- `DELETE /api/pets/{id}` — Eliminar mascota

### **Salud**
- `GET /api/health` — Verificar estado del servidor
- `GET /` — Raíz (devuelve status)

---

## 📚 Ejemplos de Uso

### Crear un Usuario
```bash
curl -X POST "http://127.0.0.1:8000/api/Usuario" \
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

### Listar Usuarios
```bash
curl -X GET "http://127.0.0.1:8000/api/Usuario"
```

### Obtener Usuario por ID
```bash
curl -X GET "http://127.0.0.1:8000/api/Usuario/1"
```

### Actualizar Usuario
```bash
curl -X PUT "http://127.0.0.1:8000/api/Usuario/1" \
  -H "Content-Type: application/json" \
  -d '{"ciudad": "Medellín"}'
```

### Eliminar Usuario
```bash
curl -X DELETE "http://127.0.0.1:8000/api/Usuario/1"
```

---

## 🗄️ Base de Datos

La aplicación utiliza **SQLite** con la base de datos `database/pata_amiga.db`.

### Tablas Disponibles
- `Usuario` — Información de usuarios
- `Mascota` — Registro de mascotas
- `HistorialMedico` — Historial médico de mascotas
- `CarnetVacunacion` — Carnets de vacunación
- `Servicio` — Servicios veterinarios
- `Producto` — Productos/artículos
- `Compra` — Registro de compras
- `Contacto` — Tabla de contactos
- `Mensaje` — Sistema de mensajería
- `Reporte` — Reportes de usuarios
- `users` (legacy) — Tabla de usuarios simple
- `pets` (legacy) — Tabla de mascotas simple

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

---

## 🔐 Notas de Seguridad

⚠️ **IMPORTANTE**: Este servidor es de desarrollo (`debug=True`). Para producción:
1. Implementar autenticación/JWT
2. Añadir validación de entrada (Pydantic schemas)
3. Hash de contraseñas (bcrypt)
4. HTTPS/SSL
5. Limpieza de variables de entorno

---

## 📞 Soporte

Para preguntas o problemas, verifica:
- La documentación de [FastAPI](https://fastapi.tiangolo.com/)
- La documentación de [SQLAlchemy](https://docs.sqlalchemy.org/)
- El estado del servidor en `http://127.0.0.1:8000/api/health`

---

**Última actualización**: Noviembre 2025