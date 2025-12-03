# routers/pedidos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date

from database import get_db
from models import Pedido, EstadoPedido
from schemas import PedidoCreate, PedidoResponse
from typing import List

router = APIRouter()

# ------------------ CREAR PEDIDO ------------------

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def crear_pedido(pedido_in: PedidoCreate, db: Session = Depends(get_db)):

    nuevo_pedido = Pedido(
        cliente_id=pedido_in.cliente_id,
        producto_id=pedido_in.producto_id,
        cliente=pedido_in.cliente,
        telefono=pedido_in.telefono,
        producto=pedido_in.producto,
        sabor=pedido_in.sabor,
        tamano=pedido_in.tamano,
        precio=pedido_in.precio,
        fecha_entrega=pedido_in.fecha_entrega,
        estado=pedido_in.estado or EstadoPedido.pendiente,
    )

    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    return nuevo_pedido


# ------------------ LISTAR TODOS LOS PEDIDOS ------------------

@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).order_by(Pedido.fecha_entrega.desc()).all()


# ------------------ FILTRAR POR ESTADO ------------------

@router.get("/estado/{estado}", response_model=List[PedidoResponse])
def pedidos_por_estado(estado: EstadoPedido, db: Session = Depends(get_db)):
    return db.query(Pedido).filter(Pedido.estado == estado).all()


# ------------------ FILTRAR POR FECHA ------------------

@router.get("/fecha/{fecha}", response_model=List[PedidoResponse])
def pedidos_por_fecha(fecha: date, db: Session = Depends(get_db)):
    return db.query(Pedido).filter(Pedido.fecha_entrega == fecha).all()


# ------------------ CAMBIAR ESTADO ------------------

@router.put("/{pedido_id}/estado", response_model=PedidoResponse)
def cambiar_estado(pedido_id: int, nuevo_estado: EstadoPedido, db: Session = Depends(get_db)):

    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    pedido.estado = nuevo_estado
    db.commit()
    db.refresh(pedido)

    return pedido
