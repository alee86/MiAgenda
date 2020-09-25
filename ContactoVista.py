from os import system



class Contactos:

    def menuContacto(self):
        print('''
#######################################################
        MENU DE CONTACTOS
####################################################### 

		1 - Mostrar contactos.
		2 - Buscar contacto.
		3 - Agregar contacto.
		4 - Editar contacto.
		5 - Eliminar un contacto.
		6 - Volver a menu de principal''')
        return int(input('Ingresa el número de la opción: '))


    def pedirDatos(self, *args):
        system('cls')
        print('\n\n\t-----------------------------')
        print('\n\tIngrese los siguientes datos:')
        salida = dict()
        for r in args:
            salida[r] = input(r+ ' ')
            system('cls')   
        return salida


    def pedirDatosEditar(self, *args):
        print('\n\n\t-----------------------------')
        print('\n\tIngrese los siguientes datos:')
        salida = dict()
        for r in args:
            salida[r] = input(r+ " ")  
        return salida 


    def resultados(self,resultados):
        print('\n\n\tContacto/s: \n')
        for r in resultados:
            print("\t", r)

