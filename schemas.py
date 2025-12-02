# schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional
from models import EstadoPedido


class PedidoBase(BaseModel):
    cliente: str
    telefono: str
    producto: str
    sabor: str
    tamano: Optional[str] = None
    precio: float
    fecha_entrega: date
    estado: EstadoPedido = EstadoPedido.pendiente


class PedidoCreate(PedidoBase):
    """
    Esquema para crear un pedido (POST).
    De momento es igual al base.
    """
    pass


class PedidoUpdate(BaseModel):
    """
    Esquema para actualizar un pedido (PUT/PATCH).
    Todos los campos son opcionales.
    """
    cliente: Optional[str] = None
    telefono: Optional[str] = None
    producto: Optional[str] = None
    sabor: Optional[str] = None
    tamano: Optional[str] = None
    precio: Optional[float] = None
    fecha_entrega: Optional[date] = None
    estado: Optional[EstadoPedido] = None


class PedidoOut(PedidoBase):
    """
    Esquema para responder al cliente (lo que devuelve la API).
    Incluye el id.
    """
    id: int

    class Config:
        orm_mode = True
