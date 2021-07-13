from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

data = datetime(2021, 7, 13, 18, 50)

print('date now: ', datetime.now())
print('strftime: ', data.strftime('%d/%m/%Y %H:%M'))
print('strptime: ', datetime.strptime('13/07/2021', '%d/%m/%Y'))
print('timestamp: ', data.timestamp())
print('fromtimestamp: ', data.fromtimestamp(1626213000.0))

data_sun = data.strptime('13/07/2021', '%d/%m/%Y')
data_total = data_sun + timedelta(days=5)
print('soma data: ', data.strftime('13/07/2021'), '->',  data_total.strftime('%d/%m/%Y'))

print(' ')
print('================= Calculando data ====================')
date_init = datetime.strptime('13/07/2021 20:00:00', '%d/%m/%Y %H:%M:%S')
date_end = datetime.strptime('15/07/2021 22:00:00', '%d/%m/%Y %H:%M:%S')

dif = date_end - date_init
print(dif)
print(date_init > date_end)

print(' ')
print('================= BR ====================')
setlocale(LC_ALL, '')  # pt_BR.utf-8

date_now = datetime.now()
month_current = int(date_now.strftime('%m'))
date_format = date_now.strftime('%A, %d de %B de %Y')

print(date_format)
print(f'Last day in month {month_current}: ', mdays[month_current])

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
