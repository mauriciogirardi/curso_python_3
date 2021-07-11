menu = ['Carne', 'Queijo', 'frango', 'Pizza', 'Carne Seca']
numbers = range(1, 11)

# for flavor in menu:
#   print(flavor)

number_impar = []
number_par = []

for number in numbers:
    if number % 2 == 0:
        number_par.append(number)
    else:
        number_impar.append(number)

print('Números Impar: ', number_impar)
print('Números Par: ', number_par)
