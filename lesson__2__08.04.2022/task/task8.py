# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

print ('Введите значения переменных')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
(a,b,c) = (b,c,a)
print ('Изменёные значения :')
print ('a = ', a,' b = ',b,' c = ',c)
