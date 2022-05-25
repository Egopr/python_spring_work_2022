#todo: Реализовать классы DB и Profile

class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     (атрибуты доступа к БД) . Метод возвращает соединение.'''
    __init__(self, dbname, user, password):
        # В констукторе инициализируем атрибуты доступа к БД
        pass
    def get_connect(self):
        # Метод возвращает соединение к БД
        pass



class Profile:
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''

    # В констукторе инициализируем атрибуты сущности Profile
    __init__(self, login, password, name, surname, age, tel, email):
        pass

    # в аргументе conn передается дискриптор подключения к БД
    def set_profile(self, conn):
        # Добавляет профиль в БД
        pass

    def get_profile(self, conn):
        # Извлекает профиль из БД
        pass





#

