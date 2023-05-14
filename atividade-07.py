senha = 321
for i in range(1, 4):
    s = int(input('Senha: '))
    if senha == s:
        print('Acesso permitido')
        exit()
    else:
        print('Senha incorreta, tente novamente')
        continue
print('Senha bloqueada')