name = 'Mauricio Girardi'
age = 33
height = 1.70

"""
    %d - Número inteiro
    %f - Número fracionário
    %s - String
    
    'Meu nome é {}'.format(Maurcio)
"""


print('========== format ===========')
print('Meu nome é {} tenho {} anos e {:.2f} de altura'.format(name, age, height))
print(' ')

print('========== %s ===========')
print('Meu nome é %s tenho %s anos e %.2f de altura' % (name, age, height))
print(' ')

print('========== %d ===========')
print('%d de altura' % height)
print('%.3d de altura' % height)
print(' ')

print('========== f-string ===========')
print(f'Meu nome é {name} tenho {age} anos e {height:.2f} de altura')
print(' ')
