senha = int(input('Digite a senha: '))

if senha == 2021:
    print('=====Comprovante de pagamento=====')
    preco = float(input('Digite o preço do produto: '))
    quant = int(input('Informe a quantidade: '))
    total = preco * quant
    print('..................................')

    if total > 200:
        desconto = total * (10 / 100)
        preco_final = total - desconto
        print(f'Você tem direito a 10% de desconto')
    else:
        desconto = total * (5 / 100)
        preco_final = total - desconto
        print(f'Você tem direito a 5% de desconto')

    print(f'Total: {total:.2f}')
    print(f'Desconto: {desconto:.2f}')
    print(f'Total a pagar: {preco_final:.2f}')
    print('...........Volte sempre...........')
    metodo_pagamento = int(input('Método de pagamento: [1] dinheiro [2] débito [3] crédito [4] pix: '))

    if metodo_pagamento == 1:
        print('==> Pagamento em dinheiro')
        print(f'Troco: {desconto:.2f}')
    elif metodo_pagamento == 2:
        print('==> Pagamento no débito')
    elif metodo_pagamento == 3:
        print('==> Pagamento no crédito')
    elif metodo_pagamento == 4:
        print('==> Pagamento no pix')
    else:
         print('Opção inválida')

    print(f'Valor pago: {total:.2f}')
else:
    print('Acesso inválido')