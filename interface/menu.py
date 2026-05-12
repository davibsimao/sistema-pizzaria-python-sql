from interface.menu_produto import menu_produto
from interface.menu_cliente import menu_cliente

from services import produto_service, cliente_service


def menu():
    while True:
        print('''
1 - Opções de produto
2 - Opções de pedido
3 - Opções de itens pedidos
4 - Opções de cliente
5 - Sair do sistema
 ''')
        try:
            opc = int(input('Digite sua opção: '))

        except ValueError:
            print('ERRO: Digite um número válido')
            continue

        if opc == 1:
            menu_produto(produto_service)
        
        if opc == 4:
            menu_cliente(cliente_service)

        elif opc == 5:
            print('Saindo do sistema.. Volte sempre.')
            break
        else:
            print('ERRO: Digite uma opção válida.')