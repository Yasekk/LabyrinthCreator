"""Główny moduł programu."""

import pygame
import sys
from pygame.sprite import Group

import functions
from settings import Settings
from player import Player
from wall_vertical import WallVertical
from wall_horizontal import WallHorizontal
from buttons import ButtonSave, ButtonLoad

def play():
	#Inicjalizacja gry i podstawowe ustawienia.
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width,
	                                 settings.screen_height))
	pygame.display.set_caption("Labirynth")
	#Tworzenie awatara gracza, niwidzialnej siatki ścian i pustych grup 
	#do ścian labiryntu.
	player = Player(screen, settings)
	save_button = ButtonSave(settings, screen)
	load_button = ButtonLoad(settings, screen)
	grid_walls_h = Group()
	functions.create_grid_h_walls(settings, screen, grid_walls_h)
	grid_walls_v = Group()
	functions.create_grid_v_walls(settings, screen, grid_walls_v)
	walls_h = Group()
	functions.create_h_walls(settings, screen, walls_h)
	walls_v = Group()
	functions.create_v_walls(settings, screen, walls_v)
	#Generowanie pętli wyarzeń.
	while True:
		#Reakcja na klawisze i przyciski.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				functions.mouse_click(walls_h, walls_v, grid_walls_h,
				                      grid_walls_v, settings, screen,
				                      save_button, load_button)
		#Wyświetlenie obiektów i odświeżenie ekranu.
		functions.update_screen(walls_h, walls_v, player, screen,
		                        save_button, load_button)
play()
