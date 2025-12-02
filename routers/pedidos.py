# routers/pedidos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date


import schemas
import crud
from database import get_db
from models import EstadoPedido


router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.post("/", response_model=schemas.PedidoOut, status_code=status.HTTP_201_CREATED)
def crear_pedido(pedido_in: schemas.PedidoCreate, db: Session = Depends(get_db)):
    pedido = crud.crear_pedido(db, pedido_in)
    return pedido


@router.get("/", response_model=List[schemas.PedidoOut])
def listar_pedidos(
    orden: str = "asc",
    db: Session = Depends(get_db)
):
    if orden not in ("asc", "desc"):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=400,
            detail="El parámetro 'orden' debe ser 'asc' o 'desc'."
        )

    return crud.obtener_pedidos_ordenados(db, orden)


@router.get("/fecha/{fecha_entrega}", response_model=List[schemas.PedidoOut])
def listar_pedidos_por_fecha(
    fecha_entrega: date,
    db: Session = Depends(get_db)
):
    pedidos = crud.obtener_pedidos_por_fecha(db, fecha_entrega)
    return pedidos

@router.get("/estado/{estado}", response_model=List[schemas.PedidoOut])
def listar_pedidos_por_estado(
    estado: EstadoPedido,
    db: Session = Depends(get_db)
):
    pedidos = crud.obtener_pedidos_por_estado(db, estado)
    return pedidos


@router.get("/{pedido_id}", response_model=schemas.PedidoOut)
def obtener_un_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = crud.obtener_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.put("/{pedido_id}", response_model=schemas.PedidoOut)
def actualizar_pedido(
    pedido_id: int,
    pedido_in: schemas.PedidoUpdate,
    db: Session = Depends(get_db)
):
    pedido = crud.actualizar_pedido(db, pedido_id, pedido_in)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.delete("/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    eliminado = crud.eliminar_pedido(db, pedido_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return
