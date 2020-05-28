import pygame
from pygame.locals import * 
from constantes import *
import random

						
			
			


class Item:
		

	def __init__(self, image,level):
		self.image = image
		self.level = level
		self.case_x, self.case_y = self.random_object()
		self.x = 30 * self.case_x
		self.y = 30 * self.case_y
		self.level.structure[self.case_y][self.case_x] = 'i'
	def random_object(self):
		x = random.randint(1,14)
		y = random.randint(1,14)
		while self.level.structure[y][x] != '0':
			x = random.randint(1,14)
			y = random.randint(1,14)
		return x, y
	def display(self, fenetre):
		if self.level.structure[self.case_y][self.case_x] == 'i':
			fenetre.blit(self.image, (self.x,self.y))