#4.1 - If:

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print(f"O valor {a} é maior que {b}")
if b > a:
    print(f"O valor {b} é maior que {a}")
else:
    print(f"o valor de a é igual a b!")
#obs.: Senão fosse colocado o else como uma terceira hipótese e se a = b então não haveria nenhuma
       #...saída na terminal.

#4.2 - Carro novo ou velho - dependendo da idade:

idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo!")
else:
    print("Seu carro é velho!")
