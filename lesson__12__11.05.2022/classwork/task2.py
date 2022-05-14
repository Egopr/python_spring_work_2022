import time
# start= time.time()
# end = time.time()
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]
def decor_sort(func):
    def wrapper(name):
        start = time.time()
        func(name)
        end = time.time()
        print(end-start)
    return wrapper

@decor_sort
def merge_sort (numbers):
    if len(numbers) >1 :
        delen = len(numbers)//2
        a = numbers[:delen] # первая половина массива
        b = numbers [delen:] #вторая половина массива
        merge_sort(a)
        merge_sort(b)

        i = j = k = 0 # индексы в списках a, b, numbers
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                numbers[k] = a[i]
                i += 1
            else:
                numbers[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            numbers[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            numbers[k] = b[j]
            j += 1
            k += 1

merge_sort(A)
