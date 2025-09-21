from os import system 
from parqueadero import Parqueadero
from propietarios import Propietario

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

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR VEHICULOS -"
									"\n\t************************************************")

							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR VEHICULO -"
									"\n\t************************************************")

							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR VEHICULO -"
									"\n\t************************************************")

							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR VEHICULO -"
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
				
				elif opcion == 3:
					
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

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR PARQUEOS -"
									"\n\t************************************************")

							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PARQUEO -"
									"\n\t************************************************")

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


