import pygame,sys,os
from pygame.locals import *

blue=[0,0,255]

#initialise pygame
pygame.init()

#setup window
window=pygame.display.set_mode((1000,600))
pygame.display.set_caption('slither.eat-The Snake Game')

#set up drawing surface
screen=pygame.display.get_surface()
screen.fill(blue)
pygame.display.set_caption("Snake")
pygame.display.flip()

count=0

while True:
	print("Slither.eat-The Snake Game!")
	pass