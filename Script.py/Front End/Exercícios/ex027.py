import time
nome = input('Digite seu nome:')
nomep = nome.split()
print(f'Seu primeiro nome é {nomep[0]}')
print(f'Seu último nome é {nomep[len(nomep)-1]}')
time.sleep(3)