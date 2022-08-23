#(()) - > ok, (() -> errado!
parentese = []
while True:
    opcao = (input("\nEscolha uma das opções abaixo: "
                   "\n 1 - Adicionar: "
                   "\n 2 - Remover:"
                   "\n 3 - Sair: "))
    if opcao == '1':
        par = input("Digite abre e fecha parenteses quantas vezes quiser: ")
        parentese.append(par)
        abre_par = parentese[-1].count('(')
        fecha_par = parentese[-1].count(')')
        teste = abre_par == fecha_par
        if teste:
            print("Está certo")
        else:
            print("Está errado! ")
    if opcao == '2':
        parentese.pop(-1)
        abre_par = parentese[-1].count('(')
        fecha_par = parentese[-1].count(')')
        teste = abre_par == fecha_par
        if teste:
            print("Está certo")
        else:
            print(f"\n'{parentese[-1]}' = Incorreto !")
    elif opcao == '3':
        break
    print(parentese)
