"""Moduł zawierający klasę z podstawowymi parametrami gry."""

class Settings():
	
	def __init__(self):
		"""Podawanie podstawowych parametrów gry"""
		#Parametry ekranu.
		self.screen_height = 650
		self.screen_width = 1300
		#Obliczanie szerokości i wysokości komórek, z kórych będzie
		#składał się labirynt, zeskalowanych z wymiarami ekranu.
		self.width_grid_number = 11
		self.height_grid_number = 7
		self.width_grid = self.screen_width/self.width_grid_number
		self.height_grid = self.screen_height/self.height_grid_number
		#Obliczanie wymiarów poziomych i pionowych ścian labiryntu oraz 
		#przestrzeni pomiędzy nimi.
		self.wall_horizontal_height = self.height_grid/10
		self.wall_horizontal_width = self.width_grid
		self.wall_vertical_height = self.height_grid
		self.wall_vertical_width = self.width_grid/10	
		self.grid_inside_width = (self.width_grid-2
		                          * self.wall_vertical_width)
		self.grid_inside_height=(self.height_grid-2
		                         * self.wall_horizontal_height)
		#Ustalenie koloru awataru gracza oraz ścian labiryntu.
		self.wall_color=(250, 250, 250)
		self.player_color=(150, 150, 150)
		
