def palindromo(frase:str) -> bool:

    frase = frase.replace(' ','').lower()

    return frase == frase[::-1]

print('Escolha uma frase:')
sla =  input('')

results = palindromo(sla)
print(results)