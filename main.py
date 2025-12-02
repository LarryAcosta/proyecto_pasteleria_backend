from fastapi import FastAPI
from database import Base, engine
from config import get_settings
from routers import pedidos  # nuestro router de pedidos

# Leer configuración desde .env
settings = get_settings()

# Crear la aplicación FastAPI usando datos del .env
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# Crear las tablas en la base de datos (solo para desarrollo)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {
        "message": "API Pastelería funcionando",
        "env": settings.app_env
    }


# Incluir los endpoints de pedidos
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
