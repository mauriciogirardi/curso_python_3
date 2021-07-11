order = {'sabor': 'queijo', 'valor': 12.00, 'status': True}


print(order)
print(order.get('sabor'))
print(order.get('quantidade'))

keys = order.keys()
print(keys)

values = order.values()
print(values)

dict_values = order.items()
print(dict_values)

for key, value in dict_values:
    print(key, value)
