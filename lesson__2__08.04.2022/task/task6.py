# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

print ('Вычесления уровнения A·x + B = 0 ')
a = int (input('Введите коэфициент A = '))
b = int (input('Введите коэфициент B = '))

if a != 0:
    x = -b/a
    print ('Корень уровнения = ',round(x,2))
else:
    print('не верные исходные данные A = 0')