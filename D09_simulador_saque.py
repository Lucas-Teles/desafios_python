print('=' * 30)
print('{:^30}'.format('Caixa eletronico     LucBank'))
print('=' * 30)
valor = int(input('Insira o valor que deseja sacar: R$ '))
total = valor
ced = 50 #cedula inicial
total_ced = 0 #Contador das cedulas
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 30)
print('Tenha um ótimo dia !')