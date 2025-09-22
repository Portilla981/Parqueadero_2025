
class Parqueo:
	
	def __init__(self, parqueo, fecha, hora, placa):
		self.id_parqueo = parqueo
		self.fecha_parqueo = fecha
		self.hora_parqueo = hora
		self.placa_parqueo = placa		
		self.parqueo_vehiculo = []

	def visualizar_parqueo(self):

		print(f"\n\tCodigo del Parqueo:\t\t\t{self.id_parqueo}\n"
			f"\tFecha de ingreso:\t\t\t{self.fecha_parqueo}\n"
			f"\tHora de ingreso:\t\t\t{self.hora_parqueo}\n"
			f"\tPlaca del Vehiculo:\t\t\t{self.placa_parqueo}\n"			
			f"\tTipo de Vehiculo:\t\t\t{self.parqueo_vehiculo[0]}\n"
			f"\tMarca del Vehiculo:\t\t\t{self.parqueo_vehiculo[1]}\n"
			f"\tModelo del Vehiculo:\t\t\t{self.parqueo_vehiculo[2]}\n"
			f"\tColor del Vehiculo:\t\t\t{self.parqueo_vehiculo[3]}\n"
			f"\tID del propietario del Vehiculo:\t{self.parqueo_vehiculo[4]}\n"
			f"\tNombre del propietario del Vehiculo:\t{self.parqueo_vehiculo[5]}\n")
	
		
