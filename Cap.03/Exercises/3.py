#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundos:

dias_usuario = int(input("Digite o numero de dias: "))
hrs_usuario = int(input("Digite o numero de hrs: "))
min_usuario = int(input("Digite o numero de min: "))
seg_usuario = int(input("Digite o numero de segundos: "))

total_tempo_usuario = (dias_usuario*86400) + (hrs_usuario * 3600) + (min_usuario * 60) + seg_usuario
print(f"O total em segundos do usuário é: {total_tempo_usuario}")



