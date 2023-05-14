login = input('Login: ')
senha = int(input('Senha: '))

if login == 'admin' and senha == 321:

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    nota4 = float(input('Nota 4: '))
    faltas = int(input('Faltas: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    carga_hr = 500
    limite_faltas = carga_hr * 0.25

    print('\n=====RESULTADO=====')
    print(f'Aluno(a): {nome}')
    if idade >= 18:
        if media >= 6.0 and faltas < limite_faltas:
            print(f'{nome} aprovado(a) com média {media} e {faltas} faltas')
        elif media >= 6.0 and faltas >= limite_faltas:
            print(f'{nome} vai para conselho de classe com média {media} e {faltas} faltas')
        elif media < 6.0 and faltas >= limite_faltas:
            print(f'{nome} reprovado com média {media} e com {faltas} faltas')
        elif media < 6.0 and faltas < limite_faltas:
            print(f'{nome} está de recuperação com média atual de {media} e {faltas} faltas')
    else:
        print('Você é menor de idade')

else:
    print('Acesso inválido')