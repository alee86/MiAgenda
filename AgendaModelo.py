from MiAgendaDB import *



class AgendaModelo:
	__DB = DB(name = 'MiAgendaDB')
	__tablename = 'agenda'

	def __init__(self, usuario):
		self.__usuario = usuario

	@classmethod	
	def consultar(self):
		query = 'SELECT * FROM '+AgendaModelo.__tablename
		return AgendaModelo.__DB.run(query)
		
	@classmethod
	def consultarUsuario(self):
		query = 'SELECT usuario FROM '+AgendaModelo.__tablename
		return AgendaModelo.__DB.run(query)

	def nombrarAgenda(self):
		query = "INSERT INTO "+AgendaModelo.__tablename+"(usuario) VALUES (?)"
		values = (self.__usuario)
		AgendaModelo.__DB.run(query, values)


	def modificar(self):
		query = 'UPDATE '+AgendaModelo.__tablename+' SET usuario = ?'
		values = (self.__usuario)
		AgendaModelo.__DB.run(query, values)

	@classmethod
	def eliminar(self):
		query = 'DELETE FROM '+AgendaModelo.__tablename
		return AgendaModelo.__DB.run(query)
