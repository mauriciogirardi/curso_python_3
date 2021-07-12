import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Creando um banco de dados com o nome produtos
create_table = """
    CREATE TABLE IF NOT EXISTS "produtos"
    (
        "id"    INTEGER,
        "nome"  TEXT,
        "preco" TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
"""
cursor.execute(create_table)

products = [
    ('Queijo', 6.00),
    ('Frango', 8.00),
    ('Palmito', 5.50),
    ('Carne Seca', 11.50),
    ('Calabresa', 6.00),
]

# Inserindo valores dentro do banco de dados produtos
# cursor.executemany('INSERT INTO produtos (nome, preco) values (?,?)', products)

# Fazendo uma atualização de  um valor
update = 'update produtos set nome = ? where id=?'
name = ('Bacon Com Frango', 10)
cursor.execute(update, name)

# Achando um valor especifico no bando de dados produtos
find_product = 'select * from produtos where id=1'
cursor.execute(find_product)
product = cursor.fetchone()
print('Find: ', product)

# Deletando valor no bando de dado
delete = 'delete from produtos where id=?'
cursor.execute(delete, '4')

# Pegando valores no banco de dados produtos
select = 'select * from produtos'
cursor.execute(select)

# result_one = cursor.fetchone()
# result_many = cursor.fetchmany(2)

result = cursor.fetchall()
for [index, product, price] in result:
    print(index, product, price)

connection.commit()
connection.close()
