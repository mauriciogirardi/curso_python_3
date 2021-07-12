"""
Onde:
    file:
        path + nome do arquivo
    mode:
        r = read (padrão) - leitura
        w = write - escrita, sobrescreve o conteúdo se já existir
        a = append - escrita, apenas adiciona ao final do arquivo
        b = bytes - modo binário
"""

file = open('files/orders.txt')
orders = file.readlines()

for order in orders:
    print(order.replace('\n', ''))
file.close()

customers = ['Jose', 'Mauricio', 'Josiana', 'Carlos', 'Gabriel', 'Bruna']
write_file = open('files/customer.txt', 'w')
for customer in customers:
    write_file.write(f'{customer}\n')
write_file.close()
