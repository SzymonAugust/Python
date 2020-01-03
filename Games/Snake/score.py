import pygame,sys
from constant_values import *
from classes import *
from functions import *

pygame.init()

TEXT = pygame.font.SysFont("sarai", F4)
TEXT1 = pygame.font.SysFont("sarai", F5)

def returning():
	global run
	run = False

def score():
	fields = []
	score_board = open("best_scores.txt","r")
	line = 0

	for level in score_board:
		fields.append(level.split(";"))
		fields[line].pop(len(fields[line])-1)
		line += 1

	global run
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		SCREEN.blit(BACKGROUND, STARTING_POINT)
		return_button = button(X_4,Y_4,X_FRAME_2,Y_FRAME_2,WIDTH_2,HEIGHT_2,BLACK,WHITE,GREY,"RETURN",F2,returning)
		
		texting("EASY",TEXT,X_17,Y_17,WHITE)
		texting("NORMAL",TEXT,X_18,Y_18,WHITE)
		texting("HARD",TEXT,X_19,Y_19,WHITE)

		for i in range(0,len(fields)):
			for j in range(0,len(fields[i]),2):
				texting(str(j//2+1)+". "+str(fields[i][j])+" " +str(fields[i][j+1]),TEXT1,X_20+i*D_X,Y_20+j*D_Y,WHITE)
		pygame.display.flip()
	score_board.close()
