#Faça um programa que calcule o aumento de um salário. Solicite o valor do salário e o aumento percentual.
#Exiba o valor do aumento:

salario = float(input("Digite o valor do seu salário: R$"))
aumento_percentual = int(input("Digite o valor do aumento %: "))
aumento_salario = salario * (aumento_percentual/100)
salario_atual = salario + aumento_salario

print(f"Valor do salário atualizado: R${salario_atual}", f"\nValor do aumento: R$ {aumento_salario}")
