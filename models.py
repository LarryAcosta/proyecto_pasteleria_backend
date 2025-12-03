from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum


class EstadoPedido(str, enum.Enum):
    pendiente = "pendiente"
    en_preparacion = "en_preparacion"
    entregado = "entregado"
    cancelado = "cancelado"


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)

    # Relación 1:N con Pedido
    pedidos = relationship("Pedido", back_populates="cliente_rel")


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)          # torta, cupcakes, postre, etc.
    tipo = Column(String, nullable=True)             # cumpleaños, boda, etc. (opcional)
    precio_base = Column(Float, nullable=False)

    # Relación 1:N con Pedido
    pedidos = relationship("Pedido", back_populates="producto_rel")


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=True)

    
    cliente_rel = relationship("Cliente", back_populates="pedidos")
    producto_rel = relationship("Producto", back_populates="pedidos")

    
    cliente = Column(String, index=True, nullable=False)
    telefono = Column(String, nullable=False)
    producto = Column(String, nullable=False)        # torta, cupcakes, postre, etc.
    sabor = Column(String, nullable=False)
    tamano = Column(String, nullable=False)          # 1/2 libra, 1 libra, etc.
    precio = Column(Float, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    estado = Column(
        Enum(EstadoPedido),
        default=EstadoPedido.pendiente,
        nullable=False
    )
