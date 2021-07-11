# ()
# Tuplas são imutáveis.
# Ordenadas

order = ('Queijo', 6.00, True)
print(order)

for info in order:
    print(info)

sabor, valor, status = order
print(f'O sabor pedido foi {sabor}, e o valor é R${valor:.2f} reais')
