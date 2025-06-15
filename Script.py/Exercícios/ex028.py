import time
from random import randint
while True:
 computador = randint(0,5)
 print('-=-' *20)
 print('Estou pensando em umm número de 0 a 5, tente adivinhar!')
 print('-=-' *20)
 jogador = int(input('Digite um número: ')) 
 if jogador > 5:
    print('número alto demais!')
    break
 if jogador != computador:
    print(f'Você errou! O número que eu escolhi foi {computador:^-3}')
 else: 
   print(f'Parabéns! Você acertou!')
   time.sleep(3)
   break
