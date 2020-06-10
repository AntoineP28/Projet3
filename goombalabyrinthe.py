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
	fenetre = pygame.display.set_mode((size_window, size_window))
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
		fenetre.blit(home, (0,0))

		#Refresh
		pygame.display.flip()

		#We reset these variables to 1 at each loop turn
		continuer_jeu = 1
		continuer_accueil = 1

		#WELCOME LOOP
		while continuer_accueil:
		
			#Loop speed limitation
			pygame.time.Clock().tick(30)
		
			for event in pygame.event.get():
			
				#If the user exits, we put the variables 
				#loop to 0 to step through none and close
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continuer_accueil = 0
					continuer_jeu = 0
					continuer = 0 
					#Variable of choice of level
					choix = 0
					
				elif event.type == KEYDOWN:				
					#Lancement du niveau 1
					if event.key == K_F1:
						continuer_accueil = 0	#We leave the reception
						choix = 'data/lab1'		#We define the level to load
					#Lancement du niveau 2
					elif event.key == K_F2:
						continuer_accueil = 0
						choix = 'data/lab2'
				
			

		#we check that the player has made a choice of level
		#to not load if he leaves
		if choix != 0:
			#Chargement du fond
			fund = pygame.image.load(picture_fund).convert()

			#Generation of a level from a file
			niveau = Niveau(choix)
			niveau.generer()
			niveau.afficher(fenetre)

			#character creation
			gb = Perso("images/goomba_droite.png", "images/goomba_gauche.png", 
			"images/goomba_haut.png", "images/goomba_bas.png", niveau)
			object1 = Item(piece, niveau)
			object2 = Item(chest, niveau)
			object3 = Item(potion, niveau)

					
		#GAME LOOP
		while continuer_jeu:
		
			#Limitation de vitesse de la boucle
			pygame.time.Clock().tick(30)
		
			for event in pygame.event.get():
			
				#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
				if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0
			
				elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
					if event.key == K_ESCAPE:
						continuer_jeu = 0
						
					#Touches de déplacement de Goomba
					elif event.key == K_RIGHT:
						gb.deplacer('droite')
					elif event.key == K_LEFT:
						gb.deplacer('gauche')
					elif event.key == K_UP:
						gb.deplacer('haut')
					elif event.key == K_DOWN:
						gb.deplacer('bas')	
				
			#Affichages aux nouvelles positions
			fenetre.blit(fund, (0,0))
			niveau.afficher(fenetre)
			fenetre.blit(gb.direction, (gb.x, gb.y)) #gb.direction = l'image dans la bonne direction
			object1.display(fenetre)
			object2.display(fenetre)
			object3.display(fenetre)
			pygame.display.flip()

			#Victoire -> Retour à l'accueil
			if niveau.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur == 3:
				print ("victoire")
				fenetre.blit(win, (25, 25))
				pygame.display.flip()
				time.sleep(3)
				continuer_jeu = 0
			elif niveau.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur != 3:
				print("perdu")
				fenetre.blit(defeat, (10, 10))
				pygame.display.flip()
				time.sleep(3)
				continuer_jeu = 0

if __name__ == "__main__": 
    main() 
