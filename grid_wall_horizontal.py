"""Modu zawierający klasę do tworzenia poziomych elementów siatki."""

import pygame
from pygame.sprite import Sprite

class WallHorizontal(Sprite):
	"""Klasa służące do tworzenia niewidzialch poziomych ścian."""
	
	def __init__(self, settings, screen):	
		"""Okeślenie rozmiaru i położenia ścianki."""	
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.wall_horizontal_width,
		                        settings.wall_horizontal_height)
		self.rect.left = self.screen_rect.left
		self.rect.top = self.screen_rect.top
		self.color = settings.wall_color
		
	def draw_wall(self):
		"""Wyświetlanie ściany."""
		pygame.draw.rect(self.screen, self.color, self.rect)
