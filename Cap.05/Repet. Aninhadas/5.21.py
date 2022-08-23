""""5.21 - Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter o resultado aproximado. Sendo n o numero a obter a raiz quadrada
considere b a base = 2. """

num = float(input("Digite um número: "))
raiz_quadrada = num ** 0.5
n = raiz_quadrada
b = 2
p = (b + (n / b)) / 2

while True:
    p = p * p
    while (n - p) > 0.0001:
        b = p
        p = (b + (n / b)) / 2

print("fim")
