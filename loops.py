pedidos = [
    {
        'nome': 'mario',
        'sabor': 'portuguesa'
    },
    {
        'nome': 'Marco',
        'sabor': 'presunto'
    }
]

for pedido in pedidos:
    s = 'Nome: {}\nSabor: {}'
    print(s.format(pedido['nome'], pedido['sabor']))    
    #print('Nome: {0}\nSabor {1}'.format(pedido['nome'], pedido['sabor']))
