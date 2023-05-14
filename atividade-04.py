salario = float(input('Salário: '))

if salario >= 1500.00 and salario <= 1750.00:
    print('Cargo: auxiliar de limpeza')

elif salario > 1750.00 and salario <= 2000.00:
    print('Cargo: auxiliar administrativo')

elif salario >= 2001.00 and salario <= 3500.00:
    print('Cargo: supervisor')

elif salario >= 3501.00 and salario <= 5000.00:
    print('Cargo: programador')

elif salario > 5000.00:
    print('Cargo: sócio da empresa')

else:
    print('Cargo não localizado na empresa')