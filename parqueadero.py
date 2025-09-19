
from propietarios import Propietario

class Parqueadero:

	def __init__(self):
		self.propietarios = []
		self.vehiculos = []
		self.parqueos = []


	def registrar_propietario(self, cod_propietario):

		nombre = str(input("Ingrese el nombre del propietario: ")).strip()
		telefono = str(input("\tIngrese el número telefónico del propietario: ")).strip()
		while telefono.isdigit() == False:
			telefono = str(input("\tEl dato ingresado no es un número telefónico."
				"\n\tIngrese el número telefónico del propietario: ")).strip()
		
		correo = str(input("Ingrese el nombre del propietario: "))





		

	def busqueda_general(self, codigo, indice):

		if indice == "Propietario":
			for i in range (len(self.propietarios)):				
				if self.propietarios[i].id_propietario == codigo:
					return i  
			return -1





