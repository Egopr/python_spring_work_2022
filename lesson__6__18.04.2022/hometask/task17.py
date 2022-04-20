#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
kol = {
  "banana": 2,
  "apple": 12,
  "orange":6,
  "pear": 2
}
cen=[]
kolvo=[]
proiz=[]
def compute_bill(kol):
  for key, val in prices.items():
    cen.append(val)
  for key, val in kol.items():
    kolvo.append(val)
  for i in range(len(kolvo)):
    proiz.append(cen[i]*kolvo[i])
  return sum(proiz)

print (compute_bill(kol))



