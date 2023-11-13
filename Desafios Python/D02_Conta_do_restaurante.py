'''
Eu e minha noiva fomos almoçar no mercado dos peixes,
comemos camarão, comemos batata frita, um peixe e baião, compramos também uma coquinha gelada.
No fim de tudo chegou a nossa temida conta,
e além da nossa conta teria que pagar o serviço que seria de 14%, fora o couvert de 5 reais.
Então ficamos na duvida de como calcular, seria mt legal ter um programa que pegasse o valor da conta,
o valor que tenho que pagar de gorjeta o couvert se tiver. e ja me desse a resposta.
'''


total = float(input('Digite valor total da conta: R$ '))
gorjeta = int(input('Taxa de Serviço: (%) '))
total_com_gorjeta = total*(1+(gorjeta/100))


couvert = float(input('Valor Couvert: R$ '))


total_geral = total_com_gorjeta + couvert

print('=-'*30)
print('Total da conta: R$ {:.2f}'.format(total))
print('Taxa de serviço: {}%'.format(gorjeta))
print('Couvert R$ {:.2f}'.format(couvert))
print('Valor total a pagar: R$ {:.2f}'.format(total_geral))
print('=-'*30)