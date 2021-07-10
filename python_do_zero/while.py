"""
0 - close
1 - open
"""

print(22 * '=')
print('Welcome to the bakery, make your order')
print(22 * '=')

status = 1

"""
while status == 1:
    order = input('What flavor of pastel do you want? ')
    print(f'Your flavor, {order}')
    status = int(input('Enter 1 to accept the order and 0 to close: '))
"""

count = 0
while count < 4:
    order = input('What flavor of pastel do you want? ')
    print(f'Your flavor, {order}')
    count += 1

print(f'You have {count} orders')
