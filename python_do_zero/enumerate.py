menu = ['Carne', 'Queijo', 'frango', 'Pizza', 'Carne Seca']
numbers = range(1, 11)

for index, flavor in enumerate(menu):
    print(f'[{index}]: {flavor}')

opcao = int(input('Digite o sabor desejado: '))

if 0 <= opcao <= len(menu):
    print(menu[opcao])
else:
    print('Opção inválida!')
