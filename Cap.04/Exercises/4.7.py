#Escreva um programa que leia 2 números e pergunte qual a operação que você deseja realizar.
#Exiba o resultado na tela:

n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))
tipo_operacao = input("Escolha uma operação matemática: ")
operacao = 0


if tipo_operacao == '+':
    operacao = n1 + n2

elif tipo_operacao == '-':
    operacao = n1 - n2

elif tipo_operacao == '*':
    operacao = n1 * n2

elif tipo_operacao == '/':
    operacao = n1 / n2
else:
    print("Valor inválido!")

print(f"\nO resultado da operação é {operacao}")

