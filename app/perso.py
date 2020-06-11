import pygame
from pygame.locals import * 
from constantes import *

class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, right, left, high, downs, level):
		#Character Sprites
		self.right = pygame.image.load(right).convert_alpha()
		self.left = pygame.image.load(left).convert_alpha()
		self.high = pygame.image.load(high).convert_alpha()
		self.downs = pygame.image.load(downs).convert_alpha()
		#Character position in boxes and pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Default direction
		self.direction = self.right
		#Level the character is in
		self.level = level
		self.compteur = 0
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Move right
		if direction == 'droite':
			#To not go beyond the screen
			if self.case_x < (number_sprite_size - 1):
				#We check that the destination box is not a wall
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					#Move a cell
					self.case_x += 1
					#Calculation of the "real" position in pixels
					self.x = self.case_x * size_sprite
			#Picture in the right direction
			self.direction = self.right
		
		#Move left
		if direction == 'gauche':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * size_sprite
			self.direction = self.left
		
		#Move up
		if direction == 'haut':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * size_sprite
			self.direction = self.high
		
		#Move down
		if direction == 'bas':
			if self.case_y < (number_sprite_size - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * size_sprite
			self.direction = self.downs

		if self.level.structure[self.case_y][self.case_x] == 'i':
			self.compteur += 1
			self.level.structure[self.case_y][self.case_x] = '0'
			print(self.compteur)