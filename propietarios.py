from os import system 
import re

class Propietario:

	def __init__(self, codigo, nombre, apellido, telefono, email):
		self.id_propietario = codigo
		self.nombre_propietario = nombre
		self.apellido_propietario = apellido
		self.telefono_propietario = telefono
		self.email_propietario = email
				

	def visualizar_propietario(self):

		print(f"\n\tId del Propietario:\t\t\t{self.id_propietario}\n"
			f"\tNombre del Propietario:\t\t\t{self.nombre_propietario}\n"
			f"\tApellido del Propietario:\t\t{self.apellido_propietario}\n"
			f"\tTelefono del Propietario:\t\t{self.telefono_propietario}\n"
			f"\tCorreo electronico del Propietario:\t{self.email_propietario}\n")
			

	def modificar_propietario(self):

		while True:
			system('cls')
			print("\n\t**************************************************"
				f"\n\t- Se modificara el Propietario {self.nombre_propietario} {self.apellido_propietario} -"
				"\n\t****************************************************"
				"\n\t\t\t- ¡Recuerde! -"
				"\n\tLas modificaciones realizadas en este modulo se aplicaran a operaciones futuras"
				"\n\tOpciones para modificar:"
				"\n\t1). Visializar datos almacenados del Propietario"
				"\n\t2). Modificar Nombre o Nombres del Propietario"
				"\n\t3). Modificar Apellido o Apellidos del Propietario"
				"\n\t4). Modificar Telefono del Propietario"
				"\n\t5). Modificar Correo electronico del Propietario"				
				"\n\t0). Salir del menu de Modificacion")

			try:
				opcion = int(input("\n\tIngrese una opcion: "))	

				if opcion == 1:

					print("\n\t\t- Datos almacenadados -"
						"\n\t==========================================================")	
					self.visualizar_propietario()

				elif opcion == 2:
					nombre = str(input("\tIngrese el nuevo nombre o nombres del Propietario: ")).strip().upper()
					while nombre == "":
						nombre = str(input("\tEl dato ingresado esta vacio"
							"\n\tIngrese el nuevo nombre o nombres del Propietario: ")).strip().upper()

					if self.confirmacion() == 1:
						self.nombre_propietario = nombre
						print("\n\tEl nombre del Propietario fue modificado exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						

				elif opcion == 3:
					apellido = str(input("\tIngrese el nuevo apellido o apellidos del Propietario: ")).strip().upper()
					while apellido == "":
						apellido = str(input("\tEl dato ingresado esta vacio"
							"\n\tIngrese el nuevo apellido o apellidos del Propietario: ")).strip().upper()

					if self.confirmacion() == 1:
						self.apellido_propietario = apellido
						print("\n\tEl Apellido del Propietario fue modificado exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						break

				elif opcion == 4:
					telefono = str(input("\tIngrese el nuevo numero telefonico del Propietario: ")).strip()
					while telefono.isdigit() == False:
						telefono = str(input("\tEl dato ingresado no es un numero Telefonico."
							"\n\tIngrese el numero telefonico del Propietario: ")).strip()

					if self.confirmacion() == 1:
						self.telefono_propietario = telefono
						print("\n\tEl Telefono del Propietario fue modificado exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						break
			
				elif opcion == 5:
					return 1					

				elif opcion == 0:
					break

				else:
					print("\n\t************************************************"
						"\n\t******     Error - Opcion no valida       ******"
						"\n\t************************************************")
			
			except ValueError:
				print("\t************************************************"
					"\n\t***  Error - El dato ingresado no es válido  ***"
					"\n\t************************************************")
			input("\n\t¡Presione alguna tecla para continuar!")

	
	def confirmacion(self):

		while True:
			
			print("\n\t¿Desea guardar los cambios realizados?"
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





		

