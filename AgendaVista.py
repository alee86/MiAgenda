from os import system
from AgendaModelo import *


class VistaAgenda:
    def menuAgenda(self):
        lista = AgendaModelo.consultarUsuario()
        tupla = lista[0]
        usuario = tupla[0]
        print(f'''
##########################################################################
    Hola {usuario.upper()}, esta es tu agenda de contactos. 
    ¿Qué que gustaria hacer?

        1- Ir a contatos.
        2- Cambiar nombre de la agenda

        9- Eliminar agenda.
        0- Salir
    ####################################################################EEEEEE
''')

        return int(input(''))

    def pedirDatos(self,*args):
        system('cls')
        print('\n\n\t----------------------')
        print('\n\tIngrese los siguientes datos:')
        salida = dict()
        for r in args:
            salida[r] = input(r+ " ")
        system('cls')   
        return salida	

    def eliminar(self):
        print('\n\t      ###¡ATENCIÓN!###')
        print('\n\t¿Seguro desea eliminar agenda?')
        print('\tSe perderán todos los contactos')
        print('\t    1 - SI        2 - NO')
        return int(input('\n\tOpción: '))			
