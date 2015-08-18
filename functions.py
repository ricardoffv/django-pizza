pedidos = []

#None = falso
def addpedido(nome, sabor, observacao=None):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao
    return pedido

pedidos.append(addpedido('mario', 'pepperoni'))
pedidos.append(addpedido('marco', 'portuguesa', 'dobro de cebola'))

for pedido in pedidos:
    template = 'Nome: {nome}\nSabor {sabor}'
    print(template.format(**pedido)) #expansao do dicionario para a quantidade correta dos argumentos
    if pedido['observacao']:
        print('Observacao: {}'.format(pedido['observacao']))
    print("-"*20)
