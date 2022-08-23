# Escolha um número da lista:

num = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    num[x] = int(input(f"Nº {x + 1}:"))
    x += 1
while True:
    escolha = int(input("Escolha um nº de 1 a 5 ou 0 para sair: "))
    if escolha == 0:
        break
    elif escolha > 5:
        print("Valor inválido! Digite uma opção válida!")
    else:
        print(f"Você escolheu o número: {num[escolha - 1]}")

