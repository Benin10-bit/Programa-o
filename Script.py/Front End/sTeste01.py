nome = input('Digite uma frase: ').strip().lower().replace(' ', '')
print(f'A letra A apareceu {nome.count('a')}')
print(f'A primeira letra A apareceu na posição {nome.find('a')+1}')
print(f'A última letra A apareceu na posição {nome.rfind('a')+1}')