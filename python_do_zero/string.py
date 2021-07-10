pastel1 = 'CARNE'
pastel2 = 'Carne com queijo'
pastel3 = 'Camarão'
pastel4 = 'Chocolate'
pastel5 = 'Frango'
pastel6 = 'Calabresa da casa'
pastel7 = ' Queijo '


print('========== Substituindo caracteres ===========')
print(pastel2)
print(pastel2.replace('queijo', 'cebola'))
print(pastel2.replace(' ', '-'))
print(' ')

print('========== Caixa alta ===========')
print(pastel3.upper())
print(' ')

print('========== Caixa baixa ===========')
print(pastel1.lower())
print(' ')

print('========== A str começa com e termina com  ===========')
print(pastel6)
print(pastel6.startswith('Calabresa'))
print(pastel6.endswith('casa'))
print(' ')

print('========== Removendo espaço ===========')
print(pastel7.strip())  # remove no começo e final
print(pastel7.lstrip())  # remove no começo
print(pastel7.rstrip())  # remove no final
print(' ')

print('========== Fatiar uma string ===========')
print(pastel5[0])
print(pastel5[-1])
print(pastel5[0:3])
print(pastel5[:3])
print(pastel5[2:])
print(' ')

print('========== Quantidade de caracteres LEN() ===========')
print(pastel5)
print(len(pastel5))
print(' ')

print('========== IN e NOT IN ===========')
print(pastel5)
res = pastel5 in 'Frango'
print(res)
res = 'Frango' not in pastel4
print(res)
print(' ')
