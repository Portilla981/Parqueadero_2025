import re
from os import system 
from propietarios import Propietario

class Parqueadero:

	def __init__(self):
		self.propietarios_lista = []
		self.vehiculos_lista = []
		self.parqueos_lista = []

	
	def confirmacion(self, mensaje):

		while True:
			if mensaje == "":			
				print("\n\t¿Desea guardar los cambios realizados?"
						"\n\t1). SI"
						"\n\t2). NO")
			else:
				print(f"\n\t{mensaje}"
						"\n\t1). SI"
						"\n\t2). NO")

			try:
				opcion = int(input("\n\tIngrese una opción: "))
				
				if opcion == 1 or opcion == 2:
					return opcion

				else:
					print("\n\t************************************************"
						"\n\t******     Error - Opcion no valida       ******"
						"\n\t************************************************")
			
			except ValueError:
				print("\t************************************************"
					"\n\t***  Error - El dato ingresado no es válido  ***"
					"\n\t************************************************")
			input("\n\t¡Presione alguna tecla para continuar!")	

	def validar_email(self, email):
		# Valida el formato básico de un correo electrónico usando regex.
		# Expresión regular para un formato de correo electrónico básico
		patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
		if re.match(patron, email):
			return True
		else:
			return False

#----------------------------------------------------------------------------------------------------------------------
	def registrar_general(self, elemento, indice):

		if indice == "Propietario":
			
			self.propietarios_lista.append(elemento)

			system('cls')
			print(f"\n\tEl Propietario, se ha registrado exitosamente."
				"\n\t\t- Datos almacenadados -"
				"\n\t==========================================================")	

			ultimo = len(self.propietarios_lista) - 1				
			self.propietarios_lista[ultimo].visualizar_propietario()



		
#-----------------------------------------------------------------------------------------------------------------------
	def busqueda_general(self, codigo, indice):

		if indice == "Propietario":
			for i in range (len(self.propietarios_lista)):				
				if self.propietarios_lista[i].id_propietario == codigo:
					return i  
			return -1




#------------------------------------------------------------------------------------------------------------------------
	def listar_general(self, indice):

		if indice == "Propietario":

			if self.propietarios_lista:
				print("\n\t\tListado de Propietarios"
					"\n\t================================================")
				contador = 0
				
				for propietario in self.propietarios_lista:
					print(f"\n\tPropietario No {contador + 1}"
						f"\n\tId del Propietario:\t\t{propietario.id_propietario}"
						f"\n\tNombre del Propietario:\t\t{propietario.nombre_propietario} {propietario.apellido_propietario}"
						"\n\t=====================================================================================")
					contador += 1
			else:
				print("\n\tLa lista esta vacia, Aun no se han agregado Propietarios")



#------------------------------------------------------------------------------------------------------------------------	
	def visualizar_general(self, posicion, indice):

		if indice == "Propietario":

			self.propietarios_lista[posicion].visualizar_propietario()


#-------------------------------------------------------------------------------------------------------------------
	
	def modificar_general(self, posicion, indice):

		if indice == "Propietario":

			self.propietarios_lista[posicion].modificar_propietario()









