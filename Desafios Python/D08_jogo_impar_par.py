''' Jogo impar/par que quando vc ganha, a maquina pede para ir novamente.'''
from random import randint
v = 0
while True:
    jogador = int(input('Informe o valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e eu joguei {computador} o total deu {total}')
    print('DEU PAR !' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU !!!')
            v += 1
        else:
            print('VOCÊ PERDEU !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU !!!')
            v += 1
        else:
            print('VOCÊ PERDEU !')
            break
    print('Vamos novamente...')
print(f'Game Over -> Você ganhou um total de {v} vezes')
