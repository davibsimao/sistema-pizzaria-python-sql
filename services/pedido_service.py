from models.pedido import Pedido
from models.cliente import Cliente 
from models.item_pedido import ItemPedido
from database.connection import Session
from services.cliente_service import buscar_cliente_por_id
from services.produto_service import buscar_produto_por_id
from sqlalchemy.orm import joinedload

def buscar_pedido_por_id(idpedido, session):
       
        pedido = session.query(Pedido).filter(Pedido.id == idpedido).first()
        return pedido

def criar_pedido(idcliente):

    session = Session()

    try:
        cliente = buscar_cliente_por_id(idcliente, session)

        if not cliente:
            return {'sucesso': False, 'mensagem': 'Cliente não encontrado.'}
        
        novo_pedido = Pedido(valor_total= 0, id_cliente=idcliente, status='PENDENTE')

        session.add(novo_pedido)
        session.commit()
        return {'sucesso': True, 'mensagem': 'Pedido criado com sucesso!'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao criar pedido: {erro}'}

    finally:
        session.close()

def listar_pedidos():

    session = Session()

    try:
        pedidos = session.query(Pedido).options(joinedload(Pedido.cliente)).all()

        if not pedidos:
            return {'sucesso': False, 'mensagem': 'Não há pedidos pra mostrar.', 'dados': []}
        
        return {'sucesso': True, 'mensagem': 'Pedidos encontrados', 'dados': pedidos}
            
    except Exception as erro:
        return {'sucesso': False, 'mensagem': f'Erro ao listar pedidos: {erro}', 'dados': []}

    finally:
        session.close()


def adicionar_item_ao_pedido(idpedido, idproduto, quantidade):

    if quantidade <= 0:
        return {'sucesso': False, 'mensagem': 'Erro: Digite uma quantidade válida.' }
    
    session = Session ()
    
    try:
        pedido = buscar_pedido_por_id(idpedido, session)

        if not pedido:
            return {'sucesso': False, 'mensagem': 'Erro: Digite um id pedido válido.'}
        
        if pedido.status != 'PENDENTE':
            return {'sucesso': False, 'mensagem': 'Erro: não é possivel adicionar itens a este pedido.'}
        
        produto = buscar_produto_por_id(idproduto, session)

        if not produto:
            return {'sucesso': False, 'mensagem': 'Erro: Digite um id produto válido.'}
        
        if produto.estoque < quantidade:
            return {'sucesso': False, 'mensagem': 'Estoque insuficiente.'}
        
        preco_unitario = produto.preco
        subtotal = preco_unitario * quantidade

        item_pedido = ItemPedido(preco_unitario = preco_unitario,
                                 subtotal = subtotal,
                                 quantidade = quantidade,
                                 id_pedido = idpedido,
                                 id_produto = idproduto)
        
        novo_estoque = produto.estoque - quantidade
        produto.estoque = novo_estoque

        novo_total = subtotal + pedido.valor_total
        pedido.valor_total = novo_total

        session.add(item_pedido)
        session.commit()
        return {'sucesso': True, 'mensagem': 'Item adicionado ao pedido com sucesso.'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao adicionar item ao pedido: {erro}'}
    
    finally:
        session.close()

def finalizar_pedido(idpedido):

    session = Session()

    try:
        pedido = buscar_pedido_por_id(idpedido, session)

        if not pedido:
            return {'sucesso': False, 'mensagem': 'Erro: digite um idpedido válido'}
        
        if pedido.status != 'PENDENTE':
            return {'sucesso': False, 'mensagem': 'Erro: não é possivel finalizar pedido.'}
        
        if pedido.valor_total <= 0:
            return {'sucesso': False, 'mensagem': 'Erro: não é possivel finalizar um pedido sem itens.'}

        pedido.status = 'FINALIZADO'
        session.commit()
        return {'sucesso': True, 'mensagem': 'Pedido finalizado.'}
    
    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao finalizar pedido: {erro}'}
    
    finally:
        session.close()


def cancelar_pedido(idpedido):

    session = Session()

    try:
        pedido = buscar_pedido_por_id(idpedido, session)

        if not pedido:
            return {'sucesso': False, 'mensagem': 'Erro: Digite um id pedido válido'}
        
        if pedido.status != 'PENDENTE':
            return {'sucesso': False, 'mensagem': 'Erro: Não é possivel cancelar o pedido'}

        for item in pedido.itens:
            item.produto.estoque += item.quantidade

        pedido.status = 'CANCELADO'
        session.commit()
        return {'sucesso': True, 'mensagem': 'Pedido cancelado.'}

    
    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao cancelar pedido: {erro}'}
    
    finally:
        session.close()

def buscar_pedido(idpedido):

    session = Session ()

    try:
        pedido = session.query(Pedido).filter(Pedido.id==idpedido).first()

        if not pedido:
            return {'sucesso': False, 'mensagem': 'Não há pedidos pra mostrar.', 'dados': None}
        
        return {'sucesso': True, 'mensagem': 'Pedido encontrado.', 'dados': pedido}
    
    except Exception as erro:
        return {'sucesso': False, 'mensagem': f'Erro ao buscar pedido: {erro}', 'dados': None}

    finally:
        session.close()




        

    

    
    

        


    
    






