import pygame,sys
from score import *
from play import *
from constant_values import *
from classes import *
from functions import *

pygame.init()
pygame.display.set_caption('Snake')

ALL_FONTS = pygame.font.get_fonts()

pygame.mixer.music.load("Swedish House Mafia - Greyhound.mp3")
pygame.mixer.music.play(-1)

def main():
	
	while True:
		SCREEN.blit(BACKGROUND, STARTING_POINT)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)

		play_button = button(X_1,Y_1,X_FRAME_1,Y_FRAME_1,WIDTH_1,HEIGHT_1,BLACK,WHITE,GREY,"PLAY",F1,play)
		leaderboard_button = button(X_2,Y_2,X_FRAME_1,Y_FRAME_1,WIDTH_1,HEIGHT_1,BLACK,WHITE,GREY,"SCORE",F1,score)
		quit_button = button(X_3,Y_3,X_FRAME_1,Y_FRAME_1,WIDTH_1,HEIGHT_1,BLACK,WHITE,GREY,"QUIT",F1,quit)
		
		pygame.display.flip()

main()
