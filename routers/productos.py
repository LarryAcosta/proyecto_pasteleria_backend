# routers/productos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Producto
from schemas import ProductoCreate, ProductoResponse
from typing import List

router = APIRouter()


@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto_in: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = Producto(
        nombre=producto_in.nombre,
        tipo=producto_in.tipo,
        precio_base=producto_in.precio_base
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


@router.get("/", response_model=List[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()
