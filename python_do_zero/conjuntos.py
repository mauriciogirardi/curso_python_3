order_day1 = [
    {'customer': 'Mauricio', 'pastel': 'Queijo'},
    {'customer': 'Josiana', 'pastel': 'Camarão'},
    {'customer': 'Jose', 'pastel': 'Calabresa'},
    {'customer': 'Julia', 'pastel': 'Carde Seca'},
    {'customer': 'Afonso', 'pastel': 'Frango'},
    {'customer': 'Jose', 'pastel': 'Queijo'},
]

order_day2 = [
    {'customer': 'Julio', 'pastel': 'Pizza'},
    {'customer': 'Lucas', 'pastel': 'Camarão'},
    {'customer': 'Carlos', 'pastel': 'Calabresa'},
    {'customer': 'Barbara', 'pastel': 'Carde Seca'},
    {'customer': 'Jose', 'pastel': 'Frango'},
    {'customer': 'Julia', 'pastel': 'Queijo'},
]

customer_day_1 = set()
for order in order_day1:
    customer_day_1.add(order['customer'])
print('Dia 1: ', customer_day_1)

customer_day_2 = set()
for order in order_day2:
    customer_day_2.add(order['customer'])
print('Dia 2', customer_day_2)

all_customer = customer_day_1 | customer_day_2
print('Todos os cliente: ', all_customer)

customer_buy_all_days = customer_day_1.intersection(customer_day_2)
print(customer_buy_all_days)
