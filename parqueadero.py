import re
from os import system 
from datetime import datetime, date
from propietarios import Propietario
from parqueos import Parqueo
from fecha import Fecha

class Parqueadero:

	def __init__(self):
		self.propietarios_lista = []
		self.vehiculos_lista = []
		self.parqueos_lista = []
		self.fecha_usuario = Fecha()

	
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

	def validar_placa(self, placa, tipo):
		
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

		elif indice == "Vehiculo":
			
			self.vehiculos_lista.append(elemento)

			system('cls')
			print(f"\n\tEl Vehiculo, se ha registrado exitosamente."
				"\n\t\t- Datos almacenadados -"
				"\n\t==========================================================")	

			ultimo = len(self.vehiculos_lista) - 1				
			self.vehiculos_lista[ultimo].visualizar_vehiculo()

		elif indice == "Parqueo":

			hoy = date.today()
			ahora = datetime.now()
			ahora = ahora.strftime("%H:%M:%S")

			print(f"\n\tFecha:\t\t{hoy}"
				f"\n\tHora:\t\t{ahora}")

			placa = str(input("\tIngrese la identificacion de la placa del vehiculo: ")).strip().upper()								

			pos_vehiculo = self.busqueda_general(placa, "Vehiculo")

			if pos_vehiculo != -1:
				lugar = 0

				for parqueo in self.parqueos_lista:
					if parqueo.placa_parqueo == placa:						
						lugar = 1 	
						break

				if lugar == 0:
					mensaje = "\t¿Desea registrar la entrada al parqueadero?"
					valor = self.confirmacion(mensaje)

					if valor == 1:

						# parque_datos =[]

						parqueo = Parqueo(elemento, hoy, ahora, placa)
						self.parqueos_lista.append(parqueo)

						tipo = self.vehiculos_lista[pos_vehiculo].tipo_vehiculo

						parqueo.parqueo_vehiculo.append(tipo)
						marca = self.vehiculos_lista[pos_vehiculo].marca_vehiculo
						parqueo.parqueo_vehiculo.append(marca)
						modelo = self.vehiculos_lista[pos_vehiculo].modelo_vehiculo
						parqueo.parqueo_vehiculo.append(modelo)
						color = self.vehiculos_lista[pos_vehiculo].color_vehiculo
						parqueo.parqueo_vehiculo.append(color)
						id_propietario = self.vehiculos_lista[pos_vehiculo].id_propietario_vehiculo
						parqueo.parqueo_vehiculo.append(id_propietario)
						nombre_propietario = self.vehiculos_lista[pos_vehiculo].nombre_propietario_vehiculo
						parqueo.parqueo_vehiculo.append(nombre_propietario)

						# parqueo.parqueo_vehiculo.append(parque_datos)

						system('cls')
						print(f"\n\tSe ha registrado exitosamente el parqueo del vehiculo."
							"\n\t\t- Datos almacenadados -"
							"\n\t==========================================================")

						# ultimo = len(self.parqueos_lista) - 1	
						parqueo.visualizar_parqueo()			
						# self.parqueos_lista[ultimo].visualizar_parqueo()					

					else:
						print("\n\tSe cancelo la creacion del vehiculo")

				else:
					print(f"\tEl vehiculo con placa {placa}, ya esta dentro del parqueadero")

			else:
				print(f"\n\tLa placa {placa}, No está registrado en el sistema.")


			# self.parqueos_lista.append(elemento)

		elif indice == "Salida":

			parqueo = self.parqueos_lista[posicion]
			fecha = parqueo.fecha_parqueo
			hora = parqueo.hora_parqueo

			mensaje = "\t¿Desea registrar la Salida del parqueadero?"
			valor = self.confirmacion(mensaje)

			if valor == 1:

				fecha = self.fecha_usuario.crear_fecha()

				print(fecha)

				hora_usuario = self.fecha_usuario.crear_hora(fecha)

				print(hora_usuario)





				


			else:
				print("\n\tSe cancelo la creacion del vehiculo")








		
#-----------------------------------------------------------------------------------------------------------------------
	def busqueda_general(self, codigo, indice):

		if indice == "Propietario":
			for i in range (len(self.propietarios_lista)):				
				if self.propietarios_lista[i].id_propietario == codigo:
					return i  
			return -1

		elif indice == "Vehiculo":
			for i in range (len(self.vehiculos_lista)):				
				if self.vehiculos_lista[i].placa_vehiculo == codigo:
					return i  
			return -1

		elif indice == "Parqueo":
			for i in range (len(self.parqueos_lista)):				
				if self.parqueos_lista[i].id_parqueo == codigo:
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

		elif indice == "Vehiculo":

			if self.vehiculos_lista:
				print("\n\t\tListado de Vehiculos"
					"\n\t================================================")
				contador = 0
				
				for vehiculo in self.vehiculos_lista:
					print(f"\n\tVehiculo No {contador + 1}"
						f"\n\tPlaca del Vehiculo:\t\t{vehiculo.placa_vehiculo}"
						f"\n\tTipo de Vehiculo:\t\t{vehiculo.tipo_vehiculo}"
						"\n\t=====================================================================================")
					contador += 1
			else:
				print("\n\tLa lista esta vacia, Aun no se han agregado Vehiculos")

		elif indice == "Parqueo":

			if self.parqueos_lista:
				print("\n\t\tListado de Vehiculos Parqueados"
					"\n\t================================================")
				contador = 0
				
				for parqueo in self.parqueos_lista:
					print(f"\n\tVehiculo No {contador + 1}"
						f"\n\tPlaca del Vehiculo:\t\t{parqueo.placa_parqueo}"
						f"\n\tTipo de Vehiculo:\t\t{parqueo.parqueo_vehiculo[0]}"
						f"\n\tMarca del Vehiculo:\t\t{parqueo.parqueo_vehiculo[1]}"
						"\n\t=====================================================================================")
					contador += 1
			else:
				print("\n\tLa lista esta vacia, Aun no se han parqueado vehiculos")




#------------------------------------------------------------------------------------------------------------------------	
	def visualizar_general(self, posicion, indice):

		if indice == "Propietario":

			self.propietarios_lista[posicion].visualizar_propietario()

		elif indice == "Vehiculo":

			self.vehiculos_lista[posicion].visualizar_vehiculo()

		elif indice == "Parqueo":

			self.parqueos_lista[posicion].visualizar_parqueo()


			




#-------------------------------------------------------------------------------------------------------------------
	
	def modificar_general(self, posicion, indice):

		if indice == "Propietario":

			valor = self.propietarios_lista[posicion].modificar_propietario()

			if valor == 1:

				email = str(input("\tIngrese el nuevo correo electronico del Propietario: ")).strip()
				while self.validar_email(email) == False:
					email = str(input("\tEl dato ingresado no es valido para correo electronico"
						"\n\tIngrese el nuevo correo electronico del Propietario: ")).strip()

				if self.confirmacion("") == 1:
					self.propietarios_lista[posicion].email_propietario = email
					print("\n\tEl Correo electronico del Propietario fue modificado exitosamente.")
					input()
					self.propietarios_lista[posicion].modificar_propietario()

				else:
					print("\n\tSe cancela la modificacion, No se guardara cambios.")
					input()
					self.propietarios_lista[posicion].modificar_propietario()

			

		elif indice == "Vehiculo":

			valor = self.vehiculos_lista[posicion].modificar_vehiculo()

			if valor == 1:

				codigo = str(input("\tIngrese el nuevo numero de identificacion del propietario: ")).strip()
				while codigo.isdigit() == False:
					codigo = str(input("\tEl dato ingresado no es un número de identificacion."
						"\n\tIngrese el nuevo numero de identificacion del propietario: ")).strip()

				pos_propietario = self.busqueda_general(codigo, "Propietario")

				if pos_propietario != -1:

					if self.confirmacion("") == 1:

						nombre = self.propietarios_lista[pos_propietario].nombre_propietario
						apellido = self.propietarios_lista[pos_propietario].apellido_propietario
						self.vehiculos_lista[posicion].id_propietario_vehiculo = codigo
						self.vehiculos_lista[posicion].nombre_propietario_vehiculo = f"{nombre} {apellido}"

						print("\n\tEl id del propietario del Vehiculo fue modificado exitosamente.")
						input()
						self.vehiculos_lista[posicion].visualizar_vehiculo()
					
					else:
						print("\n\tSe cancela la modificacion, No se guardara cambios.")
						input()
						self.vehiculos_lista[posicion].visualizar_vehiculo()					

				else:
					print(f"\n\tEl numero de identificacion {codigo}, No está registrado en el sistema.")
					input()
					self.vehiculos_lista[posicion].visualizar_vehiculo()










