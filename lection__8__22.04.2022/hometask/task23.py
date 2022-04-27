#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
alf='abcdefghijklmnopqrstuvwxyz'
text_free="grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
shif=''
s=0
text_free.replace(" ","")
def get_word(a,s): # а - это буква, s- это сдвиг, функция получает букву и шифрует её со здвигом
    itog = ''
    if a in alf:
        mesto = alf.index(a)
        new_m = mesto - 26 + s
        if a in alf:
            itog += alf[new_m]
        else:
            itog += a
    return itog
while s<26:
    for a in text_free.lower():
        shif += get_word(a, s)
    print('Сдвиг ',s,': ',shif)
    shif=''
    s+=1
