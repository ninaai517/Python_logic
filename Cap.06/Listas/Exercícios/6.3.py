#Faça um programa com duas listas e gere uma terceira sem repetir os elementos:
import sys

Lista_um = []
Lista_dois = []

while True:
    n = int(input(f"Lista 1 - Digite um valor  ou 0 para sair: "))
    if n == 0:
        break
    Lista_um.append(n)
while True:
    n = int(input(f"Lista 2 - Digite um valor  ou 0 para sair: "))
    if n == 0:
        break
    Lista_dois.append(n)

Lista_tres = []
Lista_um_dois = Lista_um[:]
Lista_um_dois.extend(Lista_dois)
x = 0
y = 0

while x < len(Lista_um_dois):
    while y < len(Lista_tres):
        if Lista_um_dois[x] == Lista_tres[y]:
            break
        y += 1
        if y == len(Lista_tres):
            Lista_tres.append(Lista_um_dois[x])
            x += 1
x = 0
while x < len(Lista_tres):
    print(f'{x} : {Lista_tres[x]}')
    x += 1
