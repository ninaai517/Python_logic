#Escreva um programa p/ aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar
#o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#O valor da prestação n pode ser superior 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor total do imóvel: R$"))
salario = float(input("Informe o seu salário: R$"))
anos_pagar = int(input("Informe a quantidade de anos a pagar: "))
parcela_mes = valor_casa / (anos_pagar * 12)

if parcela_mes < (0.3 * salario):
    print(f"\nValor da parcela mensal: R${parcela_mes:.2f}","Empréstimo autorizado!")
else:
    print(f"\nValor da parcela mensal: R${parcela_mes:6.2f}","\nEmpréstimo não autorizado!")

