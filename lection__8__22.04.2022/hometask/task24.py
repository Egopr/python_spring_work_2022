#todo: Числа в буквы
'''
Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
'''

alf='abcdefghijklmnopqrstuvwxyz'
chisla = [8,5,12,12,15]
word=''
#stroka=[]
in_stroka= input("Введите числа: ")
stro=in_stroka.split(" ")
print(stro)



print (stroka)
for i in stroka:
    word+=alf[i-1]
print(word)