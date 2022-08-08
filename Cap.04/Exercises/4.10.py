#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação (R = residencial, C = comercial e I = industrial)

kWh_consumo = int(input("Informe a quantidade de kWh consumida: "))
tipo_instalacao = input("Informe o tipo de instalação: ")
preco = 0

if kWh_consumo < 500 and tipo_instalacao == 'R':
    preco = kWh_consumo * 0.40
else:
    preco = kWh_consumo * 0.65

if kWh_consumo < 1000 and tipo_instalacao == 'C':
    preco = kWh_consumo * 0.55
else:
    preco = kWh_consumo * 0.60

if kWh_consumo < 5000 and tipo_instalacao == 'I':
    preco = kWh_consumo * 0.55
else:
    preco = kWh_consumo * 0.60

print(f"\nkWh consumido: {kWh_consumo}", f"\nPreço final: R${preco}", f"\nTipo de instação: {tipo_instalacao}")



