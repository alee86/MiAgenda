from os import system
from AgendaVista import *
from AgendaModelo import *
from ContactoControlador import *


class ControladorAgenda:
    def __init__(self):
        self.__VistaAgenda = VistaAgenda()
        self.validacion()


    def validacion(self):
        x = AgendaModelo.consultar()
        if x == []:
            self.ponerNombre()
        else:
            self.menuAgenda()

    def ponerNombre(self):
        x = self.__VistaAgenda.pedirDatos('Ingrese nombre del usuario')
        y = AgendaModelo(x['Ingrese nombre del usuario'])
        AgendaModelo.nombrarAgenda(y)
        self.menuAgenda()


    def menuAgenda(self):
        opcion = self.__VistaAgenda.menuAgenda()
        if opcion == 1:
            self.irContactos()
        elif opcion == 2:
            self.cambiarNombreAgenda()
            self.menuAgenda()
        elif opcion == 9:
            self.eliminaAgenda()
            #9- Eliminar agenda.
        elif opcion == 0:
            self.salir()
            #Salir
        else:
            print('No es una opcion valida')
            input('')
            self.menuAgenda()
    
    
    def irContactos(self):
        ContactoControlador()
        system('cls')
        self.menuAgenda()


    def cambiarNombreAgenda(self):
        datos = self.__VistaAgenda.pedirDatos('\n\tQue nombre le queres dar? ')
        x = AgendaModelo(datos['\n\tQue nombre le queres dar? '])
        AgendaModelo.modificar(x)
        self.validacion()


    def eliminaAgenda(self):
        system('cls')
        seleccion = self.__VistaAgenda.eliminar()
        if seleccion == 1:
            AgendaModelo.eliminar()
            #AgendaModelo.eliminarCont()
            ControladorAgenda()
        elif seleccion == 2:
            ControladorAgenda()
        else:
            print("\tingrese valor correcto")
            input("\t")
            ControladorAgenda.eliminarAg()

    def salir(self):
        pass

ControladorAgenda()