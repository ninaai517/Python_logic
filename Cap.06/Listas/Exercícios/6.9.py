#Programa 6.9 - Pesquisa sequencial:

L = [5, 12, 3, 4]
x = 0
while x < len(L):
    p = int(input("Digite um valor a procurar: "))
    v = int(input("Digite outro valor a procurar: "))
    if L[x] == p:
        print(f'\nPrimeiro valor digitado: {p} -> achado na posição {[x]}!')
        break
    elif L[x] == v:
        print(f'\nSegundo valor digitado: {v} -> achado na posição {[x]}!')
        break
    else:
        print(f"\nValor de {p} não encontrado! Tente novamente")
    x += 1
