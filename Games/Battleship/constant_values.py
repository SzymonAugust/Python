import pygame

WIDTH = 1000				#główne wymiary
HEIGHT = 1000

BLACK = (0,0,0)				#kolory
WHITE = (255,255,255)
BLUE = (0,0,255)
DARK_BLUE = (0,0,150)
DARK_BLUE_2 = (0,0,100)

BUTTON_WIDTH = 250			#wymiary przycisków
BUTTON_HEIGHT = 125

BUTTON_WIDTH_B = 30
BUTTON_HEIGHT_B = 30

WIDTH_1_B = 340				#ustawienie plansz
HEIGHT_1_B = 290
WIDTH_1_E = 650
HEIGHT_1_E = 600

WIDTH_2_B = 150
HEIGHT_2_B = 300
WIDTH_2_E = 460
HEIGHT_2_E = 610

WIDTH_3_B = 530
HEIGHT_3_B = 300
WIDTH_3_E = 840
HEIGHT_3_E = 610
	
F1 = 80						#rozmiar tekstu
F2 = 60
F3 = 50
F4 = 120
F5 = 22
F6 = 25
F7 = 18

SHIP = pygame.image.load('ship.png')									#obrazki
SHIP = pygame.transform.scale(SHIP,(BUTTON_WIDTH_B,BUTTON_HEIGHT_B))
D_SHIP = pygame.image.load('ship_d.png')
D_SHIP = pygame.transform.scale(D_SHIP,(BUTTON_WIDTH_B,BUTTON_HEIGHT_B))
ANCHOR = pygame.image.load('anchor.png')
ANCHOR = pygame.transform.scale(ANCHOR,(BUTTON_WIDTH_B,BUTTON_HEIGHT_B))

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))						#tło, ekran
BACKGROUND = pygame.image.load('Sea.jpg')
DEFEAT = pygame.image.load('defeat.jpg')
VICTORY = pygame.image.load('victory.jpg')
VICTORY1 = pygame.image.load('victory1.jpg')
VICTORY2 = pygame.image.load('victory2.jpg')
SCREEN = pygame.display.get_surface()
