from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base

class Pedido(Base):

    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor_total = Column(Float, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'))

    status = Column(String(20), nullable=False, default='PENDENTE')