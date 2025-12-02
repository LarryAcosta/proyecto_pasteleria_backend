from fastapi import FastAPI

from database import engine
import models

from routers import pedidos


# Crear las tablas en la base de datos al iniciar la app
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Pastelería",
    description="Backend para gestión de pedidos de pastelería",
    version="1.0.0",
)

app.include_router(pedidos.router)



@app.get("/")
def inicio():
    return {"mensaje": "API de Pastelería funcionando correctamente"}


