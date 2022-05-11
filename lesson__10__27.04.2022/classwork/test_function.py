import her.serializer as ser
import her.deserializer as des



list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]


list_tow = ['Над Италией обширной',
'Солнце светит с наглой мордой',
'А под лестницей, в каморке',
'Папа Карло режет бревна.',
'(Хочет сделать буратино,',
'Что скажу я вам не проще,',
'Чем пиздою улыбаться)',
'Сделал уши из картона',
'Нос из щепки свилеватой',
'Приспособил под мудя',
'Два червивых желудя',
'А потом зевнув от скуки',
'Под елду он точит руки.']


ser.to_yaml(list_tow,"as.yml")
print(des.from_yaml('as.yml'))


