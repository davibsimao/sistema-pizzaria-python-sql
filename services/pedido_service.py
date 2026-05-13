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
            print('Cliente não encontrado')
            return
        
        novo_pedido = Pedido(valor_total= 0, id_cliente=idcliente, status='PENDENTE')

        session.add(novo_pedido)
        session.commit()
        print('Pedido criado com sucesso!')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao criar pedido: {erro}')

    finally:
        session.close()

def listar_pedidos():

    session = Session()

    try:
        pedidos = session.query(Pedido).all()

        if not pedidos:
            print('Não há pedidos pra mostrar. ')
            return
        
        for pedido in pedidos:
            print(f'ID: {pedido.id} | valor total: {pedido.valor_total} | status: {pedido.status} | idcliente: {pedido.id_cliente} ')

    except Exception as erro:
        print(f'Erro ao listar pedidos: {erro}')

    finally:
        session.close()
        


    
    






