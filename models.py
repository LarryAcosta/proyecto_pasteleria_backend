# models.py
from sqlalchemy import Column, Integer, String, Float, Date, Enum
from database import Base
import enum


class EstadoPedido(str, enum.Enum):
    pendiente = "pendiente"
    en_preparacion = "en_preparacion"
    entregado = "entregado"
    cancelado = "cancelado"


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, index=True, nullable=False)
    telefono = Column(String, nullable=False)
    producto = Column(String, nullable=False)   # torta, cupcakes, postre, etc.
    sabor = Column(String, nullable=False)
    tamano = Column(String, nullable=True)      # 1/2 libra, 1 libra, etc.
    precio = Column(Float, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    estado = Column(
        Enum(EstadoPedido),
        default=EstadoPedido.pendiente,
        nullable=False
    )
