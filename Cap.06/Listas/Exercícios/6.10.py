#Programa 6.9 - Pesquisa sequencial:

L = [1, 2, 3, 4, 5, 6]

while True:
    v = int(input("Digite um valor: "))
    f = int(input("Digite um valor: "))
    posicao_v = L.index(v)
    posicao_f = L.index(f)
    if posicao_v and posicao_f:
        print(f"\nValor {v} encontrado na posição {posicao_v}"
              f"\nValor {f} encontrado na posição {posicao_f}")
    else:
        print("\nValores não encontrados!")
