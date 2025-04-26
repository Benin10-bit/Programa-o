import time
# Verificação de repetição
resposta = ['s', 'n']
while True:
    # Identificação do Programa
    print('\033[1;36m-=-' * 10)
    print('\033[1;34mCALCULADORA DE EMPRÉSTIMOS\033[m')
    print('\033[1;36m-=-\033[m' * 10)
# Variáveis
    casa = float(input('Qual o valor da casa? '))
    salario = float(input('Qual o seu salário? '))
    anos = float(input('Em quantos anos você vai financiar? '))
# Operações
    parcela = casa / (12 * anos)
    porcentagem = parcela * 100 / salario
# Vai verificar se a parcela é 30% maior que o salário
    if porcentagem >= 30:
        print(f'O empréstimo de R${casa:.2f} foi \033[1;31mNEGADO\033[m. Motivado pelas parcelas divididas em {anos:.1f} anos estarem 30% acima do seu salário de R${salario:.2f}')
        print(f'\033[1;31m{porcentagem:.2f}%\033[m e \033[1;31mR${parcela:.2f}\033[m')
    elif porcentagem < 30:
        print(f'O empréstimo em R${casa:.2f} foi \033[1;32mAPROVADO\033[m. Parabéns!')
        print(f'\033[1;32m{porcentagem:.2f}%\033[m e \033[1;32mR${parcela:.2f}\033[m')
# Pergunta se deseja recomeçar
    repetir = input('Deseja simular outro empréstimo? (s/n)').lower().strip()
    if repetir not in resposta:
        print('\033[1;33mCARÁCTERE INVÁLIDO\033[m')
        repetir = input(
            'Deseja simular outro empréstimo? (s/n)').lower().strip()
    if repetir != 's':
        print('encerrando...')
        time.sleep(3)
        break
