"""
    .insert(0, 'Frango') add um novo elemento na lista com base do index passado
    .append('Frando') add um novo elemento na lista no final
    .remove('Frango') remove o promeiro elemento que achar com o msm nome
    .count('Frango') conta quando elemento tem
    .pop(4) remove o index passado ou se não passar nada ele remove sempre o ultimo da lista
    sorted(LISTA, key=str.lower)  lista em ordem alfavetica
    len()  pegamdo o tamanho da lista
    sum() soma o total de uma lista de numero
    max() pega o maior numero da lista
    min() pega o menor numero da lista
    menu[0] = 'meat' alterando um valor da lista
"""

menu = ['carne', 'queijo', 'frango', 'calabresa']
print('LISTA: ', menu)

menu[0] = 'meat'
print('LISTA: ', menu)
print(f'Tamanho da lista {len(menu)}')

new_menu = ['Chocolate Preto', 'Chocolate Branco', 'Abaicaxi', 'Abaicaxi', 'Abaicaxi']

new_menu.remove('Abaicaxi')
new_menu.pop()

print(new_menu)
print(sorted(new_menu, key=str.lower))
print(new_menu.count('Abaicaxi'))

numeros = list(range(1, 11))

print(numeros)
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(f'{sum(numeros) / len(numeros):.2f}%')

