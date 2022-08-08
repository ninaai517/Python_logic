#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Se a velocidade for maior que 80 km/h, exiba uma mensagem que o usuário foi multado!
#Exiba o valor da multa, sendo ela R$ 5,00 por km ultrapassado a velocidade limite.

velocidade_carro = int(input("Digite a velocidade do seu carro (km/h): "))
multa = float((velocidade_carro - 80) * 5)

if velocidade_carro > 80:
    print("Você foi multado!", f"Valor da multa: R$ {multa:.2f}")
