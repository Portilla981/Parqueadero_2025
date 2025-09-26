# Importación de módulos del sistema
from os import system 
from parqueadero import Parqueadero
from propietarios import Propietario
from vehiculos import Vehiculo

# Clase principal Menu
class Menu:

	#Constructor de la clase
	def __init__ (self):

		# Se instancia un objeto de la clase Parqueadero,
        # que servirá como base de datos en memoria para propietarios, vehículos y parqueos
		self.parqueadero = Parqueadero()
		
		
	# Método principal que muestra el menú del sistema
	def mostrar_menu_parqueadero(self):

		# Bucle principal
		while True:

			#limpia la pantalla cada que se ejecute el metodo
			system('cls')

			# Menú principal 
			print("\t************************************************"
				"\n\t\t- PARQUEADERO SENA 2025 -"
				"\n\t************************************************"
				"\n\t****** Opciones:"
				"\n\t****** 1. Opciones para Propietario." 
				"\n\t****** 2. Opciones para Vehiculo." 
				"\n\t****** 3. Opciones para Parqueo." 
				"\n\t****** 4. Visualizar cantidad de Parqueos ocupados."
				"\n\t****** 5. Visualizar cantidad de Parqueos disponibles."
				"\n\t****** 6. Opciones para Generar Reportes."
				"\n\t****** 0. Salir del Sistema"
				"\n\t************************************************")

			try:
				opcion = int(input("\tDigité la opción deseada: "))

				# Submenu de propiertarios
				if opcion == 1:

					indice = "Propietario" # Define el índice a usar en búsquedas

					while True:
						system('cls')
						print("\t************************************************"
							"\n\t- OPCIONES PARA PROPIETARIO -"
							"\n\t************************************************"
							"\n\t****** 1. Registrar Propietario "
							"\n\t****** 2. Listar Propietarios "
							"\n\t****** 3. Visualizar Propietario "
							"\n\t****** 4. Modificar Propietario "
							"\n\t****** 5. Eliminar Propietario "
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO REGISTRAR PROPIETARIOS -"
									"\n\t************************************************")
								

								# Se pide el documento de identidad y se valida que sea numérico
								codigo = str(input("\tIngrese el numero de identificacion del propietario: "))
								while codigo.isdigit() == False:
									codigo = str(input("\tEl dato ingresado no es un número de identificacion."
										"\n\tIngrese el numero de identificacion del propietario: "))

								# Verificación si el propietario ya existe
								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario == -1:
									# Se le pide el nombre del propietario
									# strip() → elimina espacios al inicio/fin
									# upper() → convierte todo a MAYÚSCULAS
									nombre = str(input("\tIngrese el nombre del propietario: ")).strip().upper()
									while nombre == "": # Validación: no vacío
										nombre = str(input("\tEl dato ingresado está vacío"
											"\n\tIngrese el nombre del propietario: ")).strip().upper()


									apellido = str(input("\tIngrese el apellido del propietario: ")).strip().upper()
									while apellido == "":
										apellido = str(input("\tEl dato ingresado está vacío"
											"\n\tIngrese el apellido del propietario: ")).strip().upper()

									# Teléfono → strip elimina espacios y se valida que sean solo números
									telefono = str(input("\tIngrese el número telefónico del propietario: ")).strip()

									while telefono.isdigit() == False or len(telefono) != 10:
										telefono = str(input("\tEl dato ingresado no es un número telefónico."
											"\n\tIngrese el número telefónico del propietario: ")).strip()

									
									# Correo → strip elimina espacios y se valida formato de email con método validar_email()
									correo = str(input("\tIngrese el email del propietario: ")).strip()
									while self.parqueadero.validar_email(correo) == False:
										correo = str(input("\tEl dato ingresado no es un email valido."
											"\n\tIngrese el email del propietario: ")).strip()

									# Confirmación antes de guardar los datos
									mensaje = "\t¿Desea almacenar los datos del Propietario en el sistema?"
									valor = self.parqueadero.confirmacion(mensaje)

									if valor == 1:
										# Se crea el objeto propietario y se registra
										propietario = Propietario(codigo, nombre, apellido, telefono, correo)
										self.parqueadero.registrar_general(propietario, indice)										

									else:
										print("\n\tSe cancelo la creacion del propietario")

								else:
									print(f"\n\tEl numero de identificacion {codigo}, ya está registrado.")

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR PROPIETARIOS -"
									"\n\t************************************************")

								# Llama al método general de listar
								self.parqueadero.listar_general(indice)

							
							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PROPIETARIO -"
									"\n\t************************************************")
								# Se pide el número de identificación del propietario
								codigo = str(input("\tIngrese el numero de identificacion del propietario: "))

								# Se busca el propietario con el código
								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario != -1:

									# Si lo encuentra, se muestran sus datos	
									self.parqueadero.visualizar_general(pos_propietario, indice)

								else:
									# Si no existe, se muestra el mensaje notificando que no esta registrado
									print(f"\n\tEl numero de identificacion {codigo}, No está registrado en el sistema.")

							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR PROPIETARIOS -"
									"\n\t************************************************")

								codigo = str(input("\tIngrese el numero de identificacion del propietario que desea modificar: "))

								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario != -1:

									self.parqueadero.modificar_general(pos_propietario, indice)
									
									
								else:
									print(f"\n\tEl numero de identificacion {codigo}, No está registrado en el sistema.")


							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR PROPIETARIOS -"
									"\n\t************************************************")

								codigo = str(input("\tIngrese el numero de identificacion del propietario que desea eliminar: "))

								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario != -1:

									self.parqueadero.eliminar_general(pos_propietario, indice)									
									
								else:
									print(f"\n\tEl numero de identificacion {codigo}, No está registrado en el sistema.")



							elif opcion == 0:
								print("\n\t********************************************************"
										"\n\t\tVolviendo a menú inicial"
										"\n\t*********************************************************")
								break

							else:
								print("\n\t************************************************"
									"\n\t******     Error - Opción no valida       ******"
									"\n\t************************************************")


						except ValueError:
							print("\t************************************************"
								"\n\t***  Error - El dato ingresado no es válido  ***"
								"\n\t************************************************")
						input("\n\t¡Presione alguna tecla para continuar!")

				elif opcion == 2:

					indice = "Vehiculo"

					#Submenu de Vehiculos
					while True:
						system('cls')
						print("\t************************************************"
							"\n\t- OPCIONES PARA VEHICULO -"
							"\n\t************************************************"
							"\n\t****** 1. Registrar Vehiculo "
							"\n\t****** 2. Listar Vehiculos "
							"\n\t****** 3. Visualizar Vehiculo "
							"\n\t****** 4. Modificar Vehiculo "
							"\n\t****** 5. Eliminar Vehiculo "
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO REGISTRAR VEHICULO -"
									"\n\t************************************************")

								try:
									# Se pide el tipo de vehículo: 
									tipo = int(input("\tEscoja una de las opciones para el tipo de Vehiculo"
										"\n\t1). Vehiculo"
										"\n\t2). Motocicleta"
										"\n\t0). Salir del modulo"
										"\n\topcion: "))

									if tipo == 0:
										break

									elif tipo == 1 or tipo == 2:

										# Se pide la placa → strip() elimina espacios, upper() lo pone en MAYÚSCULAS
										if tipo == 1:
											print("\tRecuerde que para el registro de placa debe seguir este modelo \"ABC 255\" ")
										elif tipo == 2:
											print("\tRecuerde que para el registro de placa debe seguir este modelo \"ABC 55\" ")
										placa = str(input("\tIngrese la identificacion de la placa del vehiculo a registrar: ")).strip().upper()

										# Se valida que la placa cumpla el formato según el tipo de vehículo
										while self.parqueadero.validar_placa(placa, tipo) == False:
											placa = str(input("\tLa placa ingresada no es validad."
												"\n\tIngrese la identificacion de la placa del vehiculo a registrar: ")).strip().upper()

										# Se busca si la placa ya está registrada
										pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

										if pos_vehiculo == -1: # Si no existe, se registran los datos

											#strip() elimina espacios, upper() lo pone en MAYÚSCULAS
											marca = str(input("\tIngrese la marca del Vehiculo: ")).strip().upper()
											while marca == "":
												marca = str(input("\tEl dato ingresado está vacío"
													"\n\tIngrese la marca del Vehiculo: ")).strip().upper()

											modelo = str(input("\tIngrese el modelo del Vehiculo: ")).strip().upper()
											while modelo == "":
												modelo = str(input("\tEl dato ingresado está vacío"
													"\n\tIngrese el modelo del Vehiculo: ")).strip().upper()

											color = str(input("\tIngrese el color del Vehiculo: ")).strip().upper()
											while color == "":
												color = str(input("\tEl dato ingresado está vacío"
													"\n\tIngrese el color del Vehiculo: ")).strip().upper()

											codigo = str(input("\tIngrese el numero de identificacion del propietario: ")).strip()
											while codigo.isdigit() == False:
												codigo = str(input("\tEl dato ingresado no es un número de identificacion."
													"\n\tIngrese el numero de identificacion del propietario: ")).strip()

											# Se busca si el propietario está registrado en la lista de Propietarios
											pos_propietario = self.parqueadero.busqueda_general(codigo, "Propietario")

											if pos_propietario != -1:
												
												# Si existe el propietario se muestra el nombre completo del propietario registrado
												pro_vehiculo = f"{self.parqueadero.propietarios_lista[pos_propietario].nombre_propietario} {self.parqueadero.propietarios_lista[pos_propietario].apellido_propietario}"

												# Confirmación antes de guardar los datos
												mensaje = "\t¿Desea almacenar los datos del Vehiculo en el sistema?"
												valor = self.parqueadero.confirmacion(mensaje)
												
												# Si confirma, se crea y guarda el objeto Vehiculo
												if valor == 1:
													vehiculo = Vehiculo(placa, marca, modelo, color, codigo, pro_vehiculo, tipo)
													self.parqueadero.registrar_general(vehiculo, indice)										

												else:
													print("\n\tSe cancelo la creacion del vehiculo")

											else:
												print(f"\n\tEl numero de identificacion {codigo}, No está registrado en el sistema.")

										else:
											print(f"\n\tEl vehiculo de placas {placa}, ya está registrado.")


									else:
										print("\n\t************************************************"
											"\n\t******     Error - Opción no valida       ******"
											"\n\t************************************************")


								except ValueError:
									print("\t************************************************"
										"\n\t***  Error - El dato ingresado no es válido  ***"
										"\n\t************************************************")

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR VEHICULOS -"
									"\n\t************************************************")

								# Se llama al método listar_general() → muestra todos los vehículos guardados
								self.parqueadero.listar_general(indice)

							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR VEHICULO -"
									"\n\t************************************************")

								#strip() elimina espacios, upper() la pone en MAYÚSCULAS
								placa = str(input("\tIngrese la identificacion de la placa del vehiculo a visualizar: ")).strip().upper()								

								# Se busca si la placa existe en la lista de vehículos
								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									# Si existe, se muestran sus datos
									self.parqueadero.visualizar_general(pos_vehiculo, indice)

								else:
									print(f"\n\tLa placa {placa}, No está registrado en el sistema.")


							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR VEHICULO -"
									"\n\t************************************************")

								
								# Se pide el número de identificación de la placa del vehiculo
								placa = str(input("\tIngrese la identificacion de la placa del vehiculo que desea modificar: ")).strip().upper()								

								# Se busca el vehiculo con la placa
								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									# Si lo encuentra, llama el metodo modificar
									self.parqueadero.modificar_general(pos_vehiculo, indice)									
									
								else:
									print(f"\n\tLa placa {codigo}, No está registrado en el sistema.")

							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR VEHICULO -"
									"\n\t************************************************")

								placa = str(input("\tIngrese la identificacion de la placa del vehiculo que desea eliminar: ")).strip().upper()								

								# Buscar si el vehículo existe en la lista, según la placa
								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									# Si se encuentra la posición en la lista → se elimina
									self.parqueadero.eliminar_general(pos_vehiculo, indice)
									
								else:
									print(f"\n\tLa placa {placa}, No está registrado en el sistema.")


							elif opcion == 0:
								print("\n\t********************************************************"
										"\n\t\tVolviendo a menú inicial"
										"\n\t*********************************************************")
								break

							else:
								print("\n\t************************************************"
									"\n\t******     Error - Opción no valida       ******"
									"\n\t************************************************")


						except ValueError:
							print("\t************************************************"
								"\n\t***  Error - El dato ingresado no es válido  ***"
								"\n\t************************************************")
						input("\n\t¡Presione alguna tecla para continuar!")
				
				elif opcion == 3:

					indice = "Parqueo"
					
					while True:
						system('cls')
						print("\t************************************************"
							"\n\t- OPCIONES PARA PARQUEO -"
							"\n\t************************************************"
							"\n\t****** 1. Registrar Parqueo "
							"\n\t****** 2. Listar Parqueos "
							"\n\t****** 3. Visualizar Parqueo "
							"\n\t****** 4. Anular Parqueo "
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO REGISTRAR PARQUEO -"
									"\n\t************************************************")

								try:
									tipo = int(input("\tEscoja una de las siguientes opciones"
										"\n\t1). Registrar Parqueo del Vehiculo"
										"\n\t2). Registrar Salida del Vehiculo"
										"\n\t0). Salir del modulo"
										"\n\topcion: "))

									if tipo == 1:

										try:

											tipo = int(input("\tEscoja una de las opciones para el tipo de Vehiculo"
												"\n\t1). Vehiculo"
												"\n\t2). Motocicleta"
												"\n\t0). Salir del modulo"
												"\n\topcion: "))

											if tipo == 0:
												break

											elif tipo == 1 or tipo == 2:
												# Llama al método general para registrar la entrada del vehículo
												self.parqueadero.registrar_general(tipo, indice)	

											else:
												print("\n\t************************************************"
													"\n\t******     Error - Opción no valida       ******"
													"\n\t************************************************")

										except ValueError:
											print("\t************************************************"
												"\n\t***  Error - El dato ingresado no es válido  ***"
												"\n\t************************************************")


									elif tipo == 2:
										
										# Se solicita la placa del vehículo que va a salir
										placa = str(input("\tIngrese la placa del vehiculo para registrar la salida: ")).strip().upper()								

										# pos_vehiculo = self.parqueadero.busqueda_general(placa, "Vehiculo")

										# if pos_vehiculo != -1:

										lugar = "" # Aquí se guarda la posición del vehículo dentro de la lista de parqueos

										# Se recorre toda la lista de parqueos ocupados
										for i in range(len(self.parqueadero.parqueos_lista)):
											# print(self.parqueadero.parqueos_lista[i].placa_parqueo)
											# Si la placa del vehículo parqueado es igual a placa:
											if self.parqueadero.parqueos_lista[i].placa_parqueo == placa:						
												lugar = i # Guarda la posición encontrada													

										# Si se encontró el vehículo dentro de los parqueos
										if lugar != "":
											# Se registra la salida del vehículo en el sistema
											self.parqueadero.registrar_general(lugar, "Salida")
											
										else:
											print(f"\n\tLa placa {placa}, No está registrado en el sistema.")

										# else:
										# 	print(f"\n\tLa placa {placa}, No está registrado en el sistema.")											

									elif tipo == 0:
										break

									else:
										print("\n\t************************************************"
											"\n\t******     Error - Opción no valida       ******"
											"\n\t************************************************")

								except ValueError:
									print("\t************************************************"
										"\n\t***  Error - El dato ingresado no es válido  ***"
										"\n\t************************************************")							
						
							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR PARQUEOS -"
									"\n\t************************************************")

								# Llama al método general que lista todos los parqueos registrados
								self.parqueadero.listar_general(indice)


							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PARQUEO -"
									"\n\t************************************************")

								placa = str(input("\tIngrese la placa del vehiculo para visualizar el parqueo: ")).strip().upper()								

								# Busca si el vehículo está registrado en el sistema
								pos_vehiculo = self.parqueadero.busqueda_general(placa, "Vehiculo")

								if pos_vehiculo != -1:
									
									lugar = ""
									
									 # Se busca dentro de la lista de parqueos activos
									for i in range(len(self.parqueadero.parqueos_lista)):
										# Imprime todas las placas ocupadas
										print(self.parqueadero.parqueos_lista[i].placa_parqueo)
										# Si la placa del parqueo es igual a placa:
										if self.parqueadero.parqueos_lista[i].placa_parqueo == placa:	
											# Guardamos la posición del parqueo correspondiente					
											lugar = i 												

									# Si se encontró la placa en la lista de parqueos llama al metodo visualizar_general
									if lugar != "":
										self.parqueadero.visualizar_general(lugar, indice)
									else:
										print(f"\n\tLa placa {placa}, No está registrado en el sistema.")

								else:
									print(f"\n\tLa placa {placa}, No está registrado en el sistema.")

							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ANULAR PARQUEO -"
									"\n\t************************************************")

								# Cantidad de parqueos ocupados
								posicion = len(self.parqueadero.parqueos_lista)

								# Si la posicion es mayor a 0 hay uno o mas parqueo ocupado
								if posicion > 0:
									
									# Se obtiene el último vehículo ingresado (último de la lista)
									posicion = len(self.parqueadero.parqueos_lista) - 1
									print("\tRecuerde que este modulo solo anulara la ultima entrada registrada,"
										"\n\tuna vez se registre la anulacion de la entrada podra realizar nuevamente el ingreso del vehiculo\n")

									# Se elimina el último parqueo (anulación de entrada)
									self.parqueadero.eliminar_general(posicion, indice)

								else:
									print("Aun no tienes registros de ingreso de vehiculos")
							

							elif opcion == 0:
								print("\n\t********************************************************"
										"\n\t\tVolviendo a menú inicial"
										"\n\t*********************************************************")
								break

							else:
								print("\n\t************************************************"
									"\n\t******     Error - Opción no valida       ******"
									"\n\t************************************************")


						except ValueError:
							print("\t************************************************"
								"\n\t***  Error - El dato ingresado no es válido  ***"
								"\n\t************************************************")

						input("\n\t¡Presione alguna tecla para continuar!")

				elif opcion == 4:

					system('cls')
					print("\n\t************************************************"
					"\n\t\t- MÓDULO PARQUEOS OCUPADOS -"
					"\n\t************************************************")

					# Se obtiene la lista de parqueos activos desde el sistema
					lista  = self.parqueadero.parqueos_lista

					#contadores
					vehi = 0
					moto = 0

					# Recorre toda la lista de parqueos ocupados
					for i in range(len(lista)):
						# Si en la posición i hay un automóvil
						if self.parqueadero.parqueos_lista[i].parqueo_vehiculo[0] == "AUTOMOVIL":
							vehi += 1 # Suma uno al contador de automóviles
						# Si en la posición i hay una motocicleta
						elif self.parqueadero.parqueos_lista[i].parqueo_vehiculo[0] == "MOTOCICLETA":
							moto += 1 # Suma uno al contador de motos

					# Calcula el total de parqueos ocupados autos y motos
					total = vehi + moto

					if total == 0:
						print(f"\tEn el momento No tiene parqueos ocupados")
					
					else:
						print(f"\tEn el momento tiene un total de {vehi + moto} parqueos ocupado, de la siguinete forma:")
						
						if vehi == 1: 
							print (f"\tAutomoviles:\t1 zona Ocupada")
						else:
							print (f"\tAutomoviles:\t{vehi} zonas Ocupadas")

						if moto == 1:
							print (f"\tMotocicletas:\t1 zona Ocupada")
						else:
							print (f"\tMotocicletas:\t{moto} zonas Ocupadas")

				elif opcion == 5:
					system('cls')
					print("\n\t************************************************"
					"\n\t\t- MÓDULO PARQUEOS DISPONIBLES -"
					"\n\t************************************************")
					#Llama el metodo reporte_general de la clase parqueadero
					self.parqueadero.reporte_general(2)					

				elif opcion == 6:

					while True:
						system('cls')
						print("\t************************************************"
							"\n\t\t- OPCIONES PARA REPORTES -"
							"\n\t************************************************"
							"\n\t****** 1. Reporte de registro cantidad de Vehiculos parqueados"
							"\n\t****** 2. Reporte de registro cantida de espacios disponibles"
							"\n\t****** 3. Reporte de pagos recibidos por parqueo"
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t- REPORTE CANTIDAD DE VEHICULOS PARQUEADOS -"
									"\n\t************************************************")
								#Llama el metodo reporte_general de la clase parqueadero
								self.parqueadero.reporte_general(1)

							
							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t- REPORTE CANTIDAD DE ESPACIOS DISPONIBLES -"
									"\n\t************************************************")
								#Llama el metodo reporte_general de la clase parqueadero
								self.parqueadero.reporte_general(2)

							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t- REPORTE PAGOS RECIBIDOS POR PARQUEO -"
									"\n\t************************************************")
								#Llama el metodo reporte_general de la clase parqueadero
								self.parqueadero.reporte_general(3)


							elif opcion == 0:
								print("\n\t********************************************************"
										"\n\t\tVolviendo a menú inicial"
										"\n\t*********************************************************")
								break

							else:
								print("\n\t************************************************"
									"\n\t******     Error - Opción no valida       ******"
									"\n\t************************************************")


						except ValueError:
							print("\t************************************************"
								"\n\t***  Error - El dato ingresado no es válido  ***"
								"\n\t************************************************")
						input("\n\t¡Presione alguna tecla para continuar!")

				elif opcion == 0:
					print("\n\t********************************************************"
							"\n\t\tVolviendo a menú inicial"
							"\n\t*********************************************************")
					break

				else:
					print("\n\t************************************************"
						"\n\t******     Error - Opción no valida       ******"
						"\n\t************************************************")

			except ValueError:
				print("\t************************************************"
					"\n\t***  Error - El dato ingresado no es válido  ***"
					"\n\t************************************************")
			input("\n\t¡Presione alguna tecla para continuar!")
		




#======================================
#ejecución del metodo principal e instancia
if __name__ == '__main__':
	#instancia
	menu = Menu()
	#objeto.metodo -> el que se ejecuta primero
	menu.mostrar_menu_parqueadero()


