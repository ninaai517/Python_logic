#Simulação da fila de um banco:

ultimo = 3
fila = list(range(2, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite:"
          "\nA - Realizar o atendimento"
          "\nF - Fim da fila"
          "\nS para Sair")
    operacao = input("Digite A,F ou S: ")
    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido!')
        else:
            print('Fila vazia!')
    elif operacao == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida ! Digte uma das opções válidas !')
