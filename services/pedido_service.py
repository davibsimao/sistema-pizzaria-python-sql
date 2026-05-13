from models.pedido import Pedido
from models.cliente import Cliente 
from models.item_pedido import ItemPedido
from database.connection import Session
from services.cliente_service import buscar_cliente_por_id

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
        pedidos = session.query(Pedido).all()

        if not pedidos:
            return {'sucesso': False, 'mensagem': 'Não há pedidos pra mostrar.'}
        
        return {'sucesso': True, 'mensagem': 'Pedidos encontrados', 'dados': pedidos}
            
    except Exception as erro:
        return {'sucesso': False, 'mensagem': 'Erro ao listar pedidos: {erro}', 'dados': []}

    finally:
        session.close()
        


    
    






