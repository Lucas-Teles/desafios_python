'''
Criar um menu de opções - Soma, Multiplicar, Mostrar o Maior, Números novos e sair.
'''

n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
n3 = int(input('Insira o 3º número: '))
maior = n1
while True:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Mostrar o maior
    [4] Novos números
    [5] Sair.
    ''')
    opcao = str(input('O que deseja fazer: ')).strip()
    print('')
    if opcao == '1': #SOMA
        soma = n1 + n2 + n3
        print(f'{n1} + {n2} + {n3} = {soma}')
    elif opcao == '2': #Multiplicar
        multiplicar = n1 * n2 * n3
        print(f'{n1} x {n2} x {n3} = {multiplicar}')
    elif opcao == '3': # Mostrar o maior
        if n2 > maior and n2 > n3:
            maior = n2
            print(f'O maior número é: {maior}')
        elif n3 > maior and n3 > n2:
            maior = n3
            print(f'O maior número é: {maior}')
        elif n1 == n2 == n3:
            print('São todos iguais.')
        else:
            print(f'O maior número é: {maior}')
    elif opcao == '4': #Novos números
        n1 = int(input('Insira o 1º número: '))
        n2 = int(input('Insira o 2º número: '))
        n3 = int(input('Insira o 3º número: '))
    elif opcao == '5': #SAIR
        print('Obrigado por ter vindo! volte sempre')
        break