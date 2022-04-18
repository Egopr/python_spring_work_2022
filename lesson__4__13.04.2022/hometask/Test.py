words = ["оператор", "переменная", "сортировка"]

letter=input('Введите букву: ')

one_word=words[1]
print(one_word)
shab=['▒','▒','▒','▒','▒','▒','▒','▒','▒','▒']


for i in one_word:
    if i == letter:
        print('Есть')
        j=one_word.index(letter)
        shab[j]=letter
    else:
        print('Нет')
print(shab)