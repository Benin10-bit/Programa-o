def numPerfeito(num):
    divisores = []
    for d in range(1,num):
        if num % d == 0:
            divisores.append(d)
    soma = sum(divisores)

    if soma != num:
        return False
    else:
        return True
    
print('Escolha um número para verificar se é perfeito')
num = int(input(''))

resultado = numPerfeito(num)

print(resultado)