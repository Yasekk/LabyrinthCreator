import pygame
from wall_horizontal import WallHorizontal
from wall_vertical import WallVertical
import json

def create_grid_v_walls(settings,screen,grid_walls_v):
	"""Tworzenie niewidzialnej siatki scian pionowych znaczącej miejsca,
	po których kliknięciu będą zmikały lub pojawiały się ściany"""
	for number_y in range(settings.height_grid_number):
		for number_x in range(settings.width_grid_number+1):
			#Tworzenie sprite'u ściany, określenie jego położenia i 
			#dodanie go do grupy sprite'ów ścian poziomych 
			wall_vertical=WallVertical(settings,screen)
			wall_vertical.rect.centerx=settings.width_grid*number_x
			wall_vertical.rect.top=settings.height_grid*number_y
			grid_walls_v.add(wall_vertical)
def create_grid_h_walls(settings,screen,grid_walls_h):
	"""Tworzenie niewidzialnej siatki scian poziomych znaczącej miejsca,
	po których kliknięciu będą zmikały lub pojawiały się ściany"""
	for number_x in range(settings.width_grid_number+1):
		for number_y in range(settings.height_grid_number+1):
			wall_horizontal=WallHorizontal(settings,screen)
			wall_horizontal.rect.left=settings.width_grid*number_x
			wall_horizontal.rect.centery=settings.height_grid*number_y
			grid_walls_h.add(wall_horizontal)
def create_v_walls(settings,screen,walls_v):
	"""Tworzenie widocznej siatki pionowych ścian"""
	for number_y in range(settings.height_grid_number):
		for number_x in range(settings.width_grid_number+1):
			#Tworzenie sprite'u ściany, określenie jego położenia i 
			#dodanie go do grupy sprite'ów ścian poziomych 
			wall_vertical=WallVertical(settings,screen)
			wall_vertical.rect.centerx=settings.width_grid*number_x
			wall_vertical.rect.top=settings.height_grid*number_y
			walls_v.add(wall_vertical)
def create_h_walls(settings,screen,walls_h):
	"""Tworzenie widocznej siatki poziomych ścian"""
	for number_y in range(settings.height_grid_number+1):
		for number_x in range(settings.width_grid_number+1):
			#Tworzenie sprite'u ściany, określenie jego położenia i 
			#dodanie go do grupy sprite'ów ścian poziomych 
			wall_horizontal=WallHorizontal(settings,screen)
			wall_horizontal.rect.left=settings.width_grid*number_x
			wall_horizontal.rect.centery=settings.height_grid*number_y
			walls_h.add(wall_horizontal)
def mouse_click(walls_h,walls_v,grid_walls_h,grid_walls_v,
				settings,screen,save_button,load_button):
				mouse_x,mouse_y = pygame.mouse.get_pos()	
				if save_button.rect.collidepoint(mouse_x,mouse_y):
					#Jeżeli zostanie klikniety przycisk "save", nastąpi
					#zapisanie danych ścian pionowych i poziomych
					#w plikach
					with open("walls_v.json","w") as wall_v_save:
						#czyszczenie pliku "walls_v" i tworzenie pustej 
						#listy, w której przechowane będą dane do zapisu
						wall_v_data=[]
					for wall in walls_v:
						#Pobieranie danych położenia z istniejących
						#ścian pionowych i dodanie tych danych do listy
						data=wall.save()
						wall_v_data.append(data)
					with open("walls_v.json","a") as wall_v_save:
						#Zapisanie listy z danymi do pliku
						json.dump(wall_v_data,wall_v_save)
					with open("walls_h.json","w") as wall_h_save:
						#czyszczenie pliku "walls_h" i tworzenie pustej 
						#listy, w której przechowane będą dane do zapisu
						wall_h_data=[]
					for wall in walls_h:
						#Pobieranie danych położenia z istniejących
						#ścian poziomych i dodanie tych danych do listy
						data=wall.save()
						wall_h_data.append(data)
					with open("walls_h.json","a") as wall_h_save:
						#Zapisanie listy z danymi do pliku
						json.dump(wall_h_data,wall_h_save)
				elif load_button.rect.collidepoint(mouse_x,mouse_y):
					#Jeżeli zostanie klikniety przycisk "load", nastąpi
					#odczytanie zawartości plików z położeniem ścian
					with open("walls_v.json","r") as walls_v_load:
						#Usunięci wszytkich istniejących ścian 
						#pionowych i wczytanie zapisanego położenia 
						#ścian z pliku
						walls_v.empty()
						walls_v_positions=json.load(walls_v_load)
						for wall_v_position in walls_v_positions:
							#Tworzenie nowych ścian pionowych i 
							#przypisanie im położenia zgodnego z tym, 
							#który był zapisany w pliku
							wall_vertical=WallVertical(settings,screen)
							wall_vertical.rect.centerx=(
							wall_v_position[0])
							wall_vertical.rect.centery=(
							wall_v_position[1])
							walls_v.add(wall_vertical)
					with open("walls_h.json","r") as walls_h_load:
						#Usunięci wszytkich istniejących ścian 
						#pionowych i wczytanie zapisanego położenia 
						#ścian z pliku
						walls_h.empty()
						wall_h_positions=json.load(walls_h_load)
						for wall_h_position in wall_h_positions:
							#Tworzenie nowych ścian pionowych i 
							#przypisanie im położenia zgodnego z tym, 
							#który był zapisany w pliku
							wall_horizontal=WallHorizontal(settings,
							screen)
							wall_horizontal.rect.centerx=(
							wall_h_position[0])
							wall_horizontal.rect.centery=(
							wall_h_position[1])
							walls_h.add(wall_horizontal)
						
						
						
				#Jeżeli miejsce kliknięcia pokryje się ze ścianą,
				#zostanie ona usunięta
				skip_create=click_delete_wall(walls_h,walls_v,
				mouse_x,mouse_y)
				#Jeżeli nie nastąpiło usunięcie ściany a kliknięcie 
				#pokrywa się z niewidzialną śiatką, oznacza to że ściany
				#tam nie ma i może zostać dodana
				if skip_create!=True:
					click_create_wall(grid_walls_h,
					grid_walls_v,walls_h,walls_v,mouse_x,mouse_y,
					settings,screen)
def click_create_wall(grid_walls_h,grid_walls_v,walls_h,walls_v,mouse_x,
mouse_y,settings,screen):
	for wall in grid_walls_h:
		if wall.rect.collidepoint(mouse_x,mouse_y) == True:
			wall_h=WallHorizontal(settings,screen)
			wall_h.rect.centerx=wall.rect.centerx
			wall_h.rect.centery=wall.rect.centery
			walls_h.add(wall_h)
	for wall in grid_walls_v:
		if wall.rect.collidepoint(mouse_x,mouse_y) == True:
			wall_v=WallVertical(settings,screen)
			wall_v.rect.centerx=wall.rect.centerx
			wall_v.rect.centery=wall.rect.centery
			walls_v.add(wall_v)
def click_delete_wall(walls_h,walls_v,mouse_x,mouse_y):
	for wall in walls_h:
		if wall.rect.collidepoint(mouse_x,mouse_y) == True:
			wall.kill()
			return True
	for wall in walls_v:
		if wall.rect.collidepoint(mouse_x,mouse_y) == True:
			wall.kill()
			skip_create=True
			return True
def update_screen(walls_h,walls_v,player,screen,save_button,
load_button):
	"""Wyświetlenie obiektów i odświeżenie ekranu"""
	screen.fill((0,0,0))
	for wall in walls_h:
		wall.draw_wall()
	for wall in walls_v:
		wall.draw_wall()
	player.draw_player()
	save_button.draw_button()
	load_button.draw_button()
	pygame.display.flip()
