""""Modifique o programa para trabalhar com duas filas.
P/ facilitar, considere atendimento: A = fila 1. B = fila 2...etc."""

ultimo = 10
ultimo_dois = 5
fila_um = list(range(1, ultimo + 1))
fila_dois = list(range(1, ultimo_dois + 1))
while True:
    fila = (input("Selecione qual fila irá trabalhar 1 ou 2: "))
    if fila == '1' or fila == '2':
        if fila == '1':
            print(f"\nExistem {len(fila_um)} clientes na fila")
            print(f"Fila atual: {fila_um}")
        elif fila == '2':
            print(F"\nExistem {len(fila_dois)} clientes na fila")
            print(f"\nFila atual: {fila_dois}")
        print("Digite:"
                "\nA ou B - Realizar o atendimento"
                "\nF ou G- Fim da fila"
                "\nS para Sair")
        operacao = input("Digite Fila 1: A, F ou S "
                         "\nFila 2: B, G ou S: ")
        if operacao == 'A':
            if len(fila_um) > 0:
                atendido = fila_um.pop(0)
                print(f'Cliente {atendido} atendido!')
        elif operacao == "B":
            if len(fila_dois) > 0:
                atendido = fila_dois.pop(0)
                print(f'Cliente {atendido} atendido!')
            else:
                print('Fila vazia!')
        elif operacao == 'F':
            ultimo += 1
            fila_um.append(ultimo)
        elif operacao == "G":
            ultimo_dois += 1
            fila_dois.append(ultimo_dois)
        elif operacao == 'S':
            break
    else:
        print('\nOperação inválida ! Digte uma das opções válidas !')
