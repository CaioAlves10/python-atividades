while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite um segundo número: ")
    operador = input("Informe o operador para o cálculo: ")

    if not (num1.isdigit() and num2.isdigit()):
        print("Informe um número válido.")
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print("Operador inválido")
        continue

    print("O resultado é:", resultado)

    finalizar = input("Deseja finalizar o programa? [s/n]: ")
    if finalizar == 's':
        break