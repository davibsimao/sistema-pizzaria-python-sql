from database.connection import Base 
from database.connection import db
from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido
from models.item_pedido import ItemPedido

Base.metadata.create_all(bind=db)

