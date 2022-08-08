#Faça a conversão de ºC en ºF: fórmula F = ((9*C)/5) + 32

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_farenheit = ((9 * temperatura_celsius) / 5) + 32
print(f"Temperatura (ºC): {temperatura_celsius}",
      f"\nTemperatura (ºF): {temperatura_farenheit}")
