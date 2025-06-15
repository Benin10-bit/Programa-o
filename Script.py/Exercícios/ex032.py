import time
ano = int(input('Digite o ano: '))
anobi = ano % 4
if anobi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto ')
else:
    print(f'O ano de {ano} não é Bissexto ')
time.sleep(3)