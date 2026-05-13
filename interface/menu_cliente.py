def menu_cliente(cliente_service):
    while True:
        print('-'*30)
        print(f'{"OPÇÕES DE CLIENTE".center(30)}')
        print('-'*30)
        print('''
1 - cadastrar cliente
2 - listar clientes
3 - atualizar cliente
4 - deletar cliente
5 - voltar a pagina anterior       
''')
        
        try:
            sub = int(input('Digite sua opção do cliente: '))

        except ValueError:
            print('Digite um número válido')
            continue
    
        if sub == 1: 

            try:
                nome = str(input('nome do cliente: ')).strip().lower()
                telefone = input('telefone do cliente: ')
                
            except Exception as erro:
                print(f'Erro ao cadastrar cliente: {erro}')
                continue

            resultado = cliente_service.cadastrar_cliente(nome, telefone)
            print(resultado['mensagem'])


        elif sub == 2:
            resultado = cliente_service.listar_clientes()

            if not resultado['sucesso']:
                print(resultado['mensagem'])

            else:
                for cliente in resultado['dados']:
                    print(f'ID: {cliente.id} | Nome: {cliente.nome} | Telefone: {cliente.telefone}')


        elif sub == 3:

            try:
                idcliente = int(input(('id cliente para atualizar os dados: ')))
                novo_nome = str(input('Novo nome: ')).strip().lower()
                novo_telefone = input('Novo telefone: ').strip()

            except ValueError:
                print('Erro ao informar os dados do cliente. ')
                continue

            resultado = cliente_service.atualizar_cliente(idcliente, novo_nome, novo_telefone)
            print(resultado['mensagem'])


        elif sub == 4:

            try:
                idcliente = int(input('id cliente que deseja remover: '))

            except ValueError:
                print('Erro ao informar os dados do cliente. ')
                continue

            resultado = cliente_service.remover_cliente(idcliente)
            print(resultado['mensagem'])


        elif sub == 5:
            print('Voltando para a pagina anterior.')
            break

        else:
            print('Digite uma opção válida.')
            continue
