from fastapi import APIRouter, HTTPException
from typing import List

from schemas.pedido_schema import PedidoCreate, PedidoResponse, ItemPedidoCreate
from services import pedido_service


pedidos_router = APIRouter(prefix='/pedidos', tags=['Pedidos'])


@pedidos_router.post('/')
async def criar_pedido(pedido_schema: PedidoCreate):
    resultado = pedido_service.criar_pedido(pedido_schema.id_cliente)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@pedidos_router.get('/', response_model=List[PedidoResponse])
async def lista_de_pedidos():
    resultado = pedido_service.listar_pedidos()

    return resultado['dados']


@pedidos_router.get('/{idpedido}', response_model=PedidoResponse)
async def buscar_pedido_por_id(idpedido: int):
    resultado = pedido_service.buscar_pedido(idpedido)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return resultado['dados']


@pedidos_router.post('/{idpedido}/itens')
async def adicionar_itens_ao_pedido(idpedido: int, item_pedido_schema: ItemPedidoCreate):
    resultado = pedido_service.adicionar_item_ao_pedido(
        idpedido,
        item_pedido_schema.id_produto,
        item_pedido_schema.quantidade
    )

    if not resultado['sucesso']:
        raise HTTPException(status_code=400, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@pedidos_router.put('/{idpedido}/finalizar')
async def finalizar_pedido_id(idpedido: int):
    resultado = pedido_service.finalizar_pedido(idpedido)

    if not resultado['sucesso']:
        raise HTTPException(status_code=400, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@pedidos_router.put('/{idpedido}/cancelar')
async def cancelar_pedido_id(idpedido: int):
    resultado = pedido_service.cancelar_pedido(idpedido)

    if not resultado['sucesso']:
        raise HTTPException(status_code=400, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }