import re # Libreria para trabajar con expresiones regulares (validación de email y placas)
from os import system 

# Clase principal 
class Vehiculo:

	# Constructor de la clase
	def __init__(self, placa, marca, modelo, color, id_propietario, nombre_propietario, tipo):
		#Atributos
		self.placa_vehiculo = placa
		self.marca_vehiculo = marca
		self.modelo_vehiculo = modelo
		self.color_vehiculo = color
		self.id_propietario_vehiculo = id_propietario
		self.nombre_propietario_vehiculo = nombre_propietario

		if tipo == 1:
			self.tipo_vehiculo = "AUTOMOVIL"
		elif tipo == 2:
			self.tipo_vehiculo = "MOTOCICLETA"
	

	def validar_placa(self, placa, tipo):

		# metodo re.match	  
		# Valida si la placa contiene exactamente 3 letras seguidas de 3 números.
		# Returns: True si la cadena coincide con el patrón, False en caso contrario.

		# El patrón:
		# [a-zA-Z] : cualquier letra (mayúscula o minúscula)
		# {3}      : que se repita 3 veces o dos veces
		# \d       : cualquier dígito (número del 0 al 9)
		# {3}      : que se repita 3 veces
		# ^        : asegura el inicio del string
		# $        : asegura el final del string

		if tipo == 1:

			patron = r"^[a-zA-Z]{3} \d{3}$"

			if re.match(patron, placa):
				return True
			else:
				return False

		elif tipo == 2:

			patron = r"^[a-zA-Z]{3} \d{2}$"

			if re.match(patron, placa):
				return True
			else:
				return False

	# Muestra todos los datos del propietario 
	def visualizar_vehiculo(self):

		print(f"\n\tPlaca del Vehiculo:\t\t\t{self.placa_vehiculo}\n"
			f"\tTipo de Vehiculo:\t\t\t{self.tipo_vehiculo}\n"
			f"\tMarca del Vehiculo:\t\t\t{self.marca_vehiculo}\n"
			f"\tModelo del Vehiculo:\t\t\t{self.modelo_vehiculo}\n"
			f"\tColor del Vehiculo:\t\t\t{self.color_vehiculo}\n"
			f"\tID del propietario del Vehiculo:\t{self.id_propietario_vehiculo}\n"
			f"\tNombre del propietario del Vehiculo:\t{self.nombre_propietario_vehiculo}\n")
			

	def modificar_vehiculo(self):

		#Blucle
		while True:
			system('cls')

			#Menú de opciones para modificar los datos del vehiculo
			print("\n\t**************************************************"
				f"\n\t- Se modificara el Vehiculo de placas {self.placa_vehiculo} -"
				"\n\t****************************************************"
				"\n\t\t\t- ¡Recuerde! -"
				"\n\tLas modificaciones realizadas en este modulo se aplicaran a operaciones futuras"
				"\n\tOpciones para modificar:"
				"\n\t1). Visializar datos almacenados del Vehiculo"
				"\n\t2). Modificar Marca del Vehiculo"
				"\n\t3). Modificar Modelo del Vehiculo"
				"\n\t4). Modificar Color del Vehiculo"				
				"\n\t5). Modificar Id del propietario del Vehiculo"				
				"\n\t0). Salir del menu de Modificacion")

			try:
				opcion = int(input("\n\tIngrese una opcion: "))	

				if opcion == 1:

					print("\n\t\t- Datos almacenadados -"
						"\n\t==========================================================")
					#Llama metodo visualizar_vehiculo	
					self.visualizar_vehiculo()

				elif opcion == 2:
					# strip() → elimina espacios al inicio/fin
					# upper() → convierte todo a MAYÚSCULAS
					marca = str(input("\tIngrese la nueva marca del Vehiculo: ")).strip().upper()
					while marca == "": # Validación de campo vacío
						marca = str(input("\tEl dato ingresado está vacío"
							"\n\tIngrese la nueva marca del Vehiculo: ")).strip().upper()

					# Mensaje de confirmación para guardar el cambio
					if self.confirmacion() == 1:
						self.marca_vehiculo = marca
						print("\n\tLa nueva del Vehiculo fue modificada exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						

				elif opcion == 3:

					# strip() → elimina espacios al inicio/fin
					# upper() → convierte todo a MAYÚSCULAS
					modelo = str(input("\tIngrese el nuevo modelo del Vehiculo: ")).strip().upper()
					while modelo == "": # Validación de campo vacío
						modelo = str(input("\tEl dato ingresado está vacío"
							"\n\tIngrese el nuevo modelo del Vehiculo: ")).strip().upper()

					# Mensaje de confirmación para guardar el cambio
					if self.confirmacion() == 1:
						self.modelo_vehiculo = modelo
						print("\n\tEl modelo del vehiculo fue modificado exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						break

				elif opcion == 4:
					# strip() → elimina espacios al inicio/fin
					# upper() → convierte todo a MAYÚSCULAS
					color = str(input("\tIngrese el nuevo color del Vehiculo: ")).strip().upper()
					while color == "": # Validación de campo vacío
						color = str(input("\tEl dato ingresado está vacío"
							"\n\tIngrese el nuevo color del Vehiculo: ")).strip().upper()
					
					# Mensaje de confirmación para guardar el cambio
					if self.confirmacion() == 1:
						self.color_vehiculo = color
						print("\n\tEl color del vehiculo fue modificado exitosamente.")
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						break
			
				elif opcion == 5:
					print("\tModulo de modificar propietario")
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
		#Mensaje de confirmación.
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

	