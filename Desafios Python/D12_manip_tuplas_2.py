'''Criando uma lista de compras, manipulando e dando um design a lista.'''

lista_compras = ('Lapís', 1.75,
                 'Caneta', 2.00,
                 'Caderno', 10.00,
                 'Regua', 5.50,
                 'Borracha', 0.75,
                 'Mochila', 85.00,
                 'Livro', 35.00,
                 'Estojo', 12.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0, len(lista_compras)):
    if c % 2 == 0:
        print(f'{lista_compras[c]:.<30}', end='')
    else:
        print(f'R$ {lista_compras[c]:>6.2f}')
print('-' * 40)