from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base


class Cliente(Base):

    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(30), unique=True, nullable=False)

    pedidos = relationship('Pedido', back_populates='cliente')