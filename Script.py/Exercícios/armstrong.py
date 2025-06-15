def narcisista(num):
    # Armazena o valor original para comparação
    original = num  
    digitos = []

    # Separa os dígitos do número
    while num > 0:
        n = num % 10
        digitos.append(n)
        num = num // 10  # Remove o último dígito

    # Verifica se a soma dos dígitos elevados à quantidade total de dígitos é igual ao número original
    n = len(digitos)
    if sum(d**n for d in digitos) == original:
        return True
    else:
        return False


# Entrada do usuário
num = int(input('Escolha um número: '))

# Verificação
resultado = narcisista(num)
print(resultado)
