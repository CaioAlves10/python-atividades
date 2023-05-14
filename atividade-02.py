nome1= 'Guto'
profissao1= 'Desenvolvimento web'
salario1= 3500.00
salario_aumtento1= ((salario1*10)/100)+salario1
anos_trabalho1= 5
experiencia1= anos_trabalho1 > 5

nome2= 'Keila'
profissao2= 'Médica'
salario2= 5400.34
salario_aumtento2= ((salario2*10)/100)+salario2
anos_trabalho2= 6
experiencia2= anos_trabalho2 > 5

nome3= 'João'
profissao3= 'Gestor'
salario3= 3500.50
salario_aumtento3= ((salario3*10)/100)+salario3
anos_trabalho3= 10
experiencia3= anos_trabalho3 > 5

print(f'FUNCIONÁRIO 01 \n'
      f'Nome: {nome1} \n'
      f'Profissão: {profissao1} \n'
      f'Salário: R${salario1:.2f} \n'
      f'Salário com aumento: R${salario_aumtento1:.2f} \n'
      f'Tempo de experiência: {anos_trabalho1} anos \n'
      f'Tem mais de 5 anos de experiência? {experiencia1} \n')

print(f'FUNCIONÁRIO 02 \n'
      f'Nome: {nome2} \n'
      f'Profissão: {profissao2} \n'
      f'Salário: R${salario2:.2f} \n'
      f'Salário com aumento: R${salario_aumtento2:.2f} \n'
      f'Tempo de experiência: {anos_trabalho2} anos \n'
      f'Tem mais de 5 anos de experiência? {experiencia2} \n')

print(f'FUNCIONÁRIO 03 \n'
      f'Nome: {nome3} \n'
      f'Profissão: {profissao3} \n'
      f'Salário: R${salario3:.2f} \n'
      f'Salário com aumento: R${salario_aumtento3:.2f} \n'
      f'Tempo de experiência: {anos_trabalho3} anos \n'
      f'Tem mais de 5 anos de experiência? {experiencia3}')