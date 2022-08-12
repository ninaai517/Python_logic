#Escreva um programa que leia números inteiros digitados pelo usuário. O programa deve
# ler os números até digitarem 0. Ao final exiba:
    # a) A quantidade de números digitados;
    # b) A soma e a média aritmética dos números.

soma = 0
cont = 0

while True:
    num = int(input("Digite um número ou '0' para sair: "))
    if num == 0:
        break
    soma += num
    cont += 1

media = soma / cont
print(f'\nTotal de números digitados: {cont}', f'\nA soma dos números: {soma}', f'\nMédia aritmética: {media}')

