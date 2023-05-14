nome= 'Anna'
idade= 10
altura= 1.70
trabalha= True
maior_idade= idade >= 18
bonificacao= 123.044

print(nome, 'tem', idade, 'anos e sua altura é', altura, 'cm. Ela trabalha?', trabalha)
print(f'Anna tem {idade} anos e sua altura é {altura} cm. Ela trabalha? {trabalha}')

print('É maior de idade?', maior_idade)
print(f'Bonificação: R${bonificacao:.2f}')
