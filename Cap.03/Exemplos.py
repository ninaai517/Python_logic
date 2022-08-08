#Exemplo:

nota = 8
media = 7
aprovado = nota > media
print(aprovado)

#Digite se uma pessoa pagará imposto ou não. Condição Salario > 1200 -> paga!
salario = float(input("Digite o seu salário atual: "))
pagarImposto = salario > 1200
print(pagarImposto)

#Exemplo 2:

anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R$ {bonus:5.2f}")
