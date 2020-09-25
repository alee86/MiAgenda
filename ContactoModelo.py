from MiAgendaDB import DB 


class Persona:
    __DB = DB(name = 'MiAgendaDB')
    __tableName = 'contacto'

    def __init__(self, email = None, nombre = None, telefono = None, id = None):
        self.__id = id
        self.__telefono = telefono
        self.__nombre = nombre
        self.__email = email


    @classmethod
    def mostrar(cls):
        query = 'SELECT * FROM '+Persona.__tableName
        return Persona.__DB.run(query)

    @classmethod
    def buscar(cls, nombre):
        query = 'SELECT * FROM '+Persona.__tableName+' WHERE nombre = ?'
        values = (nombre)
        return Persona.__DB.run(query, values)

    def agregar(self):
        query = 'INSERT INTO '+Persona.__tableName+' (email,nombre, telefono) VALUES (?,?,?)'
        values = (self.__email,self.__nombre,self.__telefono)
        Persona.__DB.run(query,values)

    def modificar(email, nombre, telefono, id):
        query = 'UPDATE '+Persona.__tableName+' SET email = ?, nombre = ?, telefono = ? WHERE id = ?'
        values = (email, nombre, telefono, id)
        Persona.__DB.run(query, values)

    def eliminar(id):
        query = 'DELETE FROM '+Persona.__tableName+' WHERE id = ?'
        values = (id)
        Persona.__DB.run(query, values)

