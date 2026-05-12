def menu_produto(produto_service):
    while True:
        print('-'*30)
        print(f'{"OPÇOES DE PRODUTO".center(30)}')
        print('-'*30)
        print('''
1 - cadastrar produto
2 - listar produto
3 - atualizar produto
4 - deletar produto
5 - voltar
''')
        try:
            sub = int(input('Digite sua opção do produto: '))

        except ValueError:
            print('Digite um número válido')
            continue

        if sub == 1: # cadastrar produtos

            try:
                nome = str(input('nome do produto: ')).lower().strip()
                preco = float(input('preço do produto: '))
                estoque = int(input('estoque do produto: '))

            except Exception as erro:
                print(f'Erro ao cadastrar produto: {erro}')
                continue

            produto_service.cadastrar_produto(nome, preco, estoque)

        elif sub == 2: # listar produtos

            produto_service.listar_produtos()

        elif sub == 3: # atualizar produtos

            try:
                idproduto = int(input('id produto para atualizar os dados: '))

            except ValueError:
                print('Erro ao informar os dados do produto. ')
                continue

            produto_service.atualizar_produto(idproduto)

        elif sub == 4: # remover produtos

            try:
                idproduto = int(input('id produto que deseja remover: '))

            except ValueError:
                print('Erro ao informar os dados do produto. ')
                continue

            produto_service.remover_produto(idproduto)
        
        elif sub == 5:

            print('Voltando para a pagina anterior.')
            break

        else:

            print('Digite uma opção válida.')
            continue
    