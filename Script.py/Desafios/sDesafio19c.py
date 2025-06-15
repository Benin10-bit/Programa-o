import time
import random
#Arrays
orepetir = ['s','n']
arr_nome = ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Fernando', 'Gabriela', 'Henrique', 'Isabela', 'João',
        'Karen', 'Lucas', 'Mariana', 'Nathan', 'Olívia', 'Pedro', 'Quésia', 'Rafael', 'Sabrina', 'Thiago',
        'Úrsula', 'Vitor', 'Wellington', 'Xavier', 'Yasmin', 'Zoe', 'Adriana', 'Benício', 'Camila', 'Diego',
        'Esther', 'Felipe', 'Giovana', 'Heitor', 'Ivana', 'Jorge', 'Katia', 'Leonardo', 'Mirela', 'Nelson',
        'Otávio', 'Paula', 'Quintino', 'Rebeca', 'Samuel', 'Tatiane', 'Ubirajara', 'Vanessa', 'William', 'Ximena',
        'Yago', 'Zuleica', 'Alberto', 'Bianca', 'Caio', 'Diana', 'Elias', 'Fabiana', 'Gustavo', 'Heloísa', 'Igor',
        'Juliana', 'Kaique', 'Lorena', 'Matheus', 'Natália', 'Orlando', 'Priscila', 'Quirino', 'Rodrigo', 'Simone',
        'Tadeu', 'Ursula', 'Vicente', 'Wagner', 'Xenia', 'Yuri', 'Zilda', 'André', 'Beatriz', 'César', 'Débora',
        'Eliane', 'Flávio', 'Gabriel', 'Helena', 'Iago', 'Jéssica', 'Keila', 'Luiz', 'Maísa', 'Noemi', 'Osvaldo',
        'Patrícia', 'Quintina', 'Renato', 'Sandra', 'Tatiana', 'Ulisses', 'Vitória', 'Wallace', 'Xisto', 'Yvone']

arr_sobrenome = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Lima', 'Carvalho', 'Gomes', 'Ribeiro', 'Almeida',
             'Costa', 'Fernandes', 'Rodrigues', 'Martins', 'Barbosa', 'Freitas', 'Batista', 'Araújo', 'Mendes', 'Nunes',
             'Machado', 'Dias', 'Teixeira', 'Moreira', 'Correia', 'Moura', 'Castro', 'Campos', 'Guimarães', 'Cardoso',
             'Figueiredo', 'Andrade', 'Vieira', 'Coelho', 'Cavalcante', 'Bezerra', 'Monteiro', 'Barros', 'Assis', 'Borges',
             'Rezende', 'Tavares', 'Sales', 'Xavier', 'Braga', 'Moraes', 'Duarte', 'Neves', 'Pinheiro', 'Pinto',
             'Leite', 'Viana', 'Ramos', 'Siqueira', 'Queiroz', 'Cunha', 'Lacerda', 'Fonseca', 'Ferreira', 'Mello',
             'Amaral', 'Torres', 'Macedo', 'Farias', 'Chaves', 'Dantas', 'Drumond', 'Domingues', 'Prado', 'Lopes',
             'Barreto', 'Serra', 'Peixoto', 'Vasconcelos', 'Teles', 'Bittencourt', 'Aguiar', 'Accioli', 'Brandão', 'Souto',
             'Meireles', 'Caldas', 'Alencar', 'Bicalho', 'Menezes', 'Rangel', 'Seabra', 'Novaes', 'Beltrão', 'Noronha',
             'Toledo', 'Brum', 'Mussi', 'Goulart', 'Paixão', 'Cervantes', 'Furtado', 'Villela', 'Portela', 'Brasil']
while True:
    #Aleatorizando o nome
    nome = random.choice(arr_nome)
    sobrenome = random.choice(arr_sobrenome)
    print('Sorteando o nome...')
    #Escrevendo o resultado
    time.sleep(1.5)
    print('Calculando compatibilidade entre o nome e o sobrenome...')
    time.sleep(1.5)
    print('Nome pronto!')
    print(f'O nome de um brasileiro aleatório é {nome} {sobrenome}')
    #Perguntando se deseja sortear denovo
    time.sleep(1.75)
    repetir = input('Deseja sortear denovo? (s/n) ').strip().lower()
    if repetir not in orepetir:
        print('Caráctere inválido')
        time.sleep(0.5)
        rptr = input('Tentar novamente? (s/n) ')
        if rptr != 's':
            print('Encerrando...')
            time.sleep(3)
            break
        elif rptr == 's':
            repetir = input('Deseja sortear denovo? (s/n) ').strip().lower()
    if repetir != 's':
        print('Encerrando...')
        time.sleep(3)
        break