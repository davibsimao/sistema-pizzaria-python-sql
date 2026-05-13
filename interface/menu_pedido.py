def menu_pedido(pedido_service):
    while True:
        print('-'*30)
        print(f'{"OPÇOES DE PEDIDO".center(30)}')
        print('-'*30)
        print('''
1 - criar pedido
2 - listar pedidos
3 - 
5 - voltar       
''')
    
        try:
            sub = int(input('Digite sua opção de pedido: '))

        except ValueError:
            print('Digite um número válido')
            continue

        if sub == 1:

            try:
                idcliente = int(input('id cliente para criar pedido: '))

            except Exception as erro:
                print(f'Erro ao criar pedido: {erro}')
                continue

            pedido_service.criar_pedido(idcliente)

        elif sub == 2:

            pedido_service.listar_pedidos()

        elif sub == 5:

            print('Voltando para a pagina anterior.')
            break
            
