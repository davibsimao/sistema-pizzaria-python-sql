from interface.formatters import titulo, moeda

def menu_produto(produto_service):
    while True:
        titulo('OPÇÕES DE PRODUTO')
        print('''
1 - cadastrar produto
2 - listar produto
3 - atualizar produto
4 - deletar produto
5 - voltar a pagina anterior 
''')
        try:
            sub = int(input('Digite sua opção do produto: '))

        except ValueError:
            print('Digite um número válido')
            continue

        if sub == 1: 

            try:
                nome = str(input('nome do produto: ')).lower().strip()
                preco = float(input('preço do produto: '))
                estoque = int(input('estoque do produto: '))

            except Exception as erro:
                print(f'Erro ao cadastrar produto: {erro}')
                continue

            resultado = produto_service.cadastrar_produto(nome, preco, estoque)

            print(resultado['mensagem'])


        elif sub == 2: 

            resultado = produto_service.listar_produtos()

            if not resultado['sucesso']:
                print(resultado['mensagem'])
            
            else:
                for produto in resultado['dados']:
                    print(f'Nome: {produto.nome} | Preço: {moeda(produto.preco)} | Estoque: {produto.estoque}')

        elif sub == 3: 

            try:
                idproduto = int(input('id produto para atualizar os dados: '))
                novo_nome = str(input('Novo nome: ')).strip().lower()
                novo_preco = float(input('Novo preço: '))
                novo_estoque = int(input('Novo estoque: '))

            except ValueError:
                print('Erro ao informar os dados do produto. ')
                continue

            resultado = produto_service.atualizar_produto(idproduto, novo_nome, novo_preco, novo_estoque)

            print(resultado['mensagem'])


        elif sub == 4: 

            try:
                idproduto = int(input('id produto que deseja remover: '))

            except ValueError:
                print('Erro ao informar os dados do produto. ')
                continue

            resultado = produto_service.remover_produto(idproduto)

            print(resultado['mensagem'])
        
        elif sub == 5:

            print('Voltando para a pagina anterior.')
            break

        else:

            print('Digite uma opção válida.')
            continue
    