import pyodbc



class DB:

    def __init__(self,name,server = 'localhost\SQLEXPRESS', driver="SQL Server Native Client 11.0"):
        self.__name = name
        self.__server = server
        self.__driver = driver
        self.__conexion = None
        self.__datos = None

    def connect(self):
        self.__conexion = pyodbc.connect("DRIVER={"+self.__driver+"};"
                                  "Server="+self.__server+";"
                                  "DATABASE="+self.__name+";"
                                  "Trusted_Connection=yes;")
    
    def cursor(self):
        self.__cursor = self.__conexion.cursor()
        
    def query(self,q,v=None):
        if v:
            self.__cursor.execute(q,v)
        else:
            self.__cursor.execute(q)
        
    def commit(self,query):
        esselect = query.count('SELECT')
        if esselect == 0:
            self.__conexion.commit()

    def getData(self,query):
        esselect = query.count('SELECT')
        if esselect > 0:
            self.__datos = self.__cursor.fetchall()

    def close(self):
        self.__conexion.close()

    def run(self,query,values = None):
        self.connect()
        self.cursor()
        self.query(query,values)
        self.commit(query)
        self.getData(query)
        self.close()

        return self.__datos