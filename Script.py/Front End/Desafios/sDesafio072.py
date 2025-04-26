nextenso =("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",  "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    #Variáveis
    num = int(input('Digite um número inteiro entre 0 e 20: ')) 
    #Atribui a num o valor inteiro entre 0 e 20
    if 0<=num<=20:
        print(f'O número por extenso é {nextenso[num]}')
    else:
        print('insira um número válido')

   
