#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
#Pergunte também o valor que será pago.
#Imprima o número de meses para que a dívida seja paga; O total pago e o Total de juros pago.

divida = float(input('Valor da dívida: R$'))
juro_mes = float(input('Juro mensal %: '))
valor_pago = float(input('Valor a pagar: R$'))
juros_total = 0
total_pago = 0
mes = 0 #contador

while divida > 0:

    total_pago = total_pago + valor_pago #Acumula o valor pago
    divida = divida - valor_pago #recalcula o valor da dívida após ser debitado o pagamento
    divida = divida + (juro_mes * divida)
    juros_total = juros_total + (juro_mes * divida) #Acumula o valor de juros pago
    mes = mes + 1
    print(f'\nValor da dívida no mês {mes}: R${divida:.2f}')


if divida < 0:
    divida = divida * (-1)
    print(f'\nDivida quitada! Saldo em conta: R${divida:.2f}')

print(f'\nMeses para quitar a dívida: {mes}', f'\nTotal pago: R$ {total_pago:.2f}', f'\nTotal de juros pago: R$ {juros_total:.2f}')



