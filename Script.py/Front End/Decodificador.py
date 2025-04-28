def decode(word):
    alphabet = ['a', 'b', 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x','y','z']
    reverse = list(reversed(word.lower()))
    coded = [] 
    for p in reverse:
        num = alphabet.index(p)
        coded.append(num)
    
    cod = ''.join(str(num) for num in coded)
    print(cod)

print('Escolha uma palavra para decodificar:')
decode(input(''))
