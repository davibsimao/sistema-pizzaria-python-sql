from interface.formatters import titulo, moeda

def menu_pedido(pedido_service):
    while True:
        titulo('OPÇÕES DE PEDIDO')
        print('''
1 - criar pedido
2 - listar pedidos
3 - adicionar produto ao pedido
4 - finalizar pedido
5 - cancelar pedido
6 - voltar a pagina anterior       
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
                    print(f'ID: {pedido.id} | Cliente: {pedido.cliente.nome} | Valor total: {moeda(pedido.valor_total)} | Status: {pedido.status}')

        
        elif sub == 3:

            try:
                idpedido = int(input('Digite o id pedido: '))
                idproduto = int(input('Digite o id produto: '))
                quantidade = int(input('Digite a quantidade: '))
            
            except Exception as erro:
                print(f'Erro ao adicionar item ao pedido: {erro}')
                continue

            resultado = pedido_service.adicionar_item_ao_pedido(idpedido, idproduto, quantidade)
            print(resultado['mensagem'])
        
        elif sub == 4:

            try:
                idpedido = int(input('Digite o id pedido: '))
            
            except Exception as erro:
                print(f'Erro ao finalizar pedido: {erro}')
                continue

            resultado = pedido_service.finalizar_pedido(idpedido)
            print(resultado['mensagem'])
        
        elif sub == 5:

            try:
                idpedido = int(input('Digite o id pedido: '))
            
            except Exception as erro:
                print(f'Erro ao cancelar pedido: {erro}')
                continue

            resultado = pedido_service.cancelar_pedido(idpedido)
            print(resultado['mensagem'])

        elif sub == 6:

            print('Voltando para a pagina anterior.')
            break
        
        else:
            print('Erro: Digite uma opção válida.')
            continue
            
