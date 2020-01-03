import pygame, random, sys
from constant_values import *
from time import sleep
from pygame.locals import *
from functions import *
pygame.init()
random.seed()
TEXT1 = pygame.font.SysFont("sarai", F1)
TEXT2 = pygame.font.SysFont("sarai", F2)
TEXT3 = pygame.font.SysFont("sarai", F3)
TEXT4 = pygame.font.SysFont("sarai", F4)
TEXT5 = pygame.font.SysFont("sarai", F5)
TEXT6 = pygame.font.SysFont("samanata", F6)
TEXT7 = pygame.font.SysFont("samanata", F7)
player_one_list = [[]for i in range(0,10)]				#plansza 1. gracza
player_two_list = [[]for i in range(0,10)]				#plansza 2. gracza

for i in range(0,10):
	for j in range(0,10):
		player_one_list[i].append(0)
		player_two_list[i].append(0)

def draw_player_1():					#wypełnianie planszy 1. gracza
	sleep(0.1)
	counter = 0			#liczy, ile jest ustawionych statków
	for i in range(0,10):
		for j in range(0,10):
			player_one_list[i][j] = 0
			
	while counter < 1:			#rysowanie czteromasztowca
		counter += 1	
		x1, y1 = random_position(0,9)
		player_one_list[x1][y1] = 1
		set_4ship(player_one_list,x1,y1)
		give_2(player_one_list)

	while counter < 3:					#rysowanie dwóch trójmasztowców
		x2, y2 = random_position(0,9)
		if neighbour(player_one_list, x2, y2,1) == 0 and player_one_list[x2][y2] == 0:
			player_one_list[x2][y2] = 1				
			if (set_3ship(player_one_list,x2,y2,random_direction(x2,y2,2))):
				counter += 1
				give_2(player_one_list)
			else:
				player_one_list[x2][y2] = 0

	while counter < 6:						#rysowanie trzech dwumasztowców
		x3, y3 = random_position(0,9)
		if neighbour(player_one_list, x3, y3,1) == 0 and player_one_list[x3][y3] == 0:
			player_one_list[x3][y3] = 1				
			if (set_2ship(player_one_list,x3,y3,random_direction(x3,y3,1))):
				counter += 1
				give_2(player_one_list)
			else:
				player_one_list[x3][y3] = 0

	while counter < 10:						#rysowanie czterech jednomasztowców
		x4, y4 = random_position(0,9)
		if neighbour(player_one_list, x4, y4,1) == 0 and player_one_list[x4][y4] == 0:
			player_one_list[x4][y4] = 1				
			counter += 1
			give_2(player_one_list)

def draw_player_2():				#wypełnianie planszy 2. gracza
	sleep(0.1)
	counter = 0						#liczy, ile jest ustawionych statków
	for i in range(0,10):
		for j in range(0,10):
			player_two_list[i][j] = 0

	while counter < 1:					#rysowanie czteromasztowca
		counter += 1	
		x1, y1 = random_position(0,9)
		player_two_list[x1][y1] = 1
		set_4ship(player_two_list,x1,y1)
		give_2(player_two_list)

	while counter < 3:					#rysowanie dwóch trójmasztowców
		x2, y2 = random_position(0,9)
		if neighbour(player_two_list, x2, y2,1) == 0 and player_two_list[x2][y2] == 0:
			player_two_list[x2][y2] = 1				
			if (set_3ship(player_two_list,x2,y2,random_direction(x2,y2,2))):
				counter += 1
				give_2(player_two_list)
			else:
				player_two_list[x2][y2] = 0

	while counter < 6:						#rysowanie trzech dwumasztowców
		x3, y3 = random_position(0,9)
		if neighbour(player_two_list, x3, y3,1) == 0 and player_two_list[x3][y3] == 0:
			player_two_list[x3][y3] = 1				
			if (set_2ship(player_two_list,x3,y3,random_direction(x3,y3,1))):
				counter += 1
				give_2(player_two_list)
			else:
				player_two_list[x3][y3] = 0

	while counter < 10:					#rysowanie czterech jednomasztowców 
		x4, y4 = random_position(0,9)
		if neighbour(player_two_list, x4, y4,1) == 0 and player_two_list[x4][y4] == 0:
			player_two_list[x4][y4] = 1				
			counter += 1
			give_2(player_two_list)

def endgame1():						#zwycięstwo gracza nr 1
	pygame.mixer.music.stop
	pygame.mixer.music.load('win.mp3')
	pygame.mixer.music.play(-1)
	while True:
		input(pygame.event.get())
		SCREEN.blit(VICTORY1, (0,0))

		button_main(SCREEN, WIDTH/8, WIDTH*3/8, HEIGHT*6.5/8, HEIGHT*7.5/8, BLACK, BLACK, game2P)
		button_main(SCREEN, WIDTH*5/8, WIDTH*7/8, HEIGHT*6.5/8, HEIGHT*7.5/8, BLACK, BLACK, quit)

		texting("REPLAY", TEXT2 ,WIDTH/4,HEIGHT*7/8, WHITE)
		texting("QUIT", TEXT2 ,WIDTH*3/4,HEIGHT*7/8, WHITE)

		pygame.display.flip()

def endgame1():						#zwycięstwo gracza nr 2
	pygame.mixer.music.stop
	pygame.mixer.music.load('win.mp3')
	pygame.mixer.music.play(-1)
	while True:
		input(pygame.event.get())
		SCREEN.blit(VICTORY2, (0,0))

		button_main(SCREEN, WIDTH/8, WIDTH*3/8, HEIGHT*6.5/8, HEIGHT*7.5/8, BLACK, BLACK, game2P)
		button_main(SCREEN, WIDTH*5/8, WIDTH*7/8, HEIGHT*6.5/8, HEIGHT*7.5/8, BLACK, BLACK, quit)

		texting("REPLAY", TEXT2 ,WIDTH/4,HEIGHT*7/8, WHITE)
		texting("QUIT", TEXT2 ,WIDTH*3/4,HEIGHT*7/8, WHITE)

		pygame.display.flip()

def Continue2():			#rozgrywka między graczami
	while True:
		input(pygame.event.get())
		SCREEN.blit(BACKGROUND, (0,0))

		texting("START THE BATTLE!", TEXT4, WIDTH/2, HEIGHT*0.5/8, BLACK)
		texting("CAPTAIN 1", TEXT1, WIDTH_2_B+5*(BUTTON_WIDTH_B+2), HEIGHT*2.5/10, BLACK)
		texting("CAPTAIN 2", TEXT1, WIDTH_3_B+5*(BUTTON_WIDTH_B+2), HEIGHT*2.5/10, BLACK)

		counter1 = 0					#pozostałe pola ze statkami 1. gracza
		counter2 = 0					#pozostałe pola ze statkami 2. gracza
		player1_hits = 0				#liczba strzałów 1. gracza
		player2_hits = 0				#liczba strzałów 2. gracza

		for i in range (0,10):
			counter1 += player_one_list[i].count(1)
			counter2 += player_two_list[i].count(1)
			player1_hits += player_two_list[i].count(-1)
			player1_hits += player_two_list[i].count(-2)
			player2_hits += player_one_list[i].count(-1)
			player2_hits += player_one_list[i].count(-2)
		
		texting("FIRST FLEET'S POWER: " + str(counter1), TEXT6, WIDTH_2_B+5*(BUTTON_WIDTH_B+2), HEIGHT*7/10, BLACK)
		texting("SECOND FLEET'S POWER: " + str(counter2), TEXT6, WIDTH_3_B+5*(BUTTON_WIDTH_B+2), HEIGHT*7/10, BLACK)
		texting("Click on a square to shoot!", TEXT7, WIDTH/2, HEIGHT*7.5/10, BLACK)
		texting("If you hit enemy's ship, you'll see this picture: ", TEXT7, WIDTH/2, HEIGHT*8/10, BLACK)
		SCREEN.blit(D_SHIP,(WIDTH*7/8,HEIGHT*7.8/10))
		texting("If your shoot misses the target, you'll see this picture: ", TEXT7, WIDTH/2, HEIGHT*8.5/10, BLACK)
		SCREEN.blit(ANCHOR,(WIDTH*7/8,HEIGHT*8.35/10))
		texting("Each fleet consists of one four-master, two three-masters, three two-masters and four one-masters", TEXT7, WIDTH/2, HEIGHT*9/10, BLACK)
		texting("1 x", TEXT7, WIDTH*2/10, HEIGHT*9.5/10, BLACK)
		for i in range(0,4):
			SCREEN.blit(SHIP,(WIDTH*2.25/10+i*0.30*WIDTH/10,HEIGHT*9.30/10))
		texting("2 x", TEXT7, WIDTH*4/10, HEIGHT*9.5/10, BLACK)
		for i in range(0,3):
			SCREEN.blit(SHIP,(WIDTH*4.25/10+i*0.30*WIDTH/10,HEIGHT*9.30/10))
		texting("3 x", TEXT7, WIDTH*6/10, HEIGHT*9.5/10, BLACK)
		for i in range(0,2):
			SCREEN.blit(SHIP,(WIDTH*6.25/10+i*0.30*WIDTH/10,HEIGHT*9.30/10))
		texting("4 x", TEXT7, WIDTH*8/10, HEIGHT*9.5/10, BLACK)
		SCREEN.blit(SHIP,(WIDTH*8.25/10,HEIGHT*9.30/10))
		
		if counter1 == 0:
			sleep(0.2)
			endgame2()

		if counter2 == 0:
			sleep(0.2)
			endgame1()

		empty_button(SCREEN, WIDTH_2_B-3, WIDTH_2_E+12, HEIGHT_2_B-3, HEIGHT_2_E+12, BLACK)
		for board_h in range (HEIGHT_2_B, HEIGHT_2_E, BUTTON_HEIGHT_B+2):
			for board_w in range (WIDTH_2_B, WIDTH_2_E, BUTTON_WIDTH_B+2):
				button_1(SCREEN, board_w, board_w + BUTTON_WIDTH_B, board_h, board_h + BUTTON_HEIGHT_B, BLUE, DARK_BLUE, hit_by_player, player_one_list,(board_h-HEIGHT_2_B-2)//(BUTTON_WIDTH_B+2)+1,(board_w-WIDTH_2_B-2)//(BUTTON_HEIGHT_B+2)+1,player1_hits,player2_hits)
				if player_one_list[(board_h-HEIGHT_2_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_2_B-2)//(BUTTON_HEIGHT_B+2)+1] == -1:
					SCREEN.blit(D_SHIP,(board_w,board_h)) #pokaż zniszczony statek
				if player_one_list[(board_h-HEIGHT_2_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_2_B-2)//(BUTTON_HEIGHT_B+2)+1] == -2:
					SCREEN.blit(ANCHOR,(board_w,board_h)) #pokaż kotwicę
		
		empty_button(SCREEN, WIDTH_3_B-3, WIDTH_3_E+12, HEIGHT_2_B-3, HEIGHT_2_E+12, BLACK)
		for board_h in range (HEIGHT_3_B, HEIGHT_3_E, BUTTON_HEIGHT_B+2):
			for board_w in range (WIDTH_3_B, WIDTH_3_E, BUTTON_WIDTH_B+2):
				button_2(SCREEN, board_w, board_w + BUTTON_WIDTH_B, board_h, board_h + BUTTON_HEIGHT_B, BLUE, DARK_BLUE, hit_by_player, player_two_list,(board_h-HEIGHT_3_B-2)//(BUTTON_WIDTH_B+2)+1,(board_w-WIDTH_3_B-2)//(BUTTON_HEIGHT_B+2)+1,player1_hits,player2_hits)
				if player_two_list[(board_h-HEIGHT_3_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_3_B-2)//(BUTTON_HEIGHT_B+2)+1] == -1:
					SCREEN.blit(D_SHIP,(board_w,board_h)) #pokaż zniszczony statek
				if player_two_list[(board_h-HEIGHT_3_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_3_B-2)//(BUTTON_HEIGHT_B+2)+1] == -2:
					SCREEN.blit(ANCHOR,(board_w,board_h)) #pokaż kotwicę 

		pygame.display.flip()

def Continue1():	#wybór ustawienia przez 2. gracza
	draw_player_2()
	sleep(0.5)
	while True:
		input(pygame.event.get())
		SCREEN.blit(BACKGROUND, (0,0))

		empty_button(SCREEN, WIDTH_1_B-3, WIDTH_1_E+12, HEIGHT_1_B-3, HEIGHT_1_E+12, BLACK)

		texting("Captain Two, your turn!", TEXT1, WIDTH/2, HEIGHT*0.75/8, BLACK)	
		texting("To reset ships' positions, click \"RESET\" button", TEXT3, WIDTH/2, HEIGHT*1.5/8, BLACK)

		for board_h in range (HEIGHT_1_B, HEIGHT_1_E, BUTTON_HEIGHT_B+2):
			for board_w in range (WIDTH_1_B, WIDTH_1_E, BUTTON_WIDTH_B+2):
				button_main(SCREEN, board_w, board_w + BUTTON_WIDTH_B, board_h, board_h + BUTTON_HEIGHT_B, BLUE, DARK_BLUE, None)
				if player_two_list[(board_h-HEIGHT_1_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_1_B-2)//(BUTTON_HEIGHT_B+2)+1] == 1:
					SCREEN.blit(SHIP,(board_w,board_h))	#pokaż statek
		
		button_main(SCREEN, WIDTH/8, WIDTH*3/8, HEIGHT*5.25/8, HEIGHT*6.25/8, BLUE, DARK_BLUE, Continue2)		#przejście dalej
		button_main(SCREEN, WIDTH*5/8, WIDTH*7/8, HEIGHT*5.25/8, HEIGHT*6.25/8, BLUE, DARK_BLUE,draw_player_2)	#losowanie planszy raz jeszcze

		texting("CONTINUE", TEXT2 ,WIDTH/4,HEIGHT*5.75/8, BLACK)
		texting("RESET", TEXT2 ,WIDTH*3/4,HEIGHT*5.75/8, BLACK)
		texting("Don't let Captain One look at screen!", TEXT2, WIDTH/2, HEIGHT*7/8, BLACK)
		
		pygame.display.flip()

def game2P():									#podtrzymywanie gry w wariancie dla 2 graczy; wybór ustawienia przez 1. gracza											
	pygame.mixer.music.load('Pirates.mp3') 
	pygame.mixer.music.play(-1)
	
	draw_player_1()
	while True:
		input(pygame.event.get())
		SCREEN.blit(BACKGROUND, (0,0))

		empty_button(SCREEN, WIDTH_1_B-3, WIDTH_1_E+12, HEIGHT_1_B-3, HEIGHT_1_E+12, BLACK)

		texting("Captain One, choose your positions!", TEXT1, WIDTH/2, HEIGHT*0.75/8, BLACK)	
		texting("To reset ships' positions, click \"RESET\" button", TEXT3, WIDTH/2, HEIGHT*1.5/8, BLACK)

		for board_h in range (HEIGHT_1_B, HEIGHT_1_E, BUTTON_HEIGHT_B+2):
			for board_w in range (WIDTH_1_B, WIDTH_1_E, BUTTON_WIDTH_B+2):
				button_main(SCREEN, board_w, board_w + BUTTON_WIDTH_B, board_h, board_h + BUTTON_HEIGHT_B, BLUE, DARK_BLUE, None)
				if player_one_list[(board_h-HEIGHT_1_B-2)//(BUTTON_WIDTH_B+2)+1][(board_w-WIDTH_1_B-2)//(BUTTON_HEIGHT_B+2)+1] == 1:
					SCREEN.blit(SHIP,(board_w,board_h))	#pokaż statek
		
		button_main(SCREEN, WIDTH/8, WIDTH*3/8, HEIGHT*5.25/8, HEIGHT*6.25/8, BLUE, DARK_BLUE,Continue1)		#przejście dalej
		button_main(SCREEN, WIDTH*5/8, WIDTH*7/8, HEIGHT*5.25/8, HEIGHT*6.25/8, BLUE, DARK_BLUE,draw_player_1)	#losowanie planszy raz jeszcze 

		texting("CONTINUE", TEXT2 ,WIDTH/4,HEIGHT*5.75/8, BLACK)
		texting("RESET", TEXT2 ,WIDTH*3/4,HEIGHT*5.75/8, BLACK)
		texting("Don't let Captain Two look at screen!", TEXT2, WIDTH/2, HEIGHT*7/8, BLACK)
		
		pygame.display.flip()
