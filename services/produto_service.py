from models.produto import Produto
from database.connection import Session


def cadastrar_produto(nome, preco, estoque):

    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.nome == nome).first()

        if produto:
            print('Produto já cadastrado')
            return

        if preco <= 0:
            print('Preço inválido')
            return

        novo_produto = Produto(
            nome=nome,
            preco=preco,
            estoque=estoque)

        session.add(novo_produto)
        session.commit()
        print('Produto cadastrado com sucesso!')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao cadastrar produto: {erro}')

    finally:
        session.close()

def listar_produtos():

    session = Session()

    try:
        produtos = session.query(Produto).all()

        if not produtos:
            print('Nenhum produto cadastrado')
            return
        
        else:
            for produto in produtos:
                print(f'Nome: {produto.nome} | Preço: R${produto.preco} |Estoque: {produto.estoque}')

    except Exception as erro:
        print(f'Erro ao listar produto: {erro}')

    finally:
        session.close()


def atualizar_produto(idproduto):

    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.id == idproduto).first()

        if not produto:
            print('Produto não encontrado.')
            return
        
        else:
            novo_nome = str(input('Novo nome: ')).strip()
            novo_preco = float(input('Novo preco: '))
            novo_estoque = int(input('Novo estoque: '))

            produto.nome = novo_nome
            produto.preco = novo_preco
            produto.estoque = novo_estoque

            session.commit()
            print('Produto atualizado com sucesso!')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao cadastrar produto: {erro}')

    finally:
        session.close()

def remover_produto(idproduto):

    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.id==idproduto).first()

        if not produto:
            print('Produto não encontrado.')
            return
        
        else:
            session.delete(produto)
            session.commit()
            print('Produto deletado com sucesso.')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao deletar produto: {erro}')
    
    finally:
        session.close()


