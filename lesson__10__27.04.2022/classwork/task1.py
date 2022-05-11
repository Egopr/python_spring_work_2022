#todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.


#todo: Заданы два списка. Необходимо их сериализовать в один файл.
import pickle
list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]


fd = open("data.pkl","w+b")
pickle.dump(list_one+list_two,fd,pickle.HIGHEST_PROTOCOL)
fd.close()

with open ("data.pkl","rb") as f:
    obj = pickle.load(f)
print (obj)
