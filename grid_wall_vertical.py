import pygame
from pygame.sprite import Sprite
import settings
class WallVertical(Sprite):
	"""Klasa służące do tworzenia pionowych ścian"""
	def __init__(self,settings, screen):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0,0,settings.wall_vertical_width,settings.wall_vertical_height)
		self.rect.left=self.screen_rect.left
		self.rect.top=self.screen_rect.top
		self.color=settings.wall_color
	def draw_wall(self):
		"""Wyświetlanie ściany"""
		pygame.draw.rect(self.screen,self.color,self.rect)

