def piramidedoCaralho(altura):
    for piramideduk7 in range(1,altura+1):

        espacos = ' '*(altura-piramideduk7)
        asteriscos = '*' * (2*piramideduk7-1)

        print(espacos + asteriscos + espacos)

altura = int(input('Qual a altura da pirâmide du Caralho? '))
piramidedoCaralho(altura)