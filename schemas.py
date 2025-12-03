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


class ClienteBase(BaseModel):
    nombre: str
    telefono: str


class ClienteCreate(ClienteBase):
    """Datos que recibimos al crear un cliente"""
    pass


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        orm_mode = True


class ProductoBase(BaseModel):
    nombre: str
    tipo: str | None = None
    precio_base: float


class ProductoCreate(ProductoBase):
    pass


class ProductoResponse(ProductoBase):
    id: int

    class Config:
        orm_mode = True


class PedidoBase(BaseModel):
    cliente_id: int | None = None
    producto_id: int | None = None
    cliente: str
    telefono: str
    producto: str
    sabor: str
    tamano: str
    precio: float
    fecha_entrega: date
    estado: EstadoPedido | None = None


class PedidoCreate(PedidoBase):
    pass


class PedidoResponse(PedidoBase):
    id: int

    class Config:
        orm_mode = True
