"""Moduł zawierający klasy tworzące przyciski."""

import pygame

class ButtonSave():
	"""Klasa tworząca przycisk zapisu."""
	
	def __init__(self, settings, screen):
		"""Tworzenie przycisku zapisującego układ labiryntu."""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.width = settings.width_grid*0.8
		self.height = settings.height_grid*0.3
		self.button_color = (100, 200, 100)
		self.text_color = (225, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = (self.screen_rect.right
							 - settings.width_grid/2)
		self.rect.bottom = (self.screen_rect.bottom
						    - settings.height_grid/2)
		self.prep_msg("Zapisz")
		
	def prep_msg(self, msg):
		"""Przygotowanie tekstu znajdującego się w przycisku."""
		self.msg_image = self.font.render(msg, True, self.text_color,
		                                  self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		"""Wyświetlenie przycisku na ekranie."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
		
class ButtonLoad():
	"""Klasa tworząca przycisk odczytu."""
	
	def __init__(self, settings, screen):
		"""Tworzenie przycisku wczytujacego zapisany układ
		labiryntu.
		"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.width,self.height = (settings.width_grid*0.8,
		                          settings.height_grid*0.3)
		self.button_color = (100, 200, 100)
		self.text_color = (225, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = (self.screen_rect.right
		                     - settings.width_grid/2)
		self.rect.bottom = (self.screen_rect.bottom
		                    - settings.height_grid/10)
		self.prep_msg("Wczytaj")
		
	def prep_msg(self, msg):
		"""Przygotowanie tekstu znajdującego się w przycisku."""
		self.msg_image = self.font.render(msg, True, self.text_color,
		                                  self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		"""Wyświetlenie przycisku na ekranie."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)		
