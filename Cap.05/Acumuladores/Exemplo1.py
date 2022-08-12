#1 - acumulando um numero qualquer digitado aleatoriamente pelo usuário:

n = 1
soma = 0

while n <= 10:
    x = int(input(f'Digite o {n}º número: '))
    soma += x
    n = n + 1

print(f'Soma: {soma}')

#2 - Média:

x = 1
soma = 0

while x <= 5:
    nota = int(input(f'Digite a {x}ª nota: '))
    soma += nota
    x = x + 1

print(f'Média {soma / 5:5.1f}')



