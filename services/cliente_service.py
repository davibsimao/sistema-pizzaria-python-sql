from models.cliente import Cliente
from database.connection import Session


def buscar_cliente_por_id(idcliente, session):

    cliente = session.query(Cliente).filter(Cliente.id == idcliente).first()
    return cliente


def cadastrar_cliente(nome, telefone):

    if not nome:
        return {'sucesso': False, 'mensagem': 'Digite um nome valido.'}

    if not telefone.isdigit():
        return {'sucesso': False, 'mensagem': 'Digite um numero de telefone valido.'}

    session = Session()

    try:
        cliente = session.query(Cliente).filter(Cliente.telefone == telefone).first()

        if cliente:
            return {'sucesso': False, 'mensagem': 'Cliente ja cadastrado.'}

        novo_cliente = Cliente(nome=nome, telefone=telefone)

        session.add(novo_cliente)
        session.commit()

        return {'sucesso': True, 'mensagem': 'Cliente cadastrado com sucesso!'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao cadastrar cliente: {erro}'}

    finally:
        session.close()



def listar_clientes():

    session = Session()

    try:
        clientes = session.query(Cliente).all()

        if not clientes:
            return {'sucesso': False, 'mensagem': 'Nao ha clientes para mostrar.', 'dados': []}

        return {'sucesso': True, 'mensagem': 'Clientes encontrados.', 'dados': clientes}

    except Exception as erro:
        return {'sucesso': False, 'mensagem': f'Erro ao listar clientes: {erro}', 'dados': []}

    finally:
        session.close()


def atualizar_cliente(idcliente, novo_nome, novo_telefone):

    if not novo_nome:
        return {'sucesso': False, 'mensagem': 'Digite um nome valido.'}

    if not novo_telefone.isdigit():
        return {'sucesso': False, 'mensagem': 'Digite um numero valido.'}

    session = Session()

    try:
        cliente = buscar_cliente_por_id(idcliente, session)

        if not cliente:
            return {'sucesso': False, 'mensagem': 'Cliente nao encontrado.'}

        cliente.nome = novo_nome
        cliente.telefone = novo_telefone
        session.commit()

        return {'sucesso': True, 'mensagem': 'Cliente atualizado com sucesso.'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao atualizar cliente: {erro}'}

    finally:
        session.close()


def remover_cliente(idcliente):
    
    session = Session()

    try:
        cliente = buscar_cliente_por_id(idcliente, session)

        if not cliente:
            return {'sucesso': False, 'mensagem': 'Cliente nao encontrado.'}

        session.delete(cliente)
        session.commit()

        return {'sucesso': True, 'mensagem': 'Cliente removido com sucesso.'}

    except Exception as erro:
        session.rollback()
        return {'sucesso': False, 'mensagem': f'Erro ao remover cliente: {erro}'}

    finally:
        session.close()

def buscar_cliente(idcliente):

    session = Session() 

    try:
        cliente = session.query(Cliente).filter(Cliente.id==idcliente).first()

        if not cliente:
            return {'sucesso': False, 'mensagem': 'Cliente não encontrado.', 'dados': None}
        
        return {'sucesso': True, 'mensagem': 'Cliente encontrado.', 'dados': cliente}
    
    except Exception as erro:
        return {'sucesso': False, 'mensagem': f'Erro ao buscar cliente: {erro}', 'dados': None}

    finally:
        session.close()
