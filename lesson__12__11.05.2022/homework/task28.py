#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import time
from datetime import datetime
# def save_date():
# debug = open("debug.log","w+")
#
#
# debug.close()
def now_time():
    data_now = datetime.now()
    t = data_now.strftime("%d.%m.%Y %H:%M")
    return t

A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]

def decor_sort(func):
    def wrapper(name):
        func(name)
        print(now_time())
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