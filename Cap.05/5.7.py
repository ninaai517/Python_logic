#Faça um programa que acumule pontos pela resposta correta digitada pelo usuário.

ponto = 0
questao = 1

while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ')
    if questao == 1 and resposta == 'a' or resposta == 'A':
        ponto += 1
    if questao == 2 and resposta == 'b' or resposta == 'B':
        ponto += 1
    if questao == 3 and resposta == 'c' or resposta == 'C':
        ponto += 1

    questao += 1

print(f"\nO aluno fez {ponto} ponto(s)!")
