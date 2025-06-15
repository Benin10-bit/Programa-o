def subtracao(frase: str, trecho: str) -> str:
    # Remove o trecho e divide a frase em uma lista de palavras
    resultado = frase.replace(trecho, '').split()
    
    # Junta a lista com um único espaço entre as palavras e retorna
    return ' '.join(resultado)

# Solicita a entrada do usuário
frase = input('Qual a frase completa? ')
trecho = input('Qual parte você quer remover? ')

# Chama a função e imprime o resultado
resultado = subtracao(frase, trecho)
print(resultado)
