#5.18 - Escreva um programa  que exiba uma lista de opções (menu): +, - , x , / e sair.
#Imprima a tabuada da opção escolhida. Repita até que a opção de saída seja ativada.
import sys
tabuada = 1

while True:
    menu = str(input("Escolha uma operação matemática (soma (+), subtração (-), multiplicação (*) e divisão (/) ou 0 para sair: "))
    while tabuada <= 10:
        num = 1
        while num <= 10:
            if menu == '+':
                print(f"{tabuada} + {num} = {tabuada + num}")
                num += 1
            elif menu == '-':
                print(f"{tabuada} - {num} = {tabuada - num}")
                num += 1
            elif menu == '*':
                print(f"{tabuada} x {num} = {tabuada * num}")
                num += 1
            elif menu == '/':
                print(f"{tabuada} / {num} = {tabuada / num}")
                num += 1
            elif menu == '0':
                sys.exit(0)
        tabuada += 1
    tabuada = 1
