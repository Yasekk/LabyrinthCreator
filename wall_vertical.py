"""Moduł zawierający klasę do tworzenia pionowych ścian."""

import pygame
from pygame.sprite import Sprite

class WallVertical(Sprite):
	"""Klasa służące do tworzenia pionowych ścian."""
	
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0, 0, settings.wall_vertical_width,
		                        settings.wall_vertical_height)
		self.rect.left = self.screen_rect.left
		self.rect.top = self.screen_rect.top
		self.color = settings.wall_color
		
	def draw_wall(self):
		"""Wyświetlanie ściany."""
		pygame.draw.rect(self.screen, self.color, self.rect)
		
	def save(self):
		"""Zapisuje położenie danego egzemplarza ściany."""
		wall_position=[self.rect.centerx, self.rect.centery]
		return wall_position

