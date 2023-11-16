'''
Tabuada de multiplicação do número digitado
'''
continuar = ' '
while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    for c in range(1, 11):
        print(f'{c} x {n} = {n*c}')
    while continuar != 'N' or continuar != 'S':
        continuar = str(input('Deseja a tabuada de outro número? [S/N] ')).strip().upper()
        if continuar == 'S'or continuar == 'N':
            break
    if continuar == 'N':
        break
print('Fim')