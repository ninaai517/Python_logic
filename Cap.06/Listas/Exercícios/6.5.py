""""Altere o programa 6.7 de forma à trabalhar com vários comandos digitados de uma só vez.
Atualmente somente um comando pode ser inserido por vez.
Altere-o de forma a considerar a operação como uma String.

Ex.: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e finalmente uma saída."""
import sys

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite:"
          "\nA - Realizar o atendimento"
          "\nF - Fim da fila"
          "\nS para Sair")
    operacao = input("Digite A,F ou S: ")
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0) #Reduz a fila
                print(f"Cliente {atendido} atendido!")
            else:
                print("Fila vazia!")
        elif operacao[x] == "F":
            ultimo += 1 #Incrementa a fila
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operacao[x]} na posição {x}! Digite apenas, A, F ou S!")
        x += 1
    if sair:
        break
