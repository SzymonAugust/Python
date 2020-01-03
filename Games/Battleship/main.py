import pygame,sys
from constant_values import *
from pygame.locals import *
from functions import *
from OnePlayer import *
from TwoPlayers import *

pygame.init()
all_fonts = pygame.font.get_fonts()
TEXT = pygame.font.SysFont("sarai", F3)

pygame.display.set_caption('Statki')
SCREEN.blit(BACKGROUND, (0,0))

while True:
	input(pygame.event.get())

	button_main(SCREEN, (WIDTH-BUTTON_WIDTH)/2, (WIDTH-BUTTON_WIDTH)/2 + BUTTON_WIDTH, 200, 325, BLUE, DARK_BLUE, game2P)	#tryb gry dla dwóch graczy
	button_main(SCREEN, (WIDTH-BUTTON_WIDTH)/2, (WIDTH-BUTTON_WIDTH)/2 + BUTTON_WIDTH, 450, 575, BLUE, DARK_BLUE, game1P) 	#tryb gry dla jednego gracza
	button_main(SCREEN, (WIDTH-BUTTON_WIDTH)/2, (WIDTH-BUTTON_WIDTH)/2 + BUTTON_WIDTH, 700, 825, BLUE, DARK_BLUE, quit)		#wyjście

	texting("2 PLAYERS", TEXT, (WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH/2, 200+BUTTON_HEIGHT/2, BLACK)
	texting("1 PLAYER", TEXT, (WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH/2, 450+BUTTON_HEIGHT/2, BLACK)
	texting("EXIT", TEXT, (WIDTH-BUTTON_WIDTH)/2+BUTTON_WIDTH/2, 700+BUTTON_HEIGHT/2, BLACK)

	pygame.display.flip()
