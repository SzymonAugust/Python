import pygame,sys
from datetime import *
from time import sleep
from constant_values import *
from classes import *
from functions import *

TEXT = pygame.font.SysFont("sarai", F1)
TEXT1 = pygame.font.SysFont("sarai", F3)

def colourSnake():
	if SNAKES[0] == 1:
		return pygame.transform.scale(S_B_G,(FIELD_SIDE,FIELD_SIDE))
	elif SNAKES[1] == 1:
		return pygame.transform.scale(S_B_B,(FIELD_SIDE,FIELD_SIDE))
	elif SNAKES[2] == 1:
		return pygame.transform.scale(S_B_R,(FIELD_SIDE,FIELD_SIDE))

def play_1():
	fields = []
	score_board = open("best_scores.txt","r+")
	line = 0

	for level in score_board:
		fields.append(level.split(";"))
		fields[line].pop(len(fields[line])-1)
		line += 1

	score_board = open("best_scores.txt","w")

	refresh_time = LEVELS[0]*EASY_TIME+LEVELS[1]*NORMAL_TIME+LEVELS[2]*HARD_TIME
	point_coefficient = LEVELS[0]*2+LEVELS[1]*1.5+LEVELS[2]*1
	SNAKE_IMAGE = colourSnake()
	s = snake((0,7),SNAKE_IMAGE)
	snack = cube(randomSnack(BOARD_WIDTH,BOARD_HEIGHT,s),PREY_IMAGE)
	while True:
		score = round((len(s.body)-1)*POINTS*point_coefficient)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		if s.body[0].pos == snack.pos:
			s.addCube()
			snack = cube(randomSnack(BOARD_WIDTH,BOARD_HEIGHT,s),PREY_IMAGE)

		SCREEN.blit(BACKGROUND, STARTING_POINT)
		pygame.draw.rect(SCREEN,WHITE,(X_14-X_FRAME_1,Y_14-Y_FRAME_1,FIELD_SIDE*BOARD_WIDTH+2*X_FRAME_1,FIELD_SIDE*BOARD_HEIGHT+2*Y_FRAME_1))
		pygame.draw.rect(SCREEN,BLACK,(X_14,Y_14,FIELD_SIDE*BOARD_WIDTH,FIELD_SIDE*BOARD_HEIGHT))
		texting("Your score: " + str(score),TEXT,X_15,Y_15,WHITE)
		texting("Use 'WASD' to move the snake!",TEXT1,X_16,Y_16,WHITE)
		texting("You can slide through walls!",TEXT1,X_22,Y_22,WHITE)
		snack.draw()
		s.draw()
		s.move()
		pygame.display.flip()
		if s.crashCheck():
			score_level = LEVELS[1]*1+LEVELS[2]*2
			if score > int(fields[score_level][len(fields[score_level])-1]):
				for i in range (0,len(fields[score_level]),2):
					if score > int(fields[score_level][i+1]):
						fields[score_level][len(fields[score_level])-2] = str(date.today())
						fields[score_level][len(fields[score_level])-1] = str(score)
						for j in range (len(fields[score_level])-1,i+2,-2):
							tmp1 = fields[score_level][j]
							tmp2 = fields[score_level][j-1]
							fields[score_level][j] = fields[score_level][j-2]
							fields[score_level][j-1] = fields[score_level][j-3]
							fields[score_level][j-2] = tmp1
							fields[score_level][j-3] = tmp2
						break

			for i in range(0,len(fields)):
				for j in range (0,len(fields[i])):
					score_board.write(str(fields[i][j])+str(";"))
				score_board.write('\n')
			s.reset()
			sleep(1)
			score_board.close()
			break
		sleep(refresh_time)
		
		
	
