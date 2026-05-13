from interface.menu_produto import menu_produto
from interface.menu_cliente import menu_cliente
from interface.menu_pedido import menu_pedido
from interface.formatters import titulo
from services import produto_service, cliente_service, pedido_service


def menu():
    while True:
        titulo('MENU PRINCIPAL')
        print('''
1 - Opções de produto
2 - Opções de cliente
3 - Opções de pedido
4 - Sair do sistema
 ''')
        try:
            opc = int(input('Digite sua opção: '))

        except ValueError:
            print('ERRO: Digite um número válido')
            continue

        if opc == 1:
            menu_produto(produto_service)
        
        elif opc == 2:
            menu_cliente(cliente_service)
        
        elif opc == 3:
            menu_pedido(pedido_service)

        elif opc == 4:
            print('Saindo do sistema.. Volte sempre.')
            break
        else:
            print('ERRO: Digite uma opção válida.')