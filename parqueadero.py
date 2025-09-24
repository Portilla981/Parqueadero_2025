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
		self.reporte_lista= []
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

			if elemento == 1:
				ident = 'AUTOMOVIL'
				zona = "VEHICULO-000"
				precio = 2800

			elif elemento == 2:
				ident = 'MOTOCICLETA'
				zona = "MOTOCICLETA-00"	
				precio = 1500
			
			contador = 0

			for i in range(len(self.parqueos_lista)):
				if self.parqueos_lista[i].parqueo_vehiculo[0] == ident:
					contador +=1
					valor = self.parqueos_lista[i].id_parqueo

			if contador >= 0 and contador <= 10:

				if contador >0:				

					conversion = re.search(r'\d+$',valor)

					if conversion:
						num = int(conversion.group())
						zona = valor[:conversion.start()] + str(num + 1).zfill(len(conversion.group()))
						print(zona)
					
					else:
						print("no hay consecutivo")					

				
				hoy = date.today()
				ahora = datetime.now()
				ahora = ahora.strftime("%H:%M:%S")

				print(
					f"\n\tCodigo de parqueo:\t\t{zona}"
					f"\n\tFecha de ingreso:\t\t{hoy}"
					f"\n\tHora de ingreso:\t\t{ahora}")

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

							parque_datos = []
							
							fecha_ingreso = f"{hoy} {ahora}"				
							fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d %H:%M:%S")

							parqueo = Parqueo(zona, hoy, ahora, placa)
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
							precio_parqueo = precio
							parqueo.parqueo_vehiculo.append(precio_parqueo)

							parque_datos.append(zona)
							parque_datos.append(fecha_ingreso)
							parque_datos.append(tipo)
							parque_datos.append(placa)
							parque_datos.append(nombre_propietario)
							parque_datos.append("Registro salida")
							parque_datos.append("Tiempo Total")
							parque_datos.append(precio)
							parque_datos.append(0)

							self.reporte_lista.append(parque_datos)

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

			else:
				print("No hay lugares de parqueo disponible para esta clase de vehiculos.")


		elif indice == "Salida":

			parqueo = self.parqueos_lista[elemento]
			fecha = parqueo.fecha_parqueo
			hora = parqueo.hora_parqueo
			precio = parqueo.parqueo_vehiculo[6]
			
			mensaje = "\t¿Desea registrar la Salida del parqueadero?"
			valor = self.confirmacion(mensaje)

			if valor == 1:
				
				fecha_ingreso = f"{fecha} {hora}"
				
				fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d %H:%M:%S")
				print(f"\tRegistro de ingreso: {fecha_ingreso}")
				print("\n\tFecha de salida")
				fecha_salida = self.fecha_usuario.crear_fecha()
				print("\tHora de salida")
				fecha_salida = fecha_salida.visualizar_fecha()
				hora_usuario, unidad = self.fecha_usuario.crear_hora(fecha_salida)
				

				if unidad == 1:

					tiempo = f"{fecha_salida} {hora_usuario}"
					tiempo = datetime.strptime(tiempo, "%Y-%m-%d %H:%M:%S")					
					diferencia = tiempo - fecha_ingreso
					diferencia = abs(diferencia.total_seconds() / 60)
					horas_dif = int(diferencia // 60)
					minutos_dif = int(diferencia % 60)
					
					if minutos_dif > 1:
						total = (horas_dif + 1) * precio
					else:
						total = (horas_dif) * precio

					system('cls')
					print("\n\t************************************************"
						f"\n\t\t- TICKET ZONA {parqueo.id_parqueo} -"
						"\n\t************************************************"
						f"\n\tRegistro de ingreso:\t{fecha_ingreso}"
						f"\n\tPlaca del vehiculo:\t{parqueo.placa_parqueo}"
						f"\n\tNombre Propietario:\t{parqueo.parqueo_vehiculo[5]}"
						f"\n\tRegistro de salida:\t{tiempo}"
						f"\n\tTotal de tiempo:\t{horas_dif} horas, {minutos_dif} minutos"
						f"\n\tValor Hora/Fraccion:\t${precio} pesos"
						f"\n\tTotal a pagar:\t\t${total} pesos"
						"\n\t---------------------------------------------------------"
						"\n\t¡Gracias por utilizar nuestro servicio!"
						"\n\tRecuerde mostrar este tikect a la salida"
						)

					datos = self.reporte_lista

					for i in range(len(datos)):
						if self.reporte_lista[i][0] == parqueo.id_parqueo and self.reporte_lista[i][2] == parqueo.placa_parqueo:
							self.reporte_lista[i][5] = tiempo 
							self.reporte_lista[i][6] = f"{horas_dif} horas, {minutos_dif} minutos"
							self.reporte_lista[i][7] = total

					del self.parqueos_lista[elemento]					
				
				elif unidad == 0:
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

# --------------------------------------------------------------------------------------------------------------

	def eliminar_general(self, posicion, indice):

		if indice == "Propietario":

			mensaje = "\t¿Desea eliminar este propietario del sistema?"
			valor = self.confirmacion(mensaje)

			if valor == 1:

				del self.propietarios_lista[posicion]

				print("\n\tSe ha eliminado a el propietario elegido")

			else:
				print("\n\tSe cancelo la eliminacion del propietario") 

		elif indice == "Vehiculo":

			mensaje = "\t¿Desea eliminar este vehiculo del sistema?"
			valor = self.confirmacion(mensaje)

			if valor == 1:

				del self.vehiculo_lista[posicion]

				print("\n\tSe ha eliminado a el vehiculo elegido")

			else:
				print("\n\tSe cancelo la eliminacion del vehiculo") 

		elif indice == "Parqueo":

			mensaje = "\t¿Desea eliminar esta zona de parqueo del sistema?"
			
			valor = self.confirmacion(mensaje)

			if valor == 1:

				del self.parqueos_lista[posicion]

				print("\n\tSe ha eliminado a el vehiculo elegido")

			else:
				print("\n\tSe cancelo la eliminacion del vehiculo") 


# ---------------------------------------------------------------------
	
	def reporte_general(self, numero):

		if numero == 1:

			total = len(self.reporte_lista)
			vehi = 0
			moto = 0
			anulada = 0
			ultima = 0
			pos = 0
			salida = 0

			# parque_datos.append(zona)
			# parque_datos.append(fecha_ingreso)
			# parque_datos.append(tipo)
			# parque_datos.append(placa)
			# parque_datos.append(nombre_propietario)
			# parque_datos.append("Registro salida")
			# parque_datos.append("Tiempo Total")
			# parque_datos.append(0)


			if total > 0:

				primer = self.reporte_lista[0][1]

				for i in range(total):

					if self.reporte_lista[i][2] == "AUTOMOVIL":
						vehi += 1
					elif self.reporte_lista[i][2] == "MOTOCICLETA":
						moto += 1

					elif self.reporte_lista[i][2] == "ANULADA":
						anulada += 1

					if self.reporte_lista[i][7] > 0:
						pos = i
						salida += 1

				if pos != 0:
					ultima = self.reporte_lista[pos - 1][5]

			if vehi == 1:
				vehi = "1 Automovil"
			else:
				vehi = f"{vehi} Automoviles"

			if moto == 1:
				moto = "\t1 Motocicleta"
			else:
				moto = f"{moto} Motocicletas"

			if anulada == 1:
				anulada = "1 Anulacion"
			else:
				anulada = f"{anulada} Anulaciones"





			if total == 0:
				print(f"\tEl sistema aun no tiene registros.")
			
			elif total == 1:	
				print(f"\tEl sistema tiene 1 solo registro, de los cuales se considera lo siguiente;"
					f"\n\tHasta el momento han ingresado {vehi}, {moto} y se tiene {anulada}")
				if pos == 0:
					print("\tAun no se registra salidas")
				else:
					print(f"\n\tLa ultima salida fue {ultima}")				
			
			else:
				print(f"\tEl sistema tiene {total} registros, de los cuales se considera lo siguiente;"
					f"\n\tHasta el momento han ingresado {vehi}, {moto} y se tiene {anulada}")
				if ultima == 0:
					print("\tAun no se registra salidas")
				else:
					print(f"\n\tLa ultima salida fue {ultima}")

			print("\t\t¡Gracias por utilizar nuestro servicio!")

















