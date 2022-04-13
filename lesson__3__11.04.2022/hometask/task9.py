# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.
"""""
x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))

if x>y:
    if x>z:
        print('Наибольшее число ',x)
    else:
        if z>y:
            print('Наибольшее число ',z)
        else:
            print ('Наибольшее число ',y)
else:
    if y>z:
        print('Наибольшее число ',y)
    else:
        print('Наибольшее число ',z)
"""
x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))

if x>y and x>z:
    print('Наибольшее число ', x)
elif y>x and y>z:
    print('Наибольшее число ', y)
else:
    print('Наибольшее число ', z)
