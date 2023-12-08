def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')


def dobro(preco=0,formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def triplo(preco=0,formato=False):
    res = preco * 3
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def aumento(preco=0, taxa=0, formato=False):
    res = preco + (preco * (taxa/100))
    return res if formato is False else moeda(res)

def desconto(preco=0, taxa=0, formato=False):
    res = preco - (preco * (taxa/100))
    return res if formato is False else moeda(res)

def resumo(preco, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumento(preco, taxa, True)}')
    print(f'{taxar}% de redução: \t\t{desconto(preco, taxa, True)}')
    print('-' * 30)