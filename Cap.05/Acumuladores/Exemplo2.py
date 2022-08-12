s = 0

while True:
    v = int(input("Digite um número inteiro maior que 0 ou 0 para sair: "))
    if v == 0:
        break
    s += v

print(f'\nvalor da soma: {s}')
