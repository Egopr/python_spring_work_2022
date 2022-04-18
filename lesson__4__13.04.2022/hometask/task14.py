#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

mass = [1,2,17,54,34,54,89,2,1,54,2]
m=[]
w=[]
nome = int(input('Введите число = '))
for i in range(len(mass)):
    if mass[i] in mass[:i]:
        m.append(m[-1] + 1)
    else:
        m.append(mass.index(mass[i]))
mk=0
ml=1
for j in range(len(mass)):
    if mass[j] == nome:
        w.append(m[j])
for k in range(len(w)-1):
        for l in  range(k+1,len(w)):
            if abs(w[k]-w[l]) < abs(w[mk]-w[ml]):
                mk = k
                ml = l
mk=w[mk]
ml=w[ml]
print('Массив: ',mass)
print('Для числа ', nome , 'индексы двух ближайших чисел: ', mk,' и ', ml)