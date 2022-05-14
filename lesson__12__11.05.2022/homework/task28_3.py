from datetime import datetime
import time

def now_time():
    data_now = datetime.now()
    t = data_now.strftime("%d.%m.%Y %H:%M")
    return t


def count(func):
    counters = {}

    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)

    return wrapper
@count
def merge_sort (numbers):
    if len(numbers) >1 :
        delen = len(numbers)//2
        a = numbers[:delen] # первая половина массива
        b = numbers [delen:] #вторая половина массива
        merge_sort(a)
        merge_sort(b)

merge_sort()
