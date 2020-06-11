import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#We open the file
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#We browse the lines of the file
			for ligne in fichier:
				ligne_niveau = []
				#We browse the sprites (letters) contained in the file
				for sprite in ligne:
					#We ignore the "\ n" at the end of the line
					if sprite != '\n':
						#We add the sprite to the line list
						ligne_niveau.append(sprite)
				#We add the line to the level list
				structure_niveau.append(ligne_niveau)
			#We save this structure
			self.structure = structure_niveau

	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Loading images (only the arrival one contains transparency)
		mur = pygame.image.load(picture_mur).convert()
		depart = pygame.image.load(picture_depart).convert()
		arrivee = pygame.image.load(picture_arrivee).convert_alpha()
		piece = pygame.image.load(picture_pièce).convert()
		chest = pygame.image.load(picture_chest).convert()
		potion = pygame.image.load(picture_potion).convert()
		
		#We browse the level list
		num_ligne = 0
		for ligne in self.structure:
			#We browse the line lists
			num_case = 0
			for sprite in ligne:
				#We calculate the actual position in pixels
				x = num_case * size_sprite
				y = num_ligne * size_sprite
				if sprite == 'm':		   #m = wall
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Departure
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrival
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
				
		