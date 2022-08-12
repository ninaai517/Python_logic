#Sem o uso da repetição aninhada:

tabuada = 1
num = 1

while tabuada <= 10:
    print(f"{tabuada} x {num} = {tabuada * num}")
    num += 1
    if num == 11:
        num = 1
        tabuada += 1
        print(' ')
