#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
# Т.е. в каждой строке через пробел записаны числа.
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

file = open('filik.txt','r')
mas = file.readlines()
print(mas)
file.close()

