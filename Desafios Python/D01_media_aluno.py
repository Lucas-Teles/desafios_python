'''
Criar um programa que calcula a média de três notas.
O programa tem que pedir nome do aluno e inserir as 3 notas.
'''

print('-='*15)
print(f'{"Portal do professor":^30}')
print(f'{"Sistema de média do aluno.":^30}')
print('-='*15)
while True:
    aluno = str(input('Qual o nome do aluno: ')).strip()
    n1 = float(input('Digita a 1ª nota do aluno: '))
    n2 = float(input('Digita a 2ª nota do aluno: '))
    n3 = float(input('Digita a 3ª nota do aluno: '))

    media = (n1 + n2 + n3) / 3

    if media < 0:
        print('Média negativa ou inválida.')
        break

    print('-='*30)
    print(f'A média final do {aluno} é {media:.2f}')

    if 0 <= media < 5:
        print(f'Infelizmente o {aluno} será reprovado.')
    elif 5 < media < 7:
        print(f'O {aluno} está de recuperação')
    elif media >= 7:
        print(f'O {aluno} passou de ano com exito !')
    print('-=' * 30)
    continuar = ' '
    while continuar != 'SN':
        continuar = str(input('Deseja verificar novo aluno [S/N]: ')).upper().strip()
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            print('Resposta invalida tente novamente. ', end='')
    if continuar == 'N':
        break
print('\nObrigado e volte sempre !')
