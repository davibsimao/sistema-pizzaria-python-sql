from models.produto import Produto
from database.connection import Session


def buscar_produto_por_id(idproduto, session):

    produto = session.query(Produto).filter(Produto.id == idproduto).first()
    return produto


def cadastrar_produto(nome, preco, estoque):

    if not nome:
        return {'sucesso': False, 'mensagem': 'Digite um nome válido.'}
    
    if preco <= 0:
        return {'sucesso': False, 'mensagem': 'Preço inválido.'}
        
    if estoque < 0:
        return {'sucesso': False, 'mensagem': 'Digite um valor de estoque válido.'}

    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.nome == nome).first()

        if produto:
            return {'sucesso': False, 'mensagem': 'Produto já cadastrado.'}

        novo_produto = Produto(
            nome=nome,
            preco=preco,
            estoque=estoque)

        session.add(novo_produto)
        session.commit()
        return {'sucesso': True, 'mensagem': 'Produto cadastrado com sucesso!'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao cadastrar produto: {erro}'}

    finally:
        session.close()


def listar_produtos():

    session = Session()

    try:
        produtos = session.query(Produto).all()

        if not produtos:
            return {'sucesso': False, 'mensagem': 'Nenhum produto cadastrado.', 'dados': []}

        return {'sucesso': True, 'mensagem': 'Produtos encontrados', 'dados': produtos}

    except Exception as erro:
        return {'sucesso': False, 'mensagem': f'Erro ao listar produtos: {erro}', 'dados': []}

    finally:
        session.close()


def atualizar_produto(idproduto, novo_nome, novo_preco, novo_estoque):

    if not novo_nome:
        return {'sucesso': False, 'mensagem': 'Digite um nome válido.'}
    
    if novo_preco <= 0:
        return {'sucesso': False, 'mensagem': 'Digite um preço válido.'}

    if novo_estoque < 0:
        return {'sucesso': False, 'mensagem': 'Digite um valor de estoque válido.'}
    
    session = Session()

    try:
        produto = buscar_produto_por_id(idproduto, session)

        if not produto:
            return {'sucesso': False, 'mensagem': 'Produto não encontrado.'}

        produto.nome = novo_nome
        produto.preco = novo_preco
        produto.estoque = novo_estoque

        session.commit()
        return {'sucesso': True, 'mensagem': 'Produto atualizado com sucesso!'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao atualizar produto: {erro}'}

    finally:
        session.close()


def remover_produto(idproduto):

    session = Session()

    try:
        produto = buscar_produto_por_id(idproduto, session)

        if not produto:
            return {'sucesso': False, 'mensagem': 'Produto não encontrado.'}

        session.delete(produto)
        session.commit()
        return {'sucesso': True, 'mensagem': 'Produto removido com sucesso.'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao deletar produto: {erro}'}

    finally:
        session.close()