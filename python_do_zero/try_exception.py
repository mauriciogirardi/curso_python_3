try:
    with open('files/orders.txt') as file:
        print('Arquivo aberto com sucesso')
except Exception as err:
    print(err)
    print('Falha ao acessar o arquivo')

print('seguindo')