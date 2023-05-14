#estrutura condicional composta elif

email = input('E-mail: ')
if '@gmail.com' in email or '@outlook.com' in email:
    senha = input('Senha: ')
    if len(senha) >= 8:
        data_venc = input('Informe a data de vencimento: ')
        data_pag = input('Informe a data de pagamento: ')
        if data_pag == data_venc:
            print('Quitado')
        elif data_pag > data_venc:
            print('pago com juros')
        elif data_pag < data_venc:
            print('Pago antes do prazo')
        else:
            print('Pagamento pendente')
    else:
        print('Número de caracteres inválido')
else:
    print('Digite um e-mail válido.')