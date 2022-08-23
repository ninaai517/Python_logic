qntd = int(input("Informe o nº de pessoas na fila: "))
fila_preferencial = list(range(1, qntd + 1))
while True:
    print(f"\nFila - nº de pessoas: {len(fila_preferencial)}")
    opcao = input("\nEscolha uma das opções abaixo:"
                  "\n1 para contabilizar mais 1 pessoa na fila,"
                  "\n2 para atendimento ou"
                  "\n3 para sair: ")
    print(f"\nNº de pessoas na fila preferêncial: {qntd}")
    if opcao == '1':
        qntd += 1
        fila_preferencial.append(qntd)
        print(f"Nº de elementos atual: {len(fila_preferencial)}")
    elif opcao == '2':
        if len(fila_preferencial) > 0:
            atendimento = fila_preferencial.pop(0)
            print(f"Atendimento realizado!")
        else:
            print("\nFila vazia")
    elif opcao == '3':
        break
    else:
        print("\nValo inválido! Digite 1, 2 ou 3!")
