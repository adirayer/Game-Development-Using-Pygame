import pygame,sys,os
from pygame.locals import *

catx=10
caty=10
screen=0

def myquit():
	''' Self Explanatory'''
	pygame.quit()
	sys.exit(0)

def check_inputs(events):
	global catx,caty,screen
	#function to handle events, particulatly quitting the program
	for event in events:
		if event.type==QUIT:
			quit()
		else:
			if event.type==KEYDOWN:
				if event.key==K_ESCAPE:
					myquit()
				elif event.key== K_LEFT:
					catx-=5
					print("move rect left")
				elif event.key==K_RIGHT:
					catx+=5
					print("move rect right")
				else:
					print(event.key)
	screen.fill((20,100,42))
	pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
	pygame.display.update()

def main():
	global screen
	#Initialize Pygame
	pygame.init()

	#setup screen
	SCREEN_WIDTH=600
	SCREEN_HEIGHT=480
	window=pygame.display.set_mode((1000,600))
	pygame.display.set_caption('slither.eat-The Snake Game')

	#set up drawing surface
	screen=pygame.display.get_surface() #this is where images are displayed

	pygame.display.update()

	while True:
		check_inputs(pygame.event.get())

main()