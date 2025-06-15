import time

t1 = float(input('Digite o valor do primeiro lado: '))
t2 = float(input('Digite o valor do segundo lado: '))
t3 = float(input('Digite o valor do terceiro lado: '))
if t1 + t2 > t3 and t2 + t3 > t1 and t1 + t3 > t2:
    print('O Triângulo é verdadeiro!')
    time.sleep(3)
else: 
    print('O triângulo não existe!')
    time.sleep(3)