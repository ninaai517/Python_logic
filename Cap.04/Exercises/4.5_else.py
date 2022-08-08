#Escreva um programa em que pergunte a distância que um passageiro deseja correr.
#Calcule o preço: até 200 km = 0,50 reais. Maior que isso 0,45 reais.

distancia_viagem = int(input("Distância da viagem (km): "))
preco = 0

if distancia_viagem <= 200:
    preco = distancia_viagem * 0.5
else :
    preco = distancia_viagem * 0.45

print(f"Valor da viagem: R${preco:5.2f}")
