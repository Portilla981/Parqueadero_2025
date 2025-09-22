from os import system 
from parqueadero import Parqueadero
from propietarios import Propietario
from vehiculos import Vehiculo


class Menu:

	def __init__ (self):
		self.parqueadero = Parqueadero()
		
		
	
	def mostrar_menu_parqueadero(self):

		while True:
			system('cls')

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

				if opcion == 1:

					indice = "Propietario"

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

								codigo = str(input("\tIngrese el numero de identificacion del propietario: "))
								while codigo.isdigit() == False:
									codigo = str(input("\tEl dato ingresado no es un número de identificacion."
										"\n\tIngrese el numero de identificacion del propietario: "))

								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario == -1:

									nombre = str(input("\tIngrese el nombre del propietario: ")).strip().upper()
									while nombre == "":
										nombre = str(input("\tEl dato ingresado está vacío"
											"\n\tIngrese el nombre del propietario: ")).strip().upper()


									apellido = str(input("\tIngrese el apellido del propietario: ")).strip().upper()
									while apellido == "":
										apellido = str(input("\tEl dato ingresado está vacío"
											"\n\tIngrese el apellido del propietario: ")).strip().upper()

									telefono = str(input("\tIngrese el número telefónico del propietario: ")).strip()
									while telefono.isdigit() == False:
										telefono = str(input("\tEl dato ingresado no es un número telefónico."
											"\n\tIngrese el número telefónico del propietario: ")).strip()

									
									correo = str(input("\tIngrese el email del propietario: ")).strip()
									while self.parqueadero.validar_email(correo) == False:
										correo = str(input("\tEl dato ingresado no es un email valido."
											"\n\tIngrese el email del propietario: ")).strip()

									mensaje = "\t¿Desea almacenar los datos del Propietario en el sistema?"
									valor = self.parqueadero.confirmacion(mensaje)

									if valor == 1:
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

								self.parqueadero.listar_general(indice)

							
							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PROPIETARIO -"
									"\n\t************************************************")

								codigo = str(input("\tIngrese el numero de identificacion del propietario: "))

								pos_propietario = self.parqueadero.busqueda_general(codigo, indice)

								if pos_propietario != -1:

									self.parqueadero.visualizar_general(pos_propietario, indice)

								else:
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

									mensaje = "\t¿Desea eliminar este propietario del sistema?"
									valor = self.parqueadero.confirmacion(mensaje)

									if valor == 1:

										del self.parqueadero.propietarios_lista[pos_propietario]

										print("\n\tSe ha eliminado a el propietario elegido")

									else:
										print("\n\tSe cancelo la eliminacion del propietario") 
									
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
									tipo = int(input("\tEscoja una de las opciones para el tipo de Vehiculo"
										"\n\t1). Vehiculo"
										"\n\t2). Motocicleta"
										"\n\t0). Salir del modulo"
										"\n\topcion: "))

									if tipo == 0:
										break

									elif tipo == 1 or tipo == 2:

										placa = str(input("\tIngrese la identificacion de la placa del vehiculo a registrar: ")).strip().upper()

										while self.parqueadero.validar_placa(placa, tipo) == False:
											placa = str(input("\tLa placa ingresada no es validad."
												"\n\tIngrese la identificacion de la placa del vehiculo a registrar: ")).strip().upper()

										pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

										if pos_vehiculo == -1:

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

											pos_propietario = self.parqueadero.busqueda_general(codigo, "Propietario")

											if pos_propietario != -1:

												pro_vehiculo = f"{self.parqueadero.propietarios_lista[pos_propietario].nombre_propietario} {self.parqueadero.propietarios_lista[pos_propietario].apellido_propietario}"

												mensaje = "\t¿Desea almacenar los datos del Vehiculo en el sistema?"
												valor = self.parqueadero.confirmacion(mensaje)

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

								self.parqueadero.listar_general(indice)

							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR VEHICULO -"
									"\n\t************************************************")

								placa = str(input("\tIngrese la identificacion de la placa del vehiculo a visualizar: ")).strip().upper()								

								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									self.parqueadero.visualizar_general(pos_vehiculo, indice)

								else:
									print(f"\n\tLa placa {placa}, No está registrado en el sistema.")


							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR VEHICULO -"
									"\n\t************************************************")


								placa = str(input("\tIngrese la identificacion de la placa del vehiculo que desea modificar: ")).strip().upper()								

								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									self.parqueadero.modificar_general(pos_vehiculo, indice)									
									
								else:
									print(f"\n\tLa placa {codigo}, No está registrado en el sistema.")

							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR VEHICULO -"
									"\n\t************************************************")

								placa = str(input("\tIngrese la identificacion de la placa del vehiculo que desea eliminar: ")).strip().upper()								

								pos_vehiculo = self.parqueadero.busqueda_general(placa, indice)

								if pos_vehiculo != -1:

									mensaje = "\t¿Desea eliminar este vehiculo del sistema?"
									valor = self.parqueadero.confirmacion(mensaje)

									if valor == 1:

										del self.parqueadero.vehiculos_lista[pos_vehiculo]

										print("\n\tSe ha eliminado el vehiculo elegido")

									else:
										print("\n\tSe cancelo la eliminacion del vehiculo") 
									
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
							"\n\t****** 4. Modificar Parqueo "
							"\n\t****** 5. Eliminar Parqueo "
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO REGISTRAR PARQUEO -"
									"\n\t************************************************")

								if len(self.parqueadero.parqueos_lista) <= 10:

									try:
										tipo = int(input("\tEscoja una de las siguientes opciones"
											"\n\t1). Registrar Parqueo del Vehiculo"
											"\n\t2). Registrar Salida del Vehiculo"
											"\n\t0). Salir del modulo"
											"\n\topcion: "))


										if tipo == 1:

											codigo = str(input("\tIngrese el codigo del parqueo: ")).strip().upper()
											while codigo == "":
												codigo = str(input("\tEl dato ingresado es vacio."
													"\n\tIngrese el codigo del parqueo: ")).strip().upper()

											pos_parqueo = self.parqueadero.busqueda_general(codigo, indice)

											if pos_parqueo == -1:

												self.parqueadero.registrar_general(codigo, indice)	

											else:
												print(f"\n\tEl codigo del parqueo {codigo}, ya existe.")

										elif tipo == 2:

											placa = str(input("\tIngrese la placa del vehiculo para registrar la salida: ")).strip().upper()								

											pos_vehiculo = self.parqueadero.busqueda_general(placa, "Vehiculo")

											if pos_vehiculo != -1:

												lugar = ""

												for i in range(len(self.parqueadero.parqueos_lista)):
													print(self.parqueadero.parqueos_lista[i].placa_parqueo)
													if self.parqueadero.parqueos_lista[i].placa_parqueo == placa:						
														lugar = i														

												if lugar != "":

													self.parqueadero.registrar_general(lugar, "Salida")
													
												else:
													print(f"\n\tLa placa {placa}, No está registrado en el sistema.2")

											else:
												print(f"\n\tLa placa {placa}, No está registrado en el sistema.")											

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
									
								else:
									print(f"\n\tEl Parqueadero no tiene parqueos disponibles.")

								# input("\n\t¡Presione alguna tecla para continuar!")


							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR PARQUEOS -"
									"\n\t************************************************")

								self.parqueadero.listar_general(indice)


							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PARQUEO -"
									"\n\t************************************************")

								placa = str(input("\tIngrese la placa del vehiculo para visualizar el parqueo: ")).strip().upper()								

								pos_vehiculo = self.parqueadero.busqueda_general(placa, "Vehiculo")

								if pos_vehiculo != -1:
									
									lugar = ""

									for i in range(len(self.parqueadero.parqueos_lista)):
										print(self.parqueadero.parqueos_lista[i].placa_parqueo)
										if self.parqueadero.parqueos_lista[i].placa_parqueo == placa:						
											lugar = i 												

									if lugar != "":
										self.parqueadero.visualizar_general(lugar, indice)
									else:
										print(f"\n\tLa placa {placa}, No está registrado en el sistema.2")

								else:
									print(f"\n\tLa placa {placa}, No está registrado en el sistema.")





							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR PARQUEO -"
									"\n\t************************************************")

							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR PARQUEO -"
									"\n\t************************************************")

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

				elif opcion == 5:
					system('cls')
					print("\n\t************************************************"
					"\n\t\t- MÓDULO PARQUEOS DISPONIBLES -"
					"\n\t************************************************")

				elif opcion == 6:

					while True:
						system('cls')
						print("\t************************************************"
							"\n\t- OPCIONES PARA REPORTES -"
							"\n\t************************************************"
							"\n\t****** 1. Reporte de cantidad de Vehiculos parqueados"
							"\n\t****** 2. Reporte de cantidad de espacios disponibles para parqueo"
							"\n\t****** 3. Reporte de pagos recibidos por parqueo"
							"\n\t****** 0. Volver al menú inicial ")
						
						try:
							opcion = int(input("\tDigité la opción deseada: "))

							if opcion == 1:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- REPORTE CANTIDAD DE VEHICULOS PARQUEADOS -"
									"\n\t************************************************")

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- REPORTE CANTIDAD DE ESPACIOS DISPONIBLES -"
									"\n\t************************************************")


							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- REPORTE PAGOS RECIBIDOS POR PARQUEO -"
									"\n\t************************************************")


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
if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_parqueadero()


