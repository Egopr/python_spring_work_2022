from random import randint
words = ["оператор", "переменная", "сортировка"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Изменяемая часть программы",
         "Расположение элементов массива в определенном порядке"]
pohval = ['Вы молодец','Хорошо идёте','Даже так (**,)','Да вы гений','Откуда такие познания']
print('Рады приветствовать на нашей теле передачи\n        !!!ПОЛЕ ЧУДЕС!!!')
print('Внимание Задание на эту игру: ')
r = randint(0,2)
print (desc_[r])
one_word=words[r] #Выделяю слова из списка для сравнения
m=[]
shab=['▒']*len(one_word)
pop=10
schet=0
for i in range(len(one_word)): #создаю список с порядковым номером элементов
    if one_word[i] in one_word[:i]:
        m.append(m[-1] + 1)
    else:
        m.append(one_word.index(one_word[i]))
while schet<9:
    shabl = ''.join(shab) # изменнёный шаблон без пробелов для сравнением с ключём ответа
    shabi = ' '.join(shab) # изменненый шаблон с пробелами для вывода на экран
    if shabl != one_word:
        print(shabi)
        letter = input('Введите букву: ')
        if (letter in one_word) and (len(letter) == 1) : #проверяю условия кореектности введёных данных и присутствия этой буквы в слове
            print('Буква угадана')
            p = randint(0, len(pohval))
            print(pohval[p])
            for i in range(len(m)):
                if one_word[i] in letter:
                    shab[i]=letter
        elif len(letter) != 1:
            print('Вы ввели не один символ')
            pop -= 1
            schet += 1
            print('У вас осталось ', pop, ' попыток !')
        else:
            print('Нет такой буквы')
            pop -= 1
            schet += 1
            print('У вас осталось ', pop, ' попыток !')
    else:
        print('Вы угадали слово!!!')
        print('Мои поздравления')
        break