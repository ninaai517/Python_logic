#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o total a pagar.

preco_produto = float(input("Digite o valor da mercadoria: R$ "))
desconto = float(input("Desconto %: "))
preco_desconto = preco_produto * (desconto/100)
preco_final = preco_produto - preco_desconto

print(f"Preço: R$ {preco_produto:5.2f}",
      f"\nValor do desconto: R$ {preco_desconto:5.2f}",
      f"\nPreço final: R$ {preco_final:5.2f}")
