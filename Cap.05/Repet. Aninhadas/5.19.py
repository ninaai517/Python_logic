""""Escreva um programa que leia um número e verifique se é ou não um número primo.
Para verificar divida o resto da divisão por 2."""
num = int(input("Digite um número: "))
div = 1
divisao_por_dois = num % 2

if divisao_por_dois == 1:
    nova_divisao = num % 3
    if nova_divisao == 0:
        print("Não é primo")
    elif nova_divisao != 0:
        print("é primo")

if divisao_por_dois == 0:
    print("Não é primo!")



