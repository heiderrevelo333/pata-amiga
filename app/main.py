from fastapi import FastAPI
from routes import usuarios, mascotas

app = FastAPI(
    title="Pata Amiga API",
    description="Backend para plataforma de cuidado de mascotas",
    version="1.0.0"
)

# Incluir routers organizados por entidad
app.include_router(usuarios.router, prefix="/api")
app.include_router(mascotas.router, prefix="/api")

# Ruta raíz
@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "pata-amiga",
        "docs": "http://127.0.0.1:8000/docs"
    }


@app.get("/api/health")
def health():
    return {"status": "healthy"}

