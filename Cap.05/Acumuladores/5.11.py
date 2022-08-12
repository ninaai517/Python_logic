#5.11 - Escreva um programa que pergunte o valor do depósito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês p/os 24 primeiros meses.
#Escreva o total ganho com juros no período:


deposito = float(input("Informe o valor do depósito: R$ "))
txa_juros = float(input("Informe a taxa de juros (%): "))
total_ganho = deposito
mes = 1  # incremento

print(f'Valor depositado: R${deposito}')

while mes <= 24:
    total_ganho = total_ganho * (1 + txa_juros)
    print(f"mês {mes}: R$ {total_ganho:.2f} ")
    mes = mes + 1

print(f'\n{total_ganho:.2f}')

