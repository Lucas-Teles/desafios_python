'''DESAFIO 11
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Você digitou os valores {num}')
print(f'Nos numeros digitados o 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 foi digitado na posição {num.index(3)+1}')
else:
    print('O primeiro número 3 não foi digitado.')
pares = [n for n in num if n % 2 == 0]
if pares:
    print(f'Esses são os numeros pares {pares}')
else:
    print('Não foi digitado numeros pares')