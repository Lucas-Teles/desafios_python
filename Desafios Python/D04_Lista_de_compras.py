'''Objetivo: Escreva um programa em Python que ajude os usuários a criar e gerenciar uma lista de compras de supermercado.

Instruções:
- Inicialize uma lista vazia que representará a lista de compras.
- Permita que o usuário adicione itens à lista de compras um por um.
- Forneça a opção de remover itens da lista.
- Exiba a lista de compras atual ao usuário.
- Ofereça a opção de finalizar a lista de compras.'''
print('='*40)
print(f'{"BEM VINDO AO CRIADOR SUA LISTA":^40}')
print('='*40)
lista_compras = []

while True:
    opcao = 0
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        opcao = int(input('''
    [1] Inserir item na lista 
    [2] Remover item da lista
    [3] Verificar lista
    [4] Sair da lista
        -> '''))
    if opcao == 1:
        produto = str(input('Qual nome do item que vai adicionar: ')).strip()
        lista_compras.append(produto)
    if opcao == 2:
        r_produto = str(input('Qual nome do item que deseja remover: ')).strip()
        lista_compras.remove(r_produto)
    if opcao == 3:
        print(lista_compras)
        print(f'Sua lista ficou assim: \n{lista_compras,}')
    if opcao == 4:
        print('Obrigado por usar o programa !')
        print(f'Sua lista ficou assim: \n{lista_compras,}')
print('Espero você em breve')


