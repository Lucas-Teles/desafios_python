from desafio16.lib.interface import *

while True:
    resp = menu(['D4', 'D6', 'D18', 'D12', 'D20', 'Tel\'s dice', 'sair'])
    if resp == 1:
        cabecalho('Opcão 1')
    if resp == 2:
        cabecalho('Opção 2')
    break