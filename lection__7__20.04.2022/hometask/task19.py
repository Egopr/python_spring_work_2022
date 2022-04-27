#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.
'''
algo = open("algoritm.csv","w+")
for i in range(len(algoritm)):
    algo.writelines(algoritm[i])
    if i<(len(algoritm)-1):
        algo.write(', ')
algo.close()
'''
algo = open("algoritm.csv","w+")
for i in range(len(algoritm)):
    algo.write(str(i+1))
    algo.write(',')
    algo.write(algoritm[i]+'\n')
algo.close()