#Calculo do imposto de renda:

salario = float(input("Digite o valor do seu salário: R$ "))
base = salario
imposto = 0

if salario < 1000:
    print("Você está isento do I.R.!")

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)


print(f"Salário: R${salario}", f"\nImposto a pagar: R${imposto:6.2f}")
