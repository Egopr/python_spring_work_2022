# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

date = int(input('Введите год <положительное целое>: '))

if date >= 1000:
    god = str(date)
    buff = god[0:2]
    god = int(buff)+1
    print(god, ' Столетие')
elif date<1000 and date >=0:
    god = str(date)
    buff = god[0:1]
    god = int(buff) + 1
    print(god, ' Столетие')
else:
    print('Не корректная дата')
