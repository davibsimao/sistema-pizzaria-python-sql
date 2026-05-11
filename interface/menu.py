from interface.menu_produto import menu_produto
from services import produto_service


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
            print('Digite um número válido')
            continue

        if opc == 1:
            menu_produto(produto_service)

        elif opc == 5:
            print('Saindo do sistema.. Volte sempre.')
            break