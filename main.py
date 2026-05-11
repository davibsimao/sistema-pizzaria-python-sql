from database.connection import Base
from database.connection import db

from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido
from models.item_pedido import ItemPedido

from interface.menu import menu


Base.metadata.create_all(bind=db)

menu()