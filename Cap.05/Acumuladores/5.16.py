#Programa - Contagem de cédulas.

#Testes: tentar executar o programa digitando o valor 0.001.
#Acrescentar na contagem de dinheiro a nota de 100 e as moedas.

#Leitura do valor:
valor = float(input('Digite o valor a pagar: '))

#contagem de cédulas:
cedulas = 0

atual = 100
valor_pagar = valor

while True:
    if atual <= valor_pagar:
        valor_pagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if valor_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        else:
            break
        cedulas = 0

