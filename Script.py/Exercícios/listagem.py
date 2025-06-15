def lista(num):
    digitos = []

    while num > 0:
        digitos.append(num % 10)
        num = num // 10

    digitos.sort()
    return digitos

print('Escolha um conjunto de números que vai retornar uma lista:')
num = int(input(''))

resultado = lista(num)

print(resultado)
