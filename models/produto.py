from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database.connection import Base

class Produto(Base):

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    
    itens_pedido = relationship('ItemPedido', back_populates='produto')