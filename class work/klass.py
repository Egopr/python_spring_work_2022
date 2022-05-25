import psycopg

class Db:
    def __init__(self,name,user,password):
        self.name = name
        self.user = user
        self.password = password

    def getConnection(self):
        connect = psycopg.connect(dbname=self.name, user=self.user, password=self.password, host="localhost", port='5432')
        return connect

class Profile:
    def __init__(self,login,password,name,age):
        self.login = login
        self.password = password
        self.name = name
        self.age = age
    def getProfile(self,conn,name,age):
        obj = conn.execute("INSERT INTO test (name, age) VALUES (%s, %s)",(self.name, self.age))
        return obj
    def setProfile(self,conn):
        conn.execute()

obj = Db('tgbotgame','egopr','0000')
obj.getConnection()

