from lib.interface import *
from lib.arquivo import *

arq = 'usuarios.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver Personagens', 'Criar novo Personagem', 'sair'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Até mais')
        break
    else:
        print('\033[31mErro: digite uma opção válida\033[m')