import pygame,sys
from play_1 import *
from constant_values import *
from classes import *
from functions import *

TEXT = pygame.font.SysFont("sarai", F1)
TEXT_1 = pygame.font.SysFont("sarai", F3)

def returning():
	global run
	run = False

def play():
	global run
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

		SCREEN.blit(BACKGROUND, STARTING_POINT)

		green_snake_button = s_button(X_6,Y_6,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,0,SNAKES)
		blue_snake_button = s_button(X_7,Y_7,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,1,SNAKES)
		red_snake_button = s_button(X_8,Y_8,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,2,SNAKES)

		easy_level_button = s_button(X_10,Y_10,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,0,LEVELS)
		normal_level_button = s_button(X_11,Y_11,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,1,LEVELS)
		hard_level_button = s_button(X_12,Y_12,X_FRAME_2,Y_FRAME_2,WIDTH_3,HEIGHT_3,BLACK,WHITE,GREY,2,LEVELS)

		continue_button = button(X_13,Y_13,X_FRAME_2,Y_FRAME_2,WIDTH_4,HEIGHT_4,BLACK,WHITE,GREY,"CONTINUE",F3,play_1)
		return_button = button(X_4,Y_4,X_FRAME_2,Y_FRAME_2,WIDTH_2,HEIGHT_2,BLACK,WHITE,GREY,"RETURN",F2,returning)

		SCREEN.blit(S_B_G,(X_6+HEIGHT_3,Y_6))
		SCREEN.blit(S_B_B,(X_7+HEIGHT_3,Y_7))
		SCREEN.blit(S_B_R,(X_8+HEIGHT_3,Y_8))
		
		texting("Choose your snake!",TEXT,X_5,Y_5,WHITE)
		texting("Choose difficulty level!",TEXT,X_9,Y_9,WHITE)
		texting("EASY",TEXT_1,(2*X_10+WIDTH_3)/2,(2*Y_10+HEIGHT_3)/2,WHITE)
		texting("NORMAL",TEXT_1,(2*X_11+WIDTH_3)/2,(2*Y_11+HEIGHT_3)/2,WHITE)
		texting("HARD",TEXT_1,(2*X_12+WIDTH_3)/2,(2*Y_12+HEIGHT_3)/2,WHITE)

		pygame.display.flip()
