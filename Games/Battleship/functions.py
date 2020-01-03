import pygame,sys,random
from constant_values import *
from pygame.locals import *
from time import sleep

def button_main(surface, width_b, width_e, height_b, height_e, colour, m_colour, action):		#tworzenie przycisku zwykłego
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (width_b < mouse[0] <  width_e and height_b < mouse[1] < height_e):
		pygame.draw.rect(surface,m_colour,(width_b,height_b,width_e-width_b,height_e-height_b))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))			

def button_level(surface, width_b, width_e, height_b, height_e, colour, m_colour, a, level):				#tworzenie przycisku do wyboru poziomu trudności
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))
	if level[a] == 1:
		pygame.draw.rect(surface,m_colour,(width_b,height_b,width_e-width_b,height_e-height_b))
	if (width_b < mouse[0] <  width_e and height_b < mouse[1] < height_e and click[0] == 1):
		for i in range (0,3):
			level[i] = 0
		level[a] = 1
	

def button(surface, width_b, width_e, height_b, height_e, colour, m_colour, action,ar,index1,index2):		#tworzenie przycisku do gry - jeden gracz
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (width_b < mouse[0] <  width_e and height_b < mouse[1] < height_e):
		pygame.draw.rect(surface,m_colour,(width_b,height_b,width_e-width_b,height_e-height_b))
		if click[0] == 1 and action == hit_by_player:		
			sleep(0.2)			
			hit_by_player(ar,index1,index2)
		elif click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))

def button_1(surface, width_b, width_e, height_b, height_e, colour, m_colour, action,ar,index1,index2,a,b):		#tworzenie przycisku do gry - (1/2) graczy
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (width_b < mouse[0] <  width_e and height_b < mouse[1] < height_e):
		pygame.draw.rect(surface,m_colour,(width_b,height_b,width_e-width_b,height_e-height_b))
		if click[0] == 1 and action == hit_by_player and a == b+1:		
			sleep(0.2)			
			hit_by_player(ar,index1,index2)
		elif click[0] == 1 and action != None and action != hit_by_player:
			action()
	else:
		pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))

def button_2(surface, width_b, width_e, height_b, height_e, colour, m_colour, action,ar,index1,index2,a,b):		#tworzenie przycisku do gry - (2/2) graczy
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (width_b < mouse[0] <  width_e and height_b < mouse[1] < height_e):
		pygame.draw.rect(surface,m_colour,(width_b,height_b,width_e-width_b,height_e-height_b))
		if click[0] == 1 and action == hit_by_player and a == b:		
			sleep(0.2)			
			hit_by_player(ar,index1,index2)
		elif click[0] == 1 and action != None and action != hit_by_player:
			action()
	else:
		pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))
		
def empty_button(surface, width_b, width_e, height_b, height_e, colour):								#przycisk, który nic nie robi
	pygame.draw.rect(surface,colour,(width_b,height_b,width_e-width_b,height_e-height_b))

def texting(text,font,width,height,colour):					#napisy na przycisku
	textSurf, textRect = text_objects(text, font, colour)
	textRect.center = (width,height)
	SCREEN.blit(textSurf,textRect)

def input(events):										#wyłączanie gry
	for event in events:
		if event.type == QUIT:
			sys.exit(0)

def text_objects(text, font,colour):							#napis jako obiekt
	textSur = font.render(text, True, colour)
	return textSur, textSur.get_rect()

def neighbour(x,index1,index2,t):										#sprawdzanie, czy punkt na planszy ma sąsiada równego t
	y = 0		
	if index1 == 0 or index1 == 9:
		if index2 == 0:
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1+1][index2+1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1-1][index2+1] == t:
					y = 1
		elif index2 == 9:
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
				if x[index1+1][index2-1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
				if x[index1-1][index2-1] == t:
					y = 1
		else: # 0 < index2 < 9
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
				if x[index1+1][index2+1] == t:
					y = 1
				if x[index1+1][index2-1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
				if x[index1-1][index2-1] == t:
					y = 1
				if x[index1-1][index2+1] == t:
					y = 1
	elif (index1 != 0 and index1 != 9 and (index2 == 0 or index2 == 9)):
		if index2 == 0:
			if x[index1+1][index2] == t:
				y = 1
			if x[index1-1][index2] == t:
				y = 1
			if x[index1][index2+1] == t:
				y = 1
			if x[index1+1][index2+1] == t:
				y = 1
			if x[index1-1][index2+1] == t:
				y = 1
		else: #index2 == 9
			if x[index1+1][index2] == t:
				y = 1
			if x[index1-1][index2] == t:
				y = 1
			if x[index1][index2-1] == t:
				y = 1
			if x[index1+1][index2-1] == t:
				y = 1
			if x[index1-1][index2-1] == t:
				y = 1
	else:		
		if x[index1+1][index2] == t:
			y = 1
		if x[index1-1][index2] == t:
			y = 1
		if x[index1][index2-1] == t:
			y = 1
		if x[index1][index2+1] == t:
			y = 1
		if x[index1+1][index2+1] == t:
			y = 1
		if x[index1-1][index2+1] == t:
			y = 1
		if x[index1-1][index2-1] == t:
			y = 1
		if x[index1+1][index2-1] == t:
			y = 1
	return y
	
def neighbour_wh(x,index1,index2,t):										#sprawdzanie, czy punkt na planszy ma sąsiada w orientacji pion-poziom równego t
	y = 0		
	if index1 == 0 or index1 == 9:
		if index2 == 0:
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
		elif index2 == 9:
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
		else: # 0 < index2 < 9
			if index1 == 0:
				if x[index1+1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] == t:
					y = 1
				if x[index1][index2+1] == t:
					y = 1
				if x[index1][index2-1] == t:
					y = 1
	elif (index1 != 0 and index1 != 9 and (index2 == 0 or index2 == 9)):
		if index2 == 0:
			if x[index1+1][index2] == t:
				y = 1
			if x[index1-1][index2] == t:
				y = 1
			if x[index1][index2+1] == t:
				y = 1
		else: #index2 == 9
			if x[index1+1][index2] == t:
				y = 1
			if x[index1-1][index2] == t:
				y = 1
			if x[index1][index2-1] == t:
				y = 1
	else:		
		if x[index1+1][index2] == t:
			y = 1
		if x[index1-1][index2] == t:
			y = 1
		if x[index1][index2-1] == t:
			y = 1
		if x[index1][index2+1] == t:
			y = 1
	return y

def all_neighbours_wh(x,index1,index2,t):					#sprawdzanie, czy punkt na planszy ma wszystkich sąsiadów mniejszych od t w orientacji pion-poziom
	y = 0		
	if index1 == 0 or index1 == 9:
		if index2 == 0:
			if index1 == 0:
				if x[index1+1][index2] < t and x[index1][index2+1] < t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] < t and x[index1][index2+1] < t:
					y = 1
		elif index2 == 9:
			if index1 == 0:
				if x[index1+1][index2] < t and x[index1][index2-1] < t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] < t and x[index1][index2-1] < t:
					y = 1
		else: # 0 < index2 < 9
			if index1 == 0:
				if x[index1+1][index2] < t and x[index1][index2-1] < t and x[index1][index2+1] < t:
					y = 1
			else: #index1 == 9
				if x[index1-1][index2] < t and x[index1][index2+1] < t and x[index1][index2-1] < t:
					y = 1
	elif (index1 != 0 and index1 != 9 and (index2 == 0 or index2 == 9)):
		if index2 == 0:
			if x[index1+1][index2] < t and x[index1][index2+1] < t and x[index1-1][index2] < t:
				y = 1
		else: #index2 == 9
			if x[index1+1][index2] < t and x[index1][index2-1] < t and x[index1-1][index2] < t:
				y = 1
	else:		
		if x[index1+1][index2] < t and x[index1-1][index2] < t and x[index1][index2-1] < t and x[index1][index2+1] < t:
			y = 1
	return y

def give_2(ar):								#otaczanie statków polami o wartości 2
	for i in range (0,10):
		for j in range (0,10):
			if ar[i][j] == 0 and neighbour(ar,i,j,1) == 1:
				ar[i][j] = 2

def set_4ship(ar,index1,index2):				#ustawianie statków stąd...
	x = random_direction(index1,index2,3)		
	for i in range (1,4):
		if x == 0:
			ar[index1-i][index2] = 1
		elif x == 1:
			ar[index1][index2+i] = 1
		elif x == 2:
			ar[index1+i][index2] = 1
		elif x == 3:
			ar[index1][index2-i] = 1

def set_3ship(ar,index1,index2,x):		
	if x == 0 and ar[index1-2][index2] == 0:
		for i in range (1,3):
			ar[index1-i][index2] = 1	
		return 1
	elif x == 1 and ar[index1][index2+2] == 0:
		for i in range (1,3):
			ar[index1][index2+i] = 1
		return 1
	elif x == 2 and ar[index1+2][index2] == 0:
		for i in range (1,3):
			ar[index1+i][index2] = 1
		return 1
	elif x == 3 and ar[index1][index2-2] == 0:
		for i in range (1,3):
			ar[index1][index2-i] = 1
		return 1
	return 0

def set_2ship(ar,index1,index2,x):
	if x == 0 and ar[index1-1][index2] == 0:
		for i in range (1,2):
			ar[index1-i][index2] = 1	
		return 1
	elif x == 1 and ar[index1][index2+1] == 0:
		for i in range (1,2):
			ar[index1][index2+i] = 1
		return 1
	elif x == 2 and ar[index1+1][index2] == 0:
		for i in range (1,2):
			ar[index1+i][index2] = 1
		return 1
	elif x == 3 and ar[index1][index2-1] == 0:
		for i in range (1,2):
			ar[index1][index2-i] = 1	
		return 1
	return 0												       #...aż dotąd

def random_position(a,b):				#losowanie pozycji
	x = random.randint(a,b)
	y = random.randint(a,b)
	return x,y

def random_direction(index1,index2,a):						# 0-N 1-E 2-S 3-W
	x = random.randint(0,3)
	if index1 < a or index1 > 9-a:
		if index2 < a:
			if index1 < a:
				while x == 3 or x == 0:
					x = random.randint(0,3)
			elif index1 > 9-a:
				while x == 2 or x == 3:
					x = random.randint(0,3)
		elif index2 > 9-a:
			if index1 < a:
				while x == 0 or x == 1:
					x = random.randint(0,3)
			elif index1 > 9-a:
				while x == 2 or x == 1:
					x = random.randint(0,3)
		else: # a <= index2 <= 9-a
			if index1 < a:
				while x == 0:
					x = random.randint(0,3)
			elif index1 > 9-a:
				while x == 2:
					x = random.randint(0,3)
	elif (index1 >= a and index1 <= 9-a and (index2 < a or index2 > 9-a)):
		if index2 < a:
			while x == 3:
				x = random.randint(0,3)
		elif index2 > 9-a:
			while x == 1:
				x = random.randint(0,3)
	return x

def random_shoot(index1,index2):						# 0-N 1-E 2-S 3-W
	x = random.randint(0,3)
	if index1 == 0 or index1 == 9:
		if index2 == 0:
			if index1 == 0:
				while x == 3 or x == 0:
					x = random.randint(0,3)
			elif index1 == 9:
				while x == 2 or x == 3:
					x = random.randint(0,3)
		elif index2 == 9:
			if index1 == 0:
				while x == 0 or x == 1:
					x = random.randint(0,3)
			elif index1 == 9:
				while x == 2 or x == 1:
					x = random.randint(0,3)
		else: # 0 < index2 < 9
			if index1 == 0:
				while x == 0:
					x = random.randint(0,3)
			elif index1 == 9:
				while x == 2:
					x = random.randint(0,3)
	elif (index1 > 0 and index1 < 9 and (index2 == 0 or index2 == 9)):
		if index2 == 0:
			while x == 3:
				x = random.randint(0,3)
		elif index2 == 9:
			while x == 1:
				x = random.randint(0,3)
	return x

def hit_by_player(ar,index1,index2):					#uderzenie gracza
	if ar[index1][index2] == 1:
		ar[index1][index2] = -1
	elif ar[index1][index2] == 0 or ar[index1][index2] == 2:
		ar[index1][index2] = -2

def hit_by_AI_easy(ar):					#losowe uderzenia
	x,y = random_position(0,9)
	while (ar[x][y] != 0 and ar[x][y] != 1 and ar[x][y] != 2):
		x,y = random_position(0,9)
	sleep(0.7)
	if ar[x][y] == 0 or ar[x][y] == 2:
		ar[x][y] = -2
	elif ar[x][y] == 1:
		ar[x][y] = -1	
		
def hit_by_AI_normal(ar):						#nie atakuje pól, na których jest 0
	x,y = random_position(0,9)
	while (ar[x][y] != 2 and ar[x][y] != 1):
		x,y = random_position(0,9)
	sleep(0.7)
	if ar[x][y] == 2:
		ar[x][y] = -2
	elif ar[x][y] == 1:
		ar[x][y] = -1

def hit_by_AI_hard(ar):			#atakuje tylko 1
	x,y = random_position(0,9)
	while (ar[x][y] != 1):
		x,y = random_position(0,9)
	sleep(0.7)
	ar[x][y] = -1
