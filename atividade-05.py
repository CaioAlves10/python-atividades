login = input('Usuário: ')
senha = input('Senha: ')

if login == 'Senac' and len(senha) >= 6:
    print('Acesso liberado')
else:
    print('Usuário inválido ou senha com caracteres insuficientes (min. 6).')