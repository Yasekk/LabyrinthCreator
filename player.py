import pygame
from pygame.sprite import Sprite
class Player(Sprite):
	"""Tworzenie awatara gracza"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.grid_inside_width-2*settings.wall_vertical_width,settings.grid_inside_height-2*settings.wall_horizontal_height)
		self.rect.left=2*settings.wall_vertical_width
		self.rect.top=2*settings.wall_horizontal_height
		self.color=settings.player_color
	def draw_player(self):
		"""Wświetlenie awatara gracza"""
		pygame.draw.rect(self.screen,self.color,self.rect)
