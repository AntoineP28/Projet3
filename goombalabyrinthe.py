#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Goomba Labyrinthe
Jeu dans lequel nous devons déplacer un goomba, afin de récupérer 3 objets placés aléatoirement dans le labyrinthe. Puis aller par la suite à la casquette, afin de terminer le niveau.

Script Python
Fichiers : goombalabyrinthe.py, classes.py, constantes.py, lab1, lab2 + images
"""

import pygame
from pygame.locals import *
import time

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
piece = pygame.image.load(image_pièce).convert_alpha()
coffre = pygame.image.load(image_coffre).convert_alpha()
potion = pygame.image.load(image_potion).convert_alpha()
victoire = pygame.image.load(image_victoire).convert_alpha()
défaite = pygame.image.load(image_défaite).convert()
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0 
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'lab1'		#On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_F2:
					continuer_accueil = 0
					choix = 'lab2'
			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Goomba
		gb = Perso("images/goomba_droite.png", "images/goomba_gauche.png", 
		"images/goomba_haut.png", "images/goomba_bas.png", niveau)
		objet1 = Item(piece, niveau)
		objet2 = Item(coffre, niveau)
		objet3 = Item(potion, niveau)

				
	#BOUCLE DE JEU
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
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(gb.direction, (gb.x, gb.y)) #gb.direction = l'image dans la bonne direction
		objet1.display(fenetre)
		objet2.display(fenetre)
		objet3.display(fenetre)
		pygame.display.flip()

		#Victoire -> Retour à l'accueil
		if niveau.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur == 3:
			print ("victoire")
			fenetre.blit(victoire, (25, 25))
			pygame.display.flip()
			time.sleep(3)
			continuer_jeu = 0
		elif niveau.structure[gb.case_y][gb.case_x] == 'a' and gb.compteur != 3:
			print("perdu")
			fenetre.blit(défaite, (10, 10))
			pygame.display.flip()
			time.sleep(3)
			continuer_jeu = 0