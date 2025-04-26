
import time
array_cnv = ['KM', 'HM', 'DAM', 'M', 'DM', 'CM', 'MM']
while True:
    # Puxar informações principais
    nmr = float(input('Escreva um valor para conversão: '))
    grz01 = input(
        'Qual a grandeza que correspode este valor? \n-KM- \n-HM- \n-DAM- \n-M- \n-DM- \n-CM- \n-MM\n').strip().upper()
    grz02 = input(
        'Você deseja converter para qual grandeza? \n-KM- \n-HM- \n-DAM- \n-M- \n-DM- \n-CM- \n-MM\n').strip().upper()
# Verificar se entrada é válida
    if grz01 not in array_cnv or grz02 not in array_cnv:
        print('Parâmetro Inválido')
        time.sleep(1)
        continuar = input('Tentar novamnte? (s/n):').lower()
        if continuar != 's':
            print('saindo do programa...')
            time.sleep(3)
            break
        else:
            continue
# Determinar a posição
    p01 = array_cnv.index(grz01)
    p02 = array_cnv.index(grz02)
# Operações
    exp = p02 - p01
    vf = nmr * (10 ** exp)

# Mostrando resultado final
    print(f'O valor final da conversão de {grz01} para {grz02} é {vf:.8f}')
    tg03 = input('Deseja continuar? (s/n) ')
    if tg03.lower() != 's':
        print('fechando...')
        time.sleep(3)
        break
