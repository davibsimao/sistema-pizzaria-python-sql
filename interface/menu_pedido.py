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

            resultado = pedido_service.criar_pedido(idcliente)
            print(resultado['mensagem'])

        elif sub == 2:

            resultado = pedido_service.listar_pedidos()

            if not resultado['sucesso']:
                print(resultado['mensagem'])
                
            else:
                for pedido in resultado['dados']:
                    print(f'ID: {pedido.id} | Valor total: R${pedido.valor_total} | Status: {pedido.status} | Cliente: {pedido.id_cliente}')

        elif sub == 5:

            print('Voltando para a pagina anterior.')
            break
            
