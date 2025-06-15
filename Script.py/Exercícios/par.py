def par(lista):
    pares = []
    for x in lista:
        if x % 2 == 0:
            pares.append(x)
    print (pares)
    print(f'Existem {len(pares)} números pares na lista :)')

num1 = int(input('De:'))
num2 = int(input('Até:'))

par(range(num1,num2+1))
