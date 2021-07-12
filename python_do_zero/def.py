EMPRESA = 'MG'


def msg_welcome(name):
    print(f'Seja bem vinda a pastelaria {name} ;)')


def add_order(customer, flavor):
    new_order = f'O {customer} pediu pastel de {flavor}'
    print(new_order)


def imprima_nome():
    name = 'Mauricio'
    print(f'O {name} trabalha na {EMPRESA}')


imprima_nome()

