media = 0
for i in range(1,5):
    notas = float(input(f'Digite a {i}º nota: '))
    media += notas/4
print(f'Média: {media}')
if media >= 70:
    print('Aluno(a) aprovado(a)')
elif media >= 60 and media < 70:
    print('Aluno(a) em recuperação')
else:
    print('Aluno reprovado')