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

            if sub == 1: # cadastrar produto
                try:
                    nome = str(input('nome do produto: ')).lower().strip()
                    preco = float(input('preço do produt: '))
                    estoque = int(input('estoque do produto: '))

                except Exception as erro:
                    print(f'Erro ao cadastrar produto: {erro}')
                    continue

                produto_service.cadastrar_produto(nome, preco, estoque)

            elif sub == 2: # listar produtos
                produto_service.listar_produtos()
            
            elif sub == 5:
                print('Voltando para a pagina anterior.')
                break

            else:
                print('Digite uma opção válida.')
                continue