from models.cliente import Cliente
from database.connection import Session


def buscar_cliente_por_id(idcliente, session):

    cliente = session.query(Cliente).filter(Cliente.id == idcliente).first()
    return cliente


def cadastrar_cliente(nome, telefone):

    session = Session()

    try:
        if not telefone.isdigit():
            print('Digite um número de telefone válido.')
            return

        cliente = session.query(Cliente).filter(Cliente.telefone == telefone).first()

        if cliente:
            print('Cliente já cadastrado.')
            return

        novo_cliente = Cliente(
            nome=nome,
            telefone=telefone)

        session.add(novo_cliente)
        session.commit()
        print('Cliente cadastrado com sucesso!')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao cadastrar cliente: {erro}')

    finally:
        session.close()


def listar_clientes():

    session = Session()

    try:
        clientes = session.query(Cliente).all()

        if not clientes:
            print('Não há clientes para mostrar.')
            return

        for cliente in clientes:
            print(f'ID: {cliente.id} | Nome: {cliente.nome} | Telefone: {cliente.telefone}')

    except Exception as erro:
        print(f'Erro ao listar clientes: {erro}')

    finally:
        session.close()


def atualizar_cliente(idcliente):

    session = Session()

    try:
        cliente = buscar_cliente_por_id(idcliente, session)

        if not cliente:
            print('Cliente não encontrado.')
            return

        novo_nome = str(input('Novo nome: ')).strip().lower()
        novo_telefone = input('Novo telefone: ').strip()

        if not novo_telefone.isdigit():
            print('Digite um número válido.')
            return

        cliente.nome = novo_nome
        cliente.telefone = novo_telefone
        session.commit()
        print('Cliente atualizado com sucesso.')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao atualizar cliente: {erro}')

    finally:
        session.close()


def remover_cliente(idcliente):

    session = Session()

    try:
        cliente = buscar_cliente_por_id(idcliente, session)

        if not cliente:
            print('Cliente não encontrado.')
            return

        session.delete(cliente)
        session.commit()
        print('Cliente removido com sucesso.')

    except Exception as erro:
        session.rollback()
        print(f'Erro ao remover cliente: {erro}')

    finally:
        session.close()

