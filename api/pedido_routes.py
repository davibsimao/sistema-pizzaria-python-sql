from fastapi import APIRouter, HTTPException
from typing import List

from schemas.pedido_schema import PedidoCreate, PedidoResponse, ItemPedidoCreate

from services import pedido_service

pedidos_router = APIRouter(prefix='/pedidos', tags=['Pedidos'])

@pedidos_router.post('/')
async def criar_pedido(id_cliente):
    resultado = pedido_service.criar_pedido(id_cliente)

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@pedidos_router.get('/', response_model=List[PedidoResponse])
async def lista_de_pedidos():
    resultado = pedido_service.listar_pedidos()

    return resultado['dados']

@pedidos_router.get('/{idpedido}', response_model= PedidoResponse)
async def buscar_pedido_por_id(idpedido: int):
    resultado = pedido_service.buscar_pedido(idpedido)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return resultado['dados']