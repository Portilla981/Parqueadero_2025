from datetime import datetime, date
# importacion de las librerias y manejo de tiempos

# creacion de la clase
class Fecha:
	
	# creacion de constructor con *agrs es decir de varios argumentos de 1 a n
	def __init__(self, *args):
		# inicializacion de la variable fecha del sistema
		self.fecha = datetime.now()
		self.mes = False
		self.dia = False

		# si los arg son diferentes a 3 se tomara la fecha del sistema
		if len(args) != 3:
			self.dia = date.day
			self.mes = date.month
			self.anio = date.year

		# si los argumentos son 3 entonces
		else:

			if self.validar_anio(args[0]):
				self.anio = args[0]

				if self.validar_mes(args[1]):
					self.mes = args[1]

					if self.validar_dia(args[2]):
						self.dia = args[2]

					else:
						self.dia = False
				else:
					self.mes = date.month
			else: 
				self.anio = date.year


	def validar_anio(self, anio):
		if anio >= self.fecha.year:
			return True
		return False

	def validar_mes(self, mes):
		if mes >= 1 and mes <= 12:
			return True
		return False

	def validar_dia(self, dia):
		if self.mes in [4, 6, 9, 11]:
			if dia >= 1 and dia <= 30:
				return True

		elif self.mes in [1, 3, 5, 7, 8, 10, 12]:
			if dia >= 1 and dia <= 31:
				return True

		elif self.mes == 2:
			if self.validar_bisiesto(self.anio):
				if dia >= 1 and dia <= 29:
					return True
			else:
				if dia >= 1 and dia <= 28:
					return True

		return False

	def validar_bisiesto(self, anio):
		if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
			return True
		return False

	def visualizar_fecha(self):

		if self.anio == False or self.mes == False or self.dia == False:
			return False
		else:			
			return "%d-%d-%d" %(self.anio, self.mes, self.dia)
			
		

	def crear_fecha(self):

		fecha_actual = datetime.now()
		
		# Solicitudes al usuario
		print("\tIngrese los siguientes datos: ") 
		anio = int(input("\tDigite el año: "))
		mes = int(input("\tDigite el mes: "))
		dia = int(input("\tDigite el día: "))

		verifica = 0


		if anio > fecha_actual.year:
			verifica = 1

		elif anio == fecha_actual.year:
			if mes == fecha_actual.month:
				if dia >= fecha_actual.day:
					verifica = 1
				else:
					print("\n\tEl dia ingresado es menor a la fecha actual, o tiene valores no válidos."
						"\n\tVerifique e intente nuevamente")
			elif mes > fecha_actual.month:
				verifica = 1

			else:
				print("\n\tEl mes ingresado es menor a la fecha actual, o tiene valores no válidos."
					"\n\tVerifique e intente nuevamente")
				return False
		else:
			print("\n\tLa fecha ingresada es menor a la del sistema, o tiene valores no válidos."
				"\n\tVerifique e intente nuevamente")
			return False


		if verifica == 1:
					
			# Condicon para estáblecer el valor del mes para continuar el proceso
			if mes >= 1 and mes <= 12 and dia > 0 and dia < 32:

				# Variable que captura lo que retorne la funcion llamada pasando parametros
				fecha = Fecha(anio, mes, dia)				
				return fecha
			
			else:
				print("\tLos valores ingresados están por fuera de los rangos de fecha")
				return False

		else:
			print("\n\tNo se puede cargar la fecha")
			return False

	def crear_hora(self, fecha):

		fecha_actual = datetime.now()
		ahora = datetime.now()
		hora_lista = ahora.strftime("%H:%M:%S")

		print("\n\tIngrese los siguientes datos: ") 
		hora = int(input("\tIngrese la hora en formato 24H: "))
		while hora < 0 and hora > 23:
			hora = int(input("\tLa hora ingresada no es valida"
				"\n\tIngrese la hora en formato 24H: "))

		minuto = int(input("\tIngrese los minutos: "))
		while minuto < 0 and minuto > 60:
			minuto = int(input("\tLos minutos ingresados no son validos"
				"\n\tIngrese los minutos: "))

		fecha = datetime.strptime(fecha, "%Y-%m-%d") 

		if fecha.date() > fecha_actual.date():
			
			accion = f"{hora}:{minuto}:00" 
			return accion , 1


		elif fecha.date() == fecha_actual.date():
			if hora > ahora.hour:
				accion = f"{hora}:{minuto}:00" 
				return accion , 1
			elif hora == ahora.hour:
				if minuto > ahora.minute:
					accion = f"{hora}:{minuto}:00" 
					return accion, 1
				else:
					accion = "\n\tLa hora ingresada no es valida.""\n\tVerifique e intente nuevamente"
					return accion, 0
			else:
				accion = "\n\tLa hora ingresada no es valida.""\n\tVerifique e intente nuevamente"
				return accion, 0
		










		



	


