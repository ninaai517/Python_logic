#Faça um programa que imprima de 1 até o número digitado pelo usuário, sendo eles apenas ímpares:

fim = int(input("Digite um número: "))
x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1
