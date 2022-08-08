#Escreva um programa que calcule o salário de um funcionário.
#P/ salários maiores que 1250,00 reais o aumento é de 10%. Abaixo disso o aumento é 15%.

salario = float(input("Salário atual: R$ "))
aumento = 0
novo_salario = 0

if salario > 1250:
    aumento += salario + (salario * 0.1)
    novo_salario = aumento

if salario <= 1250:
    aumento += salario + (salario * 0.15)
    novo_salario = aumento

print(f"O valor do salário com reajuste é: R${novo_salario:6.2f}")
