#isnumeric() - verifica se o valor digitado é número

num1 = input('Digite um número: ')
if num1.isnumeric():
    print('Valor aceito')
else:
    print('Você precisa digitar um número')
print('')

#isdigit() - verifica se o valor digitado é um número inteiro ou flutuante
num2 = input('Digite um número: ')
if num2.isdigit():
    print('É um número inteiro')
else:
    print('É um número fracionado')
print('')

#upper - converte a string para maiúsculo
sexo = input('Digite seu sexo: ')
print(f'Seu sexo é {sexo.upper()}')
print('')

#lower - converte a string para minúsculo
email = input('Digite seu email: ')
print(f'Seu e-mail: {email.lower()}')
print('')

#count - retorna a quantidade de vezes que um elemento é exibido em uma lista
alunos = ['Lucas', 'Ana', 'Jão', 'Lucas', 'Rafa'].count('Lucas')
if alunos >= 1:
    print(f'O nome "Lucas" REPITIU na lista {alunos} vezes' )
else:
    print('O nome solicitado não está cadastrado')