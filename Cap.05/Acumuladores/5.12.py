#5.12 - Reescreva o programa 5.11 perguntando o depósito de cada mês:

txa_juros = float(input("Informe a taxa de juros (%): "))
total_ganho = 0
mes = 1  # incremento

while mes <= 12:
    deposito = float(input("Informe o valor do depósito: R$ "))
    total_ganho += deposito + (deposito * txa_juros)
    deposito = total_ganho
    print(f"mês {mes}: R$ {deposito:.2f} ")
    mes += 1

print(f'\nValor total: R${total_ganho}')
