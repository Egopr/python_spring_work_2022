# todo: Шифр Цезаря
alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
shif=''
s=1
def get_word(a,s): # а - это буква, s- это сдвиг, функция получает букву и шифрует её со здвигом
    itog = ''
    if a in alf:
        mesto = alf.index(a)
        new_m = mesto - 32 + s
        if a in alf:
            itog += alf[new_m]
        else:
            itog += a
    return itog

fil_e = open("message.txt", "r+")
while True:
    message = fil_e.readline()
    mes = message.replace(" ", "")
    s+=1
    if not message:
        break
    for a in mes.lower():
        shif += get_word(a, s)
    print(shif)
    shif=''
fil_e.close()