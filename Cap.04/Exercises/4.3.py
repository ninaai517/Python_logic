#Faça um programa que leia 3 números e imprima o maior e o menor deles:

n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))
n3 = int(input("Digite o valor de n3: "))

if n1 > n2 and n1 > n3:
    print("O valor de n1 é o maior número!")
    if n2 > n3:
        print("O valor de n3 é o menor número!")
    if n3 > n2:
        print("O menor número é n2")

if n2 > n1 and n2 > n3:
    print("O valor de n2 é o maior número!")
    if n1 > n3:
        print("O valor de n3 é o menor número!")
    if n3 > n1:
        print("O menor número é n1")

if n3 > n1 and n3 > n2:
    print("O valor de n3 é o maior número!")
    if n2 > n1:
        print("O valor de n1 é o menor número!")
    if n1 > n2:
        print("O menor número é n2")
