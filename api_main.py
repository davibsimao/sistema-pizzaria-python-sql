from fastapi import FastAPI, APIRouter

from database.connection import Base, db

from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido
from models.item_pedido import ItemPedido

Base.metadata.create_all(bind=db)

from api.cliente_routes import clientes_router
from api.produto_routes import produtos_router
from api.pedido_routes import pedidos_router

app = FastAPI()

status_router = APIRouter(prefix="/status", tags=["Status"])


@status_router.get("/")
async def status():
    return {"mensagem": "FUNCIONANDO"}


app.include_router(status_router)
app.include_router(clientes_router)
app.include_router(produtos_router)
app.include_router(pedidos_router)