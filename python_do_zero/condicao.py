print("Calculo do IMC".upper())
print(15 * '#')

height = float(input('Digite sua altura: '))
weight = float(input('Digite seu peso: '))
print('-----------------------------------')

imc = weight / (height ** 2)
imc = round(imc, 2)

print(imc)

if imc < 18.5:
    print(f'Sei imc é {imc} e esta na faixa MAGREZA')
elif 18.5 <= imc <= 24.9:
    print(f'Sei imc é {imc} e esta na faixa NORMAL')
elif 25.0 <= imc <= 29.9:
    print(f'Sei imc é {imc} e esta na faixa SOBREPESO')
elif 30.0 <= imc <= 39.9:
    print(f'Sei imc é {imc} e esta na faixa OBESIDADE')
elif imc >= 40:
    print(f'Sei imc é {imc} e esta na faixa OBESIDADE MAX')
else:
    pass


