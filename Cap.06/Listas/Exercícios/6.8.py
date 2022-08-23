#Programa 6.9 - Pesquisa sequencial:

L = [5, 12, 3, 4]
x = 0
while x < len(L):
    p = int(input("Digite um valor a procurar: "))
    if L[x] == p:
        print(f'\n{p} achado na posição {[x]}!')
        break
    else:
        print(f"\nValor de {p} não encontrado! Tente novamente")
    x += 1
