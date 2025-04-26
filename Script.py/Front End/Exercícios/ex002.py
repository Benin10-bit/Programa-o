import time
ban = ['Gabriel', 'André']
orepetir = ['s', 'n']

while True:
    nome = input('Digite seu nome: ').strip().capitalize()
    # ver quantos caracteres tem o nome
    letras = len(nome)
    # identificar se o input está na lista ban
    if nome in ban:
        print('Usuário banido')
        time.sleep(1.5)
        repetir = input('Tentar novamente? (s/n) ').lower().strip()
        if repetir not in orepetir:
            print('Caráctere inválido')
            time.sleep(0.5)
            repetir = input('Tentar novamente? (s/n) ').lower().strip()
        else:
            if repetir != 's':
                print('encerrando...')
                time.sleep(3)
                break
    # caso o nome não estiver em ban
    else:
        print(f'Seja bem vindo {nome.center(letras+2, '-')}')
        time.sleep(1.5)
        repetir02 = input('Deseja continuar? (s/n)')
        if repetir02 not in orepetir:
            print('Caráctere inválido')
            time.sleep(0.5)
            repetir = input('Tentar novamente? (s/n) ').lower().strip()
        else:
            if repetir02 != 's':
                print('fechando...')
                time.sleep(3)
                break
