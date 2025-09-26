# Librerías
import re # Para trabajar con expresiones regulares (validación de email y placas)
from os import system 
from datetime import datetime, date # Manejo de fechas y horas
from propietarios import Propietario
from parqueos import Parqueo
from fecha import Fecha

#Clase principal
class Parqueadero:

	def __init__(self):
		#atributo tipo lista -> almacenar los objetos del sistema
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
		# Valida el formato de las placas
		if tipo == 1:

			# Automóviles: 3 letras + espacio + 3 dígitos
			patron = r"^[a-zA-Z]{3} \d{3}$"

			#Se usan regex simples y re.match para comprobar el formato
			if re.match(patron, placa):
				return True
			else:
				return False

		elif tipo == 2:
			 # Motos: 3 letras + espacio + 2 dígitos
			patron = r"^[a-zA-Z]{3} \d{2}$"

			if re.match(patron, placa):
				return True
			else:
				return False


#----------------------------------------------------------------------------------------------------------------------
	def registrar_general(self, elemento, indice):

		if indice == "Propietario":
			
			# Añade el objeto Propietario recibido como 'elemento' a la lista de propietarios
			self.propietarios_lista.append(elemento)

			system('cls')
			print(f"\n\tEl Propietario, se ha registrado exitosamente."
				"\n\t\t- Datos almacenadados -"
				"\n\t==========================================================")	

			# Visualizar el último propietario agregado:
            # Se calcula la posición del último elemento y se llama a su método de visualización.
			ultimo = len(self.propietarios_lista) - 1				
			self.propietarios_lista[ultimo].visualizar_propietario()

		elif indice == "Vehiculo":
			
			# Añade el objeto Vehiculo recibido como 'elemento' a la lista de Vehiculos
			self.vehiculos_lista.append(elemento)

			system('cls')
			print(f"\n\tEl Vehiculo, se ha registrado exitosamente."
				"\n\t\t- Datos almacenadados -"
				"\n\t==========================================================")	

			ultimo = len(self.vehiculos_lista) - 1				
			self.vehiculos_lista[ultimo].visualizar_vehiculo()

		elif indice == "Parqueo":

			#Se genera un código de zona (VEHICULO-001, MOTOCICLETA-01)
			if elemento == 1:
				ident = 'AUTOMOVIL'
				zona = "VEHICULO-001" # código base inicial
				precio = 2800 # valor por hora/fracción 

			elif elemento == 2:
				ident = 'MOTOCICLETA'
				zona = "MOTOCICLETA-01"	
				precio = 1500
			
			#cuenta cuántos parqueos activos hay de ese tipo (para controlar capacidad y generar consecutivo)
			contador = 0

			for i in range(len(self.parqueos_lista)):
				# para cada parqueo activo, si su tipo coincide con 'ident' aumentamos el contador
				if self.parqueos_lista[i].parqueo_vehiculo[0] == ident:
					contador +=1
					# 'valor' guarda el id_parqueo del último parqueo encontrado de VEHICULO, MOTOCICLETA
					valor = self.parqueos_lista[i].id_parqueo

			#permite entre 0 y 10 parqueos por VEHICULO, MOTOCICLETA
			if contador >= 0 and contador <= 10:

				# Si ya hay uno, se genera el siguiente parqueo a partir del último 'valor'
				if contador >0:				

					# re.search busca la porción numérica final del id_parqueo ("001")
					conversion = re.search(r'\d+$',valor)

					if conversion:
						# extrae el número, lo incrementa y lo vuelve a insertar ("002")
						num = int(conversion.group())
						zona = valor[:conversion.start()] + str(num + 1).zfill(len(conversion.group()))						
					
					else:
						print("no hay consecutivo")					

				
				# Obtiene fecha y hora actaul para el registro de ingreso.
				hoy = date.today()
				ahora = datetime.now()
				ahora = ahora.strftime("%H:%M:%S")

				print(
					f"\n\tCodigo de parqueo:\t\t{zona}"
					f"\n\tFecha de ingreso:\t\t{hoy}"
					f"\n\tHora de ingreso:\t\t{ahora}")

				placa = str(input("\tIngrese la identificacion de la placa del vehiculo: ")).strip().upper()								

				# Se busca la posición del vehículo en vehiculos_lista; busqueda_general devuelve -1 si no existe
				pos_vehiculo = self.busqueda_general(placa, "Vehiculo")

				if pos_vehiculo != -1:

					# Validación para que el vehículo no esté ya registrado como parqueado
					lugar = 0

					for parqueo in self.parqueos_lista:	
						# Si existe un parqueo con la misma placa, marca como ya dentro					
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
							parque_datos.append("NO registra salida")
							parque_datos.append("Tiempo Total")
							parque_datos.append(precio)
							parque_datos.append(0)
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
				while fecha_salida == False:
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
					
					if minutos_dif >= 1:
						total = (horas_dif + 1) * precio
					else:
						total = (horas_dif) * precio

					system('cls')
					print("\n\tPrevisualizacion del cobro."
						"\n\tVerifique los datos antes de hacer el cobro del parqueadero"
						"\n\t************************************************"
						f"\n\t\t- TICKET ZONA {parqueo.id_parqueo} -"
						"\n\t************************************************"
						f"\n\tRegistro de ingreso:\t{fecha_ingreso}"
						f"\n\tPlaca del vehiculo:\t{parqueo.placa_parqueo}"
						f"\n\tNombre Propietario:\t{parqueo.parqueo_vehiculo[5]}"
						f"\n\tRegistro de salida:\t{tiempo}"
						f"\n\tTotal de tiempo:\t{horas_dif} horas, {minutos_dif} minutos"
						f"\n\tValor Hora/Fraccion:\t$ {precio} pesos"
						f"\n\tTotal a pagar:\t\t$ {total} pesos")

					mensaje = "\t¿Desea realizar el cobro del parqueadero?"
					valor = self.confirmacion(mensaje)

					if valor == 1:

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
							"\n\tRecuerde mostrar este tikect a la salida")

						datos = self.reporte_lista

						for i in range(len(datos)):
							if self.reporte_lista[i][9] == 1:
								self.reporte_lista[i][9] = 0

							if self.reporte_lista[i][0] == parqueo.id_parqueo and self.reporte_lista[i][3] == parqueo.placa_parqueo:
								self.reporte_lista[i][5] = tiempo 
								self.reporte_lista[i][6] = f"{horas_dif} horas, {minutos_dif} minutos"
								self.reporte_lista[i][8] = total
								self.reporte_lista[i][9] = 1

						del self.parqueos_lista[elemento]	
		
					else:
						print("\n\tSe cancelo el cobro del parqueadero")				
				
				elif unidad == 0:
					print(hora_usuario)

			else:
				print("\n\tSe cancelo la salida del vehiculo")

		
#-----------------------------------------------------------------------------------------------------------------------
	def busqueda_general(self, codigo, indice):

		if indice == "Propietario":

			# Recorre toda la lista de propiertarios
			for i in range (len(self.propietarios_lista)): 

				# Se compara el id de cada propietario con el código ingresado
				if self.propietarios_lista[i].id_propietario == codigo:

					# Retorna la posición en la lista si encuentra coincidencia
					return i  
			# Si no encuentra nada, retorna -1 
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

			# Si la lista de propietarios no está vacía, lista.
			if self.propietarios_lista:
				print("\n\t\tListado de Propietarios"
					"\n\t================================================")
				# Contador para numerar cada propietario
				contador = 0
				
				 # Recorre la lista de propietarios
				for propietario in self.propietarios_lista:
					print(f"\n\tPropietario No {contador + 1}"
						f"\n\tId del Propietario:\t\t{propietario.id_propietario}"
						f"\n\tNombre del Propietario:\t\t{propietario.nombre_propietario} {propietario.apellido_propietario}"
						"\n\t=====================================================================================")
					
					# Se incrementa el contador
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

		# Si indice es igual a propietario llama al metodo
		if indice == "Propietario":

			# Llama al método de la clase Propietario para mostrar sus datos
			self.propietarios_lista[posicion].visualizar_propietario()

		elif indice == "Vehiculo":

			self.vehiculos_lista[posicion].visualizar_vehiculo()

		elif indice == "Parqueo":

			self.parqueos_lista[posicion].visualizar_parqueo()


#-------------------------------------------------------------------------------------------------------------------
	
	def modificar_general(self, posicion, indice):

		# Si indice es igual a propietario:
		if indice == "Propietario":

			# Se llama al método modificar_propietario() de la clase Propietario
            # Este devuelve un valor (ej: 1) para indicar qué campo se desea modificar
			valor = self.propietarios_lista[posicion].modificar_propietario()

			if valor == 1:

				# Solicita el nuevo email y valida llamando al metodo validar_email
				email = str(input("\tIngrese el nuevo correo electronico del Propietario: ")).strip()
				while self.validar_email(email) == False:
					email = str(input("\tEl dato ingresado no es valido para correo electronico"
						"\n\tIngrese el nuevo correo electronico del Propietario: ")).strip()

				# Confirmación para guardar los cambios
				if self.confirmacion("") == 1:
					self.propietarios_lista[posicion].email_propietario = email
					print("\n\tEl Correo electronico del Propietario fue modificado exitosamente.")
					input()
					# Muestra el menú de modificación del propietario
					self.propietarios_lista[posicion].modificar_propietario()

				else:
					print("\n\tSe cancela la modificacion, No se guardara cambios.")
					input()
					self.propietarios_lista[posicion].modificar_propietario()

			

		elif indice == "Vehiculo":

			# Se llama al método modificar_vehiculo() de la clase Vehiculo
			valor = self.vehiculos_lista[posicion].modificar_vehiculo()

			if valor == 1:

				codigo = str(input("\tIngrese el nuevo numero de identificacion del propietario: ")).strip()
				# Validación numerica
				while codigo.isdigit() == False:
					codigo = str(input("\tEl dato ingresado no es un número de identificacion."
						"\n\tIngrese el nuevo numero de identificacion del propietario: ")).strip()

				# Busca si el propietario con esa identificación existe en el sistema
				pos_propietario = self.busqueda_general(codigo, "Propietario")

				# Si el propietario existe
				if pos_propietario != -1:

					# Confirmación para guardar cambios
					if self.confirmacion("") == 1:

						# Actualiza el propietario del vehículo con el nuevo id y nombre
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

		# Si indice es igual a propietario:
		if indice == "Propietario":

			#Mensaje de advertencia
			print("\tRecuerde..."
				"\n\tAl realizar la eliminacion del propietario,"
				"\n\ttodo vinculo que tenga el propietario tambien sera eliminado."
				"\n\tEsta accion tendra efectos a las acciones futuras.")

			mensaje = "\t¿Desea eliminar este propietario del sistema?"
			# Confirmación para guardar cambios
			valor = self.confirmacion(mensaje)

			if valor == 1:

				propio = self.propietarios_lista[posicion]
				
				# Busca todos los vehículos asociados al propietario y los elimina
				for i in range(len(self.vehiculos_lista)):

					if self.vehiculos_lista[i].id_propietario_vehiculo == propio.id_propietario:
						# Elimina vehículo asociado
						del self.vehiculos_lista[i]

				# Elimina al propietario
				del self.propietarios_lista[posicion]

				print("\n\tSe ha eliminado a el propietario elegido")

			else:
				print("\n\tSe cancelo la eliminacion del propietario") 

		elif indice == "Vehiculo":

			mensaje = "\t¿Desea eliminar este vehiculo del sistema?"
			valor = self.confirmacion(mensaje)

			if valor == 1:

				# Elimina el vehículo de la lista
				del self.vehiculo_lista[posicion]

				print("\n\tSe ha eliminado a el vehiculo elegido")

			else:
				print("\n\tSe cancelo la eliminacion del vehiculo") 

		elif indice == "Parqueo":

			mensaje = "\t¿Desea anular la entrada de este vehiculo?"
			
			valor = self.confirmacion(mensaje)

			if valor == 1:

				# Se marca el último registro en el reporte como ANULADO
				ultima = len(self.reporte_lista) - 1

				self.reporte_lista[ultima][2] = "ANULADA"

				# Se elimina el parqueo activo de la lista
				del self.parqueos_lista[posicion]	

				print("\n\tSe ha anulado el ingreso del vehiculo, ya puede continuar con el registro")

			else:
				print("\n\tSe cancelo la anulacion de la entrada del vehiculo del sistema") 


# ---------------------------------------------------------------------
	
	def reporte_general(self, numero):

		#Reporte general del historial (entradas, salidas y anulaciones)
		if numero == 1:

			# Cuenta cuántos registros hay en el historial
			total = len(self.reporte_lista)

			#Contadores
			vehi = 0
			moto = 0
			anulada = 0
			ultima = 0
			pos = 0
			salida = 0

			# for i in range(total):
			# 	print(f"\n\t0:\t{self.reporte_lista[i][0]} "
			# 		f"\n\t1:\t{self.reporte_lista[i][1]} "
			# 		f"\n\t2:\t{self.reporte_lista[i][2]} "
			# 		f"\n\t3:\t{self.reporte_lista[i][3]} "
			# 		f"\n\t4:\t{self.reporte_lista[i][4]} "
			# 		f"\n\t5:\t{self.reporte_lista[i][5]} "
			# 		f"\n\t6:\t{self.reporte_lista[i][6]} "
			# 		f"\n\t7:\t{self.reporte_lista[i][7]} "
			# 		f"\n\t8:\t{self.reporte_lista[i][8]} "
			# 		f"\n\t9:\t{self.reporte_lista[i][9]} ")

			if total > 0:

				# Nombre del propietario de la primera entrada registrada
				primer = self.reporte_lista[0][1]

				# Recorre todos los registros de reporte_lista
				for i in range(total):

					if self.reporte_lista[i][2] == "AUTOMOVIL":
						vehi += 1 # Cuenta cuantos automóviles hay
					elif self.reporte_lista[i][2] == "MOTOCICLETA":
						moto += 1 # Cuenta cuantas motocicletas hay

					elif self.reporte_lista[i][2] == "ANULADA":
						anulada += 1 # Cuenta cuantas anulaciones hay

					# Recorre todos los registros de reporte_lista
					if self.reporte_lista[i][8] > 0 and self.reporte_lista[i][9] == 1:	

						# Guarda la posición de la última salida					
						pos = i

						# Aumenta el contador de salidas
						salida += 1

				# Guarda la hora de la última salida registrada
				ultima = self.reporte_lista[pos][5]

			#Si vehi tiene solo 1 automovil muestra: 1 automovil
			if vehi == 1:
				vehi = "1 Automovil"

			# Si tiene mas de 1 muestra cuantos tiene.
			else:
				vehi = f"{vehi} Automoviles"

			if moto == 1:
				moto = "1 Motocicleta"
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
					f"\n\n\tHasta el momento han ingresado {vehi}, {moto} y se tiene {anulada}")
				
				if salida == 0:
					print(f"\tLa primera entrada fue regitrada: {primer}"
						"\n\tAun no se registra salidas")
				else:
					print(f"\tLa primera entrada fue regitrada: {primer}"
						f"\n\tLa ultima salida reportada fue: {ultima}")

			else:
				print(f"\tEl sistema tiene {total} registros, de los cuales se considera lo siguiente;"
					f"\n\n\tHasta el momento han ingresado {vehi}, {moto} y se tiene {anulada}")
				
				if salida == 0:
					print(f"\tLa primera entrada fue regitrada: {primer}"
						"\n\tAun no se registra salidas")
				else:
					print(f"\tLa primera entrada fue regitrada: {primer}"
						f"\n\tLa ultima salida reportada fue: {ultima}")

			print("\n\t\t¡Gracias por utilizar nuestro servicio!")

		#Reporte del estado actual de los parqueaderos disponibles
		elif numero == 2:

			# lista de parqueos activos
			lista  = self.parqueos_lista

			#Contadores
			vehi = 0
			moto = 0

			# Recorre la lista de parqueos
			for i in range(len(lista)):

				# Verifica si el vehículo en el parqueo es un automóvil
				if self.parqueos_lista[i].parqueo_vehiculo[0] == "AUTOMOVIL":
					vehi += 1 #Contador

				# Verifica si el vehículo en el parqueo es una motocicleta
				elif self.parqueos_lista[i].parqueo_vehiculo[0] == "MOTOCICLETA":
					moto += 1

			# Total de parqueos ocupados
			total = vehi + moto

			#Si total = 0, todos los cupos estan disponibles
			if total == 0:
				print(f"\tEn el momento tiene un total de 20 parqueos disponibles,"
					"\n\t10 para Automoviles y 10 para Motocicletas")

			# Si no, si hay vehiculos y resta segun los cupos que tiene el parqueadero
			else:
				print(f"\tEn el momento tiene un total de {20 - total} parqueos disponibles, de la siguinete forma:")
				
				# Si solo queda 1 cupo disponible para automoviles
				if vehi == 9:
					print (f"\tAutomoviles:\t1 zona Disponible")
				else:
					print (f"\tAutomoviles:\t{10 - vehi} zonas Disponibles")

				# Si solo queda 1 cupo disponible para motocicletas
				if moto == 9:
					print (f"\tMotocicletas:\t1 zona Disponible ")
				else:
					print (f"\tMotocicletas:\t{10 - moto} zonas Disponibles ")


		#Reporte económico (valores cobrados por salidas de vehículos)
		elif numero == 3:

			total = len(self.reporte_lista)
			vehi = 0
			moto = 0
			valor_vehiculo = 0
			valor_moto = 0
			total_parqueadero = 0
			
			if total > 0:

				# primer = self.reporte_lista[0][1]

				# Recorre el historial de reportes
				for i in range(total):

					# Si es automóvil, tuvo cobro
					if self.reporte_lista[i][2] == "AUTOMOVIL" and self.reporte_lista[i][8] > 0:
						vehi += 1
						# Acumula el valor pagado
						valor_vehiculo += self.reporte_lista[i][8]
					
					# Si es motocicleta, tuvo cobro
					elif self.reporte_lista[i][2] == "MOTOCICLETA" and self.reporte_lista[i][8] > 0:
						moto += 1
						# Acumula el valor pagado
						valor_moto += self.reporte_lista[i][8]	

			# Suma el valor de la moto y del automovil 
			total_parqueadero = valor_vehiculo + valor_moto			

			if vehi == 1:
				vehi = "1 Automovil"
			else:
				vehi = f"{vehi} Automoviles"

			if moto == 1:
				moto = "1 Motocicleta"
			else:
				moto = f"{moto} Motocicletas"			

			if total == 0:
				print(f"\tEl sistema aun no tiene registros de ingresos de vehiculos.")
			
			elif total == 1:	
				print(f"\tEl sistema tiene 1 solo registro de ingreso de vehiculos"
					f"\n\tde lo cual se considera lo siguiente:")

			else:
				print(f"\tEl sistema tiene {total} registros de ingreso de vehiculos"
					f"\n\tde lo cual se considera lo siguiente:")


			if total_parqueadero == 0:
				print("\tAun no se registra salidas")

			else:
				print("\t==============================================================="
					f"\n\tCantidad de salida de Automoviles:\t{vehi}"
					f"\n\tSubtotal del cobro de parqueaderos:\t$ {valor_vehiculo}"
					f"\n\tCantidad de salida de Automoviles:\t{moto}"
					f"\n\tSubtotal del cobro de parqueaderos:\t$ {valor_moto}"
					f"\n\t-----------------------------------------------------------")

				# Verifica si fue un solo vehículo o más
				if (moto + vehi) == 1:
					print(f"\tHasta el momento se ha registrado el pago de un vehiculo")

				else:
					print(f"\tHasta el momento se ha registrado el pago de {moto + vehi} vehiculos")

				print(f"\tTotal del cobro de parqueaderos:\t$ {total_parqueadero}")				

			print("\n\t\t¡Gracias por utilizar nuestro servicio!")





















