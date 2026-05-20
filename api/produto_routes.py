from fastapi import APIRouter, HTTPException
from typing import List

from schemas.produto_schema import ProdutoCreate, ProdutoResponse
from services import produto_service


produtos_router = APIRouter(prefix='/produtos', tags=['Produtos'])


@produtos_router.post('/')
async def criar_produto(produto_schema: ProdutoCreate):
    resultado = produto_service.cadastrar_produto(
        produto_schema.nome,
        produto_schema.preco,
        produto_schema.estoque
    )

    if not resultado['sucesso']:
        raise HTTPException(status_code=400, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@produtos_router.get('/', response_model=List[ProdutoResponse])
async def lista_de_produtos():
    resultado = produto_service.listar_produtos()

    return resultado['dados']


@produtos_router.get('/{idproduto}', response_model=ProdutoResponse)
async def buscar_produto_por_id(idproduto: int):
    resultado = produto_service.buscar_produto(idproduto)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return resultado['dados']


@produtos_router.put('/{idproduto}')
async def atualizar_dados_produto(idproduto: int, produto_schema: ProdutoCreate):
    resultado = produto_service.atualizar_produto(
        idproduto,
        produto_schema.nome,
        produto_schema.preco,
        produto_schema.estoque
    )

    if not resultado['sucesso']:
        raise HTTPException(status_code=400, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }


@produtos_router.delete('/{idproduto}')
async def deletar_produto(idproduto: int):
    resultado = produto_service.remover_produto(idproduto)

    if not resultado['sucesso']:
        raise HTTPException(status_code=404, detail=resultado['mensagem'])

    return {
        'sucesso': resultado['sucesso'],
        'mensagem': resultado['mensagem']
    }
