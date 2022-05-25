#todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
#
#
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||
def transpose(mas):
    change_mat = [[mas[j][i] for j in range(len(mas))] for i in range(len(mas[0]))]
    return print(change_mat)
transpose([[1, 2, 3], [4, 5, 6]])
