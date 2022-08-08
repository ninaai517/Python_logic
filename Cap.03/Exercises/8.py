#Escreva um programa que pergunte a qntd de km percorridos por um carro alugado + qntd de dias alugados.
#Calcule o preço a pagar sabendo que:
    #o aluguel é R$ 60/dia
    #R$0,15 * km rodado.

km_percorrido = float(input("Digite a quilometragem percorrida: "))
dias_alugado = int(input("Informe a quantidade de diária: "))
preco_total = (dias_alugado * 60) + (0.15 * km_percorrido)

print(f"Preço total do aluguel: R${preco_total:5.2f}")
