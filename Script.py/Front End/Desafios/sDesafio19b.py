import random
import time
alunos = ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Fernando', 'Gabriela', 'Henrique', 'Isabela', 'João',
          'Karen', 'Lucas', 'Mariana', 'Nathan', 'Olívia', 'Pedro', 'Quésia', 'Rafael', 'Sabrina', 'Thiago',
          'Úrsula', 'Vitor', 'Wellington', 'Xavier', 'Yasmin', 'Zoe', 'Adriana', 'Benício', 'Camila', 'Diego',
          'Esther', 'Felipe', 'Giovana', 'Heitor', 'Ivana', 'Jorge', 'Katia', 'Leonardo', 'Mirela', 'Nelson',
          'Otávio', 'Paula', 'Quintino', 'Rebeca', 'Samuel', 'Tatiane', 'Ubirajara', 'Vanessa', 'William', 'Ximena',
          'Yago', 'Zuleica', 'Alberto', 'Bianca', 'Caio', 'Diana', 'Elias', 'Fabiana', 'Gustavo', 'Heloísa', 'Igor',
          'Juliana', 'Kaique', 'Lorena', 'Matheus', 'Natália', 'Orlando', 'Priscila', 'Quirino', 'Rodrigo', 'Simone',
          'Tadeu', 'Ursula', 'Vicente', 'Wagner', 'Xenia', 'Yuri', 'Zilda', 'André', 'Beatriz', 'César', 'Débora',
          'Eliane', 'Flávio', 'Gabriel', 'Helena', 'Iago', 'Jéssica', 'Keila', 'Luiz', 'Maísa', 'Noemi', 'Osvaldo',
          'Patrícia', 'Quintina', 'Renato', 'Sandra', 'Tatiana', 'Ulisses', 'Vitória', 'Wallace', 'Xisto', 'Yvone'
          ]
while True:
    # randomizando
    escolhido = random.choice(alunos)
    print('sorteando...')
    time.sleep(2)

    # quantidade de letras
    letras = len(escolhido)

    # finalizando
    print(f'O nome sorteado foi {escolhido.center(letras + 2, '-')}')
    time.sleep(0.75)

    # perguntando se quer continuar
    repetir = input('Sortear novamente? (s/n) ').lower().strip()
    if repetir != 's':
        time.sleep(1)
        print('Encerrando...')
        time.sleep(3)
        break
