from os import system
from ContactoModelo import * 
from ContactoVista import *



class ContactoControlador:
	def __init__(self):
		self.__Contactos = Contactos()
		self.menu()

	def menu(self):
		system('cls')
		seleccion = self.__Contactos.menuContacto()
		if seleccion == 1:
			self.mostrarContactos()
		elif seleccion == 2:
			self.buscarContacto()
		elif seleccion == 3:
			self.agregarContacto()
		elif seleccion == 4:
			self.editarContacto()
		elif seleccion == 5:
			self.eliminarContacto()			
		elif seleccion == 6:
			self.volerAgenda()
		else:
			print("\tingrese valor correcto")
			input("\t")
			self.menu()	
			
	def mostrarContactos(self):
		system('cls')
		x = Persona.mostrar()
		self.__Contactos.resultados(x)
		input("\t")
		system('cls')
		self.menu()


	def buscarContacto(self):
		dato = self.__Contactos.pedirDatos('\n\tBuscar por nombre: ')
		x = Persona.buscar(dato['\n\tBuscar por nombre: '])
		self.__Contactos.resultados(x)
		input("\t")
		system('cls')
		self.menu()


	def agregarContacto(self):
		datos = self.__Contactos.pedirDatos('\n\temail: ','\n\tNombre: ','\n\ttelefono: ')
		x = Persona(datos['\n\temail: '], datos['\n\tNombre: '], datos['\n\ttelefono: '])
		Persona.agregar(x)
		self.menu()


	def editarContacto(self):
		system('cls')
		x = Persona.mostrar()
		self.__Contactos.resultados(x)
		datos = self.__Contactos.pedirDatosEditar('\n New Email ', '\n New nombre: ', '\nNew Telefono', '\nID a modificar')
		Persona.modificar(datos['\n New Email '], datos['\n New nombre: '], datos['\nNew Telefono'], datos['\nID a modificar'])
		self.menu()


	def eliminarContacto(self):
		system('cls')
		x = Persona.mostrar()
		self.__Contactos.resultados(x)
		datos = self.__Contactos.pedirDatosEditar('\nID a eliminar')
		Persona.eliminar(datos['\nID a eliminar'])
		self.menu()
		
	def volerAgenda(self):
		pass
