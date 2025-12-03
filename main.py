from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import Base, engine
from config import get_settings
from routers import pedidos, clientes, productos # nuestro router de pedidos


# Leer configuración desde .env
settings = get_settings()

# Crear la aplicación FastAPI usando datos del .env
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# Servir archivos estáticos (JS, CSS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Crear las tablas en la base de datos (solo para desarrollo)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {
        "message": "API Pastelería funcionando",
        "env": settings.app_env
    }

@app.get("/app")
def get_frontend():
    return FileResponse("frontend/index.html")


# Incluir los endpoints de pedidos
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(productos.router, prefix="/productos", tags=["Productos"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
