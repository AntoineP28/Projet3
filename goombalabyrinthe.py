#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Goomba Labyrinthe
Jeu dans lequel nous devons déplacer un goomba, afin de récupérer 3 objets placés aléatoirement dans le labyrinthe. Puis aller par la suite à la casquette, afin de terminer le niveau.

Script Python
Fichiers : goombalabyrinthe.py, classes.py, constantes.py, lab1, lab2 + images
"""

import pygame
from app.niveau import Niveau
from app.perso import Perso
from app.items import Item
from pygame.locals import *
import time

from constantes import *

def main():
	pygame.init()

	#Opening the Pygame window (square: width = height)
	window = pygame.display.set_mode((size_window, size_window))
	#Icon
	icon = pygame.image.load(picture_icon)
	piece = pygame.image.load(picture_pièce).convert_alpha()
	chest = pygame.image.load(picture_chest).convert_alpha()
	potion = pygame.image.load(picture_potion).convert_alpha()
	win = pygame.image.load(picture_win).convert_alpha()
	defeat = pygame.image.load(picture_defeat).convert()
	pygame.display.set_icon(icon)
	#Title
	pygame.display.set_caption(title_window)

	#Main loop
	continuer = 1
	while continuer:	
		#Loading and displaying the home screen
		home = pygame.image.load(picture_home).convert()
		window.blit(home, (0,0))

		#Refresh
		pygame.display.flip()

		#We reset these variables to 1 at each loop turn
		continue_game = 1
		continue_home = 1

		#WELCOME LOOP
		while continue_home:
		
			#Loop speed limitation
			pygame.time.Clock().tick(30)
		
			for event in pygame.event.get():
			
				#If the user exits, we put the variables 
				#loop to 0 to step through none and close
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continuer = 0 
					#Variable of choice of level
					choice = 0
					
				elif event.type == KEYDOWN:				
					#Level launch 1
					if event.key == K_F1:
						continue_home = 0	#We leave the reception
						choice = 'data/lab1'		#We define the level to load
					#Level launch 2
					elif event.key == K_F2:
						continue_home = 0
						choice = 'data/lab2'
				
			

		#we check that the player has made a choice of level
		#to not load if he leaves
		if choice != 0:
			#bottom loading
			fund = pygame.image.load(picture_fund).convert()

			#Generation of a level from a file
			level = Niveau(choice)
			level.generer()
			level.afficher(window)

			#character creation
			gb = Perso("images/goomba_droite.png", "images/goomba_gauche.png", 
			"images/goomba_haut.png", "images/goomba_bas.png", level)
			object1 = Item(piece, level)
			object2 = Item(chest, level)
			object3 = Item(potion, level)

					
		#GAME LOOP
		while continue_game:
		
			#Loop speed limitation
			pygame.time.Clock().tick(30)
		
			for event in pygame.event.get():
			
				#If the user exits, we put the variable that continues the game
				#AND the general variable to 0 to close the window
				if event.type == QUIT:
					continue_game = 0
					continuer = 0
			
				elif event.type == KEYDOWN:
					#If the user presses Esc here, we only return to the menu
					if event.key == K_ESCAPE:
						continue_game = 0
						
					#Goomba move keys
					elif event.key == K_RIGHT:
						gb.deplacer('droite')
					elif event.key == K_LEFT:
						gb.deplacer('gauche')
					elif event.key == K_UP:
						gb.deplacer('haut')
					elif event.key == K_DOWN:
						gb.deplacer('bas')	
				 
			#Displays at new positions
			window.blit(fund, (0,0))
			level.afficher(window)
			window.blit(gb.direction, (gb.x, gb.y)) #gb.direction = the picture in the right direction
			object1.display(window)
			object2.display(window)
			object3.display(window)
			pygame.display.flip()

			#Victory -> Back to Home
			if level.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur == 3:
				print ("victoire")
				window.blit(win, (25, 25))
				pygame.display.flip()
				time.sleep(3)
				continue_game = 0
			elif level.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur != 3:
				print("perdu")
				window.blit(defeat, (10, 10))
				pygame.display.flip()
				time.sleep(3)
				continue_game = 0

if __name__ == "__main__": 
    main() 
