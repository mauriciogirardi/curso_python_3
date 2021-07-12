import csv

create_order = open('files/menu.csv', 'w', newline='', encoding='utf-8')
order = csv.writer(create_order, delimiter=';')

header = ['Sabor', 'Valor', 'Status']
order.writerow(header)

order_1 = ['Queijo', '5.50', 'Disponevel']
order.writerow(order_1)

order.writerow(['Frango', '7.00', 'Disponevel'])
order.writerow(['Carne Seca', '10.50', 'Disponevel'])
create_order.close()


open_file = open('files/menu.csv', 'r')
file_csv = csv.reader(open_file, delimiter=";")

for [sabor, valor, status] in file_csv:
    print(f'{sabor} | {valor} | {status}')
open_file.close()
