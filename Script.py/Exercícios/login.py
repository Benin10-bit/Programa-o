import json
import os
import time
import re

caminho = 'arquivo.json'
acesso = []

def loadUser():
    if not os.path.exists(caminho) or 0.1< os.path.getsize(caminho) >= 0:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        signIn()
    else:
        login()

def saveUser(usuario):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(usuario, arquivo, indent=4, ensure_ascii=False)

def validPassword(passw):
    if len(passw) < 8:
        return False, "A senha precisa de mais de 8 caracteres"
    
    if not re.search(r"[A-Z]", passw):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r"[a-z]", passw):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r"[0-9]", passw):
        return False, "A senha deve conter pelo menos um número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", passw):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, "Senha válida!"

def signIn():
    user = input('Cadastre o usuário: ')
    password = input('Cadastre sua senha: ')

    while True:
        valid, msg = validPassword(password)

        if valid:
            users = {'Usuário': user, 'Senha': password}
            acesso.append(users)
            saveUser(acesso)
            break
        else:
            print(f'Senha inválida.{msg}\nTente novamente.\n')
            signIn()

    print('Cadastro concluído com sucesso! Faça o Login')
    login()


def login():
    usu = input('Digite o seu Usuário: ').lower().strip()
    psw = input('Digite sua senha: ').lower().strip()

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    foundUser = False
    for user in dados:
        if user['Usuario'] == usu & user['Senha'] == psw:
            foundUser = True
            break
    
    if foundUser == True:
        print('Usuário encontrado, seja bem vindo!')
        time.sleep(3)
    else:
        print('Usuário ou senha incorretos, tente novamente')
        login()

if __name__ == '__main__':
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            try:
                acesso = json.load(arquivo)
            except json.JSONDecodeError:
                acesso = []
    else:
        acesso = []

    loadUser()