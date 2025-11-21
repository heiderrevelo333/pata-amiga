import uvicorn
from app.database import init_db

if __name__ == '__main__':
    # Crear todas las tablas
    init_db()
    
    # run FastAPI app (app.main:app)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
