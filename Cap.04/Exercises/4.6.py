#Preço do produto pela categoria.

categoria = int(input("Escolha uma categoria de 1 a 5: "))
preco= 0

if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 18.00
elif categoria == 3:
    preco = 23.00
elif categoria == 4:
    preco = 26.00
elif categoria == 5:
    preco = 31.00

else:
    print("Opção inválida! Escolha uma categoria de 1 a 5.")
    categoria = int(input("Escolha uma categoria de 1 a 5: "))

print(f"O valor do produto da categoria {categoria} é: R${preco:5.2f}")

