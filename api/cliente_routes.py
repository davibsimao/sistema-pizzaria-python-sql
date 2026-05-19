from fastapi import APIRouter, HTTPException
from typing import List

from schemas.cliente_schema import ClienteCreate, ClienteResponse
from services import cliente_service


clientes_router = APIRouter(prefix='/clientes', tags=['Clientes'])


@clientes_router.post('/')
async def criar_cliente(cliente_schema: ClienteCreate):
    resultado = cliente_service.cadastrar_cliente(
        cliente_schema.nome,
        cliente_schema.telefone
    )

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@clientes_router.get('/', response_model=List[ClienteResponse])
async def lista_de_clientes():
    resultado = cliente_service.listar_clientes()

    return resultado['dados']


@clientes_router.get('/{idcliente}', response_model=ClienteResponse)
async def buscar_cliente__por_id(idcliente: int):
    resultado = cliente_service.buscar_cliente(idcliente)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return resultado['dados']


@clientes_router.put('/{idcliente}')
async def atualizar_dados_cliente(idcliente: int, cliente_schema: ClienteCreate):
    resultado = cliente_service.atualizar_cliente(
        idcliente,
        cliente_schema.nome,
        cliente_schema.telefone
    )

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@clientes_router.delete('/{idcliente}')
async def deletar_cliente(idcliente: int):
    resultado = cliente_service.remover_cliente(idcliente)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }