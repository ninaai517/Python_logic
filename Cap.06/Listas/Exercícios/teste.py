##############################################################################
# Parte do livro IntroduÃ§Ã£o Ã  ProgramaÃ§Ã£o com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2022
# Primeira ediÃ§Ã£o - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda ediÃ§Ã£o - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira EdiÃ§Ã£o - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 06\exercicio-06-03.py
##############################################################################

primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if e == 0:
        break
    segunda.append(e)
terceira = []
# Aqui vamos criar uma outra lista, com os elementos da primeira
# e da segunda. Existem vÃ¡rias formas de resolver este exercÃ­cio.
# Nesta soluÃ§Ã£o, vamos pesquisar os valores a inserir na terceira
# lista. Se nÃ£o existirem, adicionaremos Ã  terceira. Caso contrÃ¡rio,
# nÃ£o copiaremos, evitando assim os repetidos.
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1
