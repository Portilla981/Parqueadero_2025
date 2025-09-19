
class Menu:

	def __init__ (self):
		pass
	
	def mostrar_menu_parqueadero():

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

							elif opcion == 2:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO LISTAR PROPIETARIOS -"
									"\n\t************************************************")
							
							elif opcion == 3:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO VISUALIZAR PROPIETARIO -"
									"\n\t************************************************")

							elif opcion == 4:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO MODIFICAR PROPIETARIOS -"
									"\n\t************************************************")

							elif opcion == 5:
								system('cls')
								print("\n\t************************************************"
									"\n\t\t- MÓDULO ELIMINAR PROPIETARIOS -"
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


