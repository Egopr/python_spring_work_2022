#todo: Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame ({
    'Страна': ['Россия', 'Казахстан', 'Украина', 'Белоруссия', 'Узбекистан'],
    '2017 год': [1665, 179, 131, 60, 50],
    '2018 год': [1702, 182, 154, 63, 58],
}, index=['RU', 'KZ', 'UA', 'BY', 'UZ'] )
#print(df)
# with open("data.csv","r+") as f:
#     f.write('Hello, word!\n')
df.to_csv("data.csv")

vet_csv = pd.read_csv("data.csv")
print(vet_csv)

df.plot(kind='barh', y='2018 год', color='blue')
plt.show()
