import random
import time
alunos = ['Maria', 'João', 'Clara', 'José']
while True:
    # pegando um número aleatório

    anmr = random.randint(0, 3)
    print('Sorteando Número...')

    # identificando a str que corresponde ao número

    aluno = alunos[anmr]

    # lendo a quantidade de letras

    letras = len(aluno)

    # Finalizando

    time.sleep(2)
    print(f'O sorteado foi {aluno.center(letras + 2, '-')}')

    # Perguntando se quer sortear dnv

    time.sleep(0.75)
    tn = input('Deseja sortear novamente? (s/n)').lower().strip()
    if tn != 's':
        print('Encerrando...')
        time.sleep(3)
        break
