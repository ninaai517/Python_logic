#Escreva um programa para controlar uma máquina registradora. Solicite ao usuário o cód. do produto e a quantidade.
#Seu programa deve exibir o total de compras depois que digitarem 0 (p/ sair);
#Qualquer código diferente do programado deverá gerar uma mensagem de erro.

total_compras = 0
total_pago = 0
total = 0

while True:
    cod = int(input('Digite o valor do código: '))
    if cod == 0:
        break
    quant = int(input('Digite a quantidade de produtos: '))
    if cod == 1:
        total_pago = quant * 0.5
    elif cod == 2:
        total_pago = quant * 1.0
    elif cod == 3:
        total_pago = quant * 4.0
    elif cod == 5:
        total_pago = quant * 7.0
    elif cod == 9:
        total_pago = quant * 8.0
    else:
            print('Código inválido! Digite um código válido!')
    total_compras += quant
    total += total_pago

print(f'\nTotal de compras: {total_compras} ', f'\nTotal pago: R$ {total_pago:.2f}')


