# routers/clientes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Cliente
from schemas import ClienteCreate, ClienteResponse
from typing import List

router = APIRouter()


@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente_in: ClienteCreate, db: Session = Depends(get_db)):
    # Crear instancia del modelo
    nuevo_cliente = Cliente(
        nombre=cliente_in.nombre,
        telefono=cliente_in.telefono
    )

    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)

    return nuevo_cliente


@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes
