"""
Serializar
    è o processo de transformar objetos em JSON
    métodos:
        dump() - Irá transformar o objeto em py para escrever em um aquivo json,
        dumps() - Irá transformar o objeto em py para uma string em formato json
        utilizado para enviar um dados JSON para uma API por exemplo
Deserializar
    é o processo de transformar JSON para objetos
    métodos:
        load() - Irá transformar um objeto JSON para objeto py utilizado para ler arquivos JSON
        loads() - Irá transformar um objeto JSON para objeto py possibilitando manipular em py
"""

import json

my_orders = {
    'estabelecimento': 'Pastelaria DevOps',
    'orders': [
        {'customer': 'Mauricio Girardi', 'price': 12.50},
        {'customer': 'Josiana Lima Girardi', 'price': 32.50},
        {'customer': 'Luana Prado', 'price': 65.00},
    ]
}

# Serializar
json_data = json.dumps(my_orders, indent=4)
print(json_data)

with open('files/my_orders.json', 'w') as file:
    json.dump(my_orders, file, indent=2)

# Deserializar
with open('files/my_orders.json') as file:
    json_order = json.load(file)

print(type(json_order))
print(json_order)

json_order_string = '{"estabelecimento": "Pastelaria DevOps","orders": [{"customer": "Mauricio Girardi","price": 12.5},{"customer": "Josiana Lima Girardi","price": 32.5}]}'

json_string = json.loads(json_order_string)
print(json_string)