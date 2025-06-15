arrta = ['s','n']
while True:
 #Input
 numero = int(input('Me diga um número qualquer: '))
 #Pega o resto da divisão por 2
 par_ou_impar = numero % 2
 #Identifica se o resto é diferente de zero
 if par_ou_impar != 0:
    print(f'O número {numero} é Ímpar')
 else:
    print(f'O número {numero} é Par')
 #Pergunta se quer continuar
 ta = input('Deseja continuar? (s/n) ').lower().strip()
 if ta not in arrta:
   print('Caráctere Inválido')
   ta = input('Deseja continuar? (s/n) ').lower().strip()
 if ta != 's':
   print('Encerrando...')
   print('Encerrando...')
   print('Encerrando...')
   print('Encerrando...')
   print('Encerrando...')
   print('Encerrando...')
   print('Encerrando...')
   break
