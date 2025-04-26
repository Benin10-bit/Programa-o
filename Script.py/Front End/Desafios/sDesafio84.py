import time

dcver = ('s', 'n')
pessoas = []

while True:
    # listas
    dados = []

    # Inputs
    nome = input('Nome: ')
    peso = float(input('peso: '))

    # Adicionar a listas
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    del dados

    # Pergunta se deseja continuar
    dc = input('Deseja continuar? (s/n) ').strip().lower()
    if dc != 's':
        break

    else:
        continue

print("\nLista de pessoas:")
for i in range(len(pessoas)):
    print(f'{pessoas[i][0]} pesa {pessoas[i][1]}KG')
