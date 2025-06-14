import json
import os
import time

acesso = []  

caminho = 'usuarios.json'

def salvarUsuarios(usuarios):
    
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def carregarUsuarios():
    if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
        cadastro()
    else:
        login()

def cadastro():
    nome = input('Digite o seu usuário: ').lower().strip()
    senha = input('Digite sua senha: ').lower().strip()

    usuario = {"Usuário": nome, "Senha": senha}

    for user in acesso:
        if user["Usuário"] == nome:
            print("Usuário já existe! Tente fazer login.")
            login()
            return

    acesso.append(usuario)

    salvarUsuarios(acesso)  

    print('PARABÉNS! Conta criada com sucesso! Agora faça login')
    login()

def login():
    usu = input('Usuário: ').lower().strip()
    psw = input('Senha: ').lower().strip()

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    usuario_encontrado = False
    for user in dados:
        if user["Usuário"] == usu and user["Senha"] == psw:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        print(f'Usuário encontrado! Bem-vindo de volta {usu}')
        time.sleep(3)
    else:
        print('Usuário e senha incorretos, tente novamente')
        login()

if __name__ == '__main__':
    if os.path.exists(caminho) and os.path.getsize(caminho) > 0:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            try:
                acesso = json.load(arquivo)
            except json.JSONDecodeError:
                acesso = []
    carregarUsuarios()
