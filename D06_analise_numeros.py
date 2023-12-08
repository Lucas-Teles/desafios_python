'''
Desenvolver um programa que o usuário quantos números quiser,
e quando ele não quiser mais você vai retornar as seguintes informações:
Quantidade de números
A média dos números digitados
O maior valor
O menor valor
'''
quant_n = 0
maior = menor = 0
somatoria = 0
while True:
    numeros = int(input('Digite um número (Quando quiser parar, basta digitar 0)\n >> '))
    if numeros == 0:
        break
    quant_n += 1
    somatoria += numeros
    if quant_n == 1:
        maior = menor = numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
print(f'Foram digitados {quant_n} números')
print(f'O maior é o {maior}')
print(f'O menor é  o {menor}')
print(f'A media de tododos os números digitados é igual a {somatoria/quant_n:.2f}')