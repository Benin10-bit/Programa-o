import random
import time

def jokenpo(play):
    moves = ['pedra', 'papel', 'tesoura']
    turn = random.randint(0, 2)
    choice = moves[turn]

    play = play.lower()  # converte uma vez só

    if play not in moves:
        print('Insert a valid option')
        return  # evita continuar com jogada inválida

    print(f'Você escolheu {play}, o computador escolheu {choice}')

    if play == choice:
        print('Draw')
    
    elif play == 'papel':
        if choice == 'pedra':
            print('You win')
        else:
            print('You lose')

    elif play == 'tesoura':
        if choice == 'papel':
            print('You win')
        else:
            print('You lose')

    elif play == 'pedra':
        if choice == 'tesoura':
            print('You win')
        else:
            print('You lose')

urTurn = input('Escolha sua jogada: ')
jokenpo(urTurn)
