while True:
    # Solicita os números e a operação
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    o1 = input('Escolha a operação (+, -, *, /,**): ')

    # Realiza a operação de acordo com a escolha
    if o1 == '+':
        print(f'O resultado de {n1} + {n2} é: {n1 + n2}')
    elif o1 == '-':
        print(f'O resultado de {n1} - {n2} é: {n1 - n2}')
    elif o1 == '*':
        print(f'O resultado de {n1} * {n2} é: {n1 * n2}')
    elif o1 == '/':
        # Verifica se o divisor é zero
        if n2 == 0:
            print('Não é possível dividir por 0!')
        else:
            print(f'O resultado de {n1} / {n2} é: {n1 / n2}')
    elif o1 == '**':
        raizQ = n1**(1/n2)
        print(raizQ)

    # Pergunta se o usuário deseja continuar
    continuar = input('Você deseja continuar? (s/n):')
    if continuar.lower() != 's':
        print('saindo do programa')
        import time
        time.sleep(3)
        break
