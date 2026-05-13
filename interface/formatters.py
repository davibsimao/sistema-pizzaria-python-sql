def linha(tamanho=40):
    return '-' * tamanho


def titulo(texto):

    print(linha())
    print(texto.center(40))
    print(linha())


def moeda(valor):

    return f'R$ {valor:.2f}'.replace('.', ',')
