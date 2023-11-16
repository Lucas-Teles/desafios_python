'''
Criar uma tupla que mnostre os 20 times da série A, na ordem da colocação.
- Mostrar os 5 primeiros times.
- Os últimos 4 colocados para ser rebaixado
- Times em ordem alfabética
- Em que posição está o São Paulo
'''

tabela = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG',
'Flamengo', 'Athletico-PR', 'Fluminese', 'Cuiabá', 'São Paulo',
'Corithians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco', 'Bahia', 
'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os 4 ultimos são: {tabela[-4:]}')
print(f'A tabela em ordem alfabetica: \n{sorted(tabela)}')
colocacao = tabela.index('São Paulo')
print(f'O São Paulo se encontra em {colocacao + 1}º colocado.')