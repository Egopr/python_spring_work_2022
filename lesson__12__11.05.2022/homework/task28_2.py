from datetime import datetime
import time
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]
counter = 0
data=[]

def now_time():
    data_now = datetime.now()
    t = data_now.strftime("%d.%m.%Y %H:%M")
    return t

def save_date(data_all):
    debug = open("debug.log","w+")
    for i in range(len(data_all)):
        debug.writelines(data_all[i])
        if i < (len(data_all) - 1):
            debug.write(', ')
    debug.write('\n')
    debug.close()

def decor_sort(func):
    def wrapper(name):
        func(name)
        global counter, name_func
        counter += 1
        print(now_time())
    return wrapper

@decor_sort
def merge_sort (numbers):
    if len(numbers) >1 :
        delen = len(numbers)//2
        a = numbers[:delen] # первая половина массива
        b = numbers [delen:] #вторая половина массива
        merge_sort(a)
        merge_sort(b)

merge_sort(A)
print (data)
