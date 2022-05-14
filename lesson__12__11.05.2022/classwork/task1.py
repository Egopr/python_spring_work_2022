#todo: Реализовать декоратор который подсчитывает время выполнения функции.
# Для этого необходимо взять время до начала запуска функции и после ее окончания.
# Проверить декоратор для различного рода алгоритмов сортировок на большом наборе данных.
import time
# start= time.time()
# end = time.time()
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]
def decor_sort(func):
    def wrapper(name):
        start = time.time()
        func(name)
        end = time.time()
        print((end-start)*10e6)
    return wrapper

@decor_sort
def insertion_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i-1
        while j >=0 and key > mas[j] :
            mas[j+1] = mas[j]
            j -= 1
        mas[j+1] = key

insertion_sort(A)

