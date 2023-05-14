for i in range(1, 5):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print(f'{i}ª idade cadastrada: {idade} anos')
    else:
        print('Idade não permitida')
        continue