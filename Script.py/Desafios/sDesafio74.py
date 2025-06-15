from random import randint
validação = ('s','n')
while True:
    num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
    print(f'Os números aleatórios são {num}')
    print(f'O maior número aleatório é {max(num)}')
    print(f'O menor número aleatório é {min(num)}')
    #Pergunta se quer sortear denovo?
    repetir = input('Deseja sortear dnv? (s/n) ').strip().lower()
    if repetir != 's':
        print('Fechando...')
        print('Fechando...')
        print('Fechando...')
        print('Fechando...')
        print('Fechando...')
        break
    #Verifica se o input é válido
    if repetir not in validação:
        print('Insira um Caractere válido ')
        repetir = input('Deseja sortear dnv? (s/n) ').strip().lower()
    
