#todo: Найти сумму элементов матрицы,
# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>>
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423
matrix = [[1, 2, 3], [4, 5, 6]]
def msum(m):
    summ = sum ([col for row in m for col in row])
    return print(summ)
msum (matrix)
