from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class ItemPedido(Base):

    __tablename__ = 'itens_pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    preco_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    id_pedido = Column(Integer, ForeignKey('pedidos.id'))
    id_produto = Column(Integer, ForeignKey('produtos.id'))


    produto = relationship('Produto', back_populates='itens_pedido')
    pedido = relationship('Pedido', back_populates='itens')
