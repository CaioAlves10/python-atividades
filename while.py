user = ''
while user != 'admin':
    user = input('Digite seu usuário: ')
    idade = int(input('Digite sua idade: '))
    while idade < 18:
        idade = int(input('Digite sua idade: '))
print('Acesso permitido')