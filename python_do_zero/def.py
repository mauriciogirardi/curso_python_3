EMPRESA = 'MG'


def msg_welcome(name):
    print(f'Seja bem vinda a pastelaria {name} ;)')


def add_order(customer, flavor):
    new_order = f'O {customer} pediu pastel de {flavor}'
    print(new_order)


def imprima_nome():
    name = 'Mauricio'
    print(f'O {name} trabalha na {EMPRESA}')


def imprime_valores(sabor, status="Disponivel"):
    print(f'O sabor é: {sabor} e o status é: {status}')

