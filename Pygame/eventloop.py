import pygame,sys,os
from pygame.locals import *

blue=[0,0,255]

#initialise pygame
pygame.init()

#setup window
DISPSURF=pygame.display.set_mode((1000,600))
pygame.display.set_caption('slither.eat-The Snake Game')

#set up drawing surface
screen=pygame.display.get_surface()
screen.fill(blue)
pygame.display.set_caption("Snake")
pygame.display.flip()

count=0

while True:
#main game loop
	for event in pygame.event.get():
		print(event)
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	