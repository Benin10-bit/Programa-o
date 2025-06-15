import time
array = {'Maria', 'Pedro', 'Caio'}
while True:
    nome = input('Nome? ').capitalize().strip()
    qletras = int(len(nome))
    if nome in array:
        print('acesso concedido')
        time.sleep(0.55)
        print(f'Bem Vindo {nome.center(qletras + 2, '-')}')
        time.sleep(0.88)
        break
    else:
        print(f'{nome}, seu ladrão safado!')
        time.sleep(0.5)
        print('Triangulando localização...')
        time.sleep(1.5)
        print('Enviando Tropas de Operações Especiais')
        time.sleep(0.75)
        break
