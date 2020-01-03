import pygame
from constant_values import *
from random import *

def text_objects(text,font,colour):
	textSur = font.render(text, True, colour)
	return textSur, textSur.get_rect()

def texting(text,font,width,height,colour):
	textSurf, textRect = text_objects(text, font, colour)
	textRect.center = (width,height)
	SCREEN.blit(textSurf,textRect)

def randomSnack(n1,n2,item):
	positions = item.body

	while True:
		x = randrange(n1)
		y = randrange(n2)
		if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
			continue
		else:
			break
        
	return (x,y)
