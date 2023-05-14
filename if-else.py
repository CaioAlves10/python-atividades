nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('\n=====RESULTADO=====')
print(f'Aluno(a): {nome}')
if idade >= 18:
    if media >= 60:
        print(f'{nome} está aprovado(a) com média {media}')
    else:
        print(f'{nome} está reprovado(a) com média {media}')
else:
    print('Você é menor de idade')