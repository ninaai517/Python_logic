#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a
#velocidade esperada.

distancia = float(input("Digite a distância do trajeto em km: "))
velocidade_media = float(input("Digite a velocidade média esperada para o trajeto km/hr: "))
tempo_viagem = distancia / velocidade_media

print(f"O tempo de viagem é aproximadamente: {tempo_viagem} hr(s)")
