import pygame
from random import *
from constant_values import *
from functions import *

class button:
	def __init__(self,x_start,y_start,x_frame,y_frame,width,height,colour_1,colour_2,colour_3,text,f_size,action):
		self.x_start = x_start
		self.y_start = y_start
		self.x_frame = x_frame
		self.y_frame = y_frame
		self.width = width
		self.height = height
		self.colour_1 = colour_1
		self.colour_2 = colour_2
		self.colour_3 = colour_3
		self.text = text
		self.f_size = f_size
		self.action = action

		pygame.draw.rect(SCREEN,self.colour_2,(self.x_start-self.x_frame,self.y_start-self.y_frame,self.width+2*self.x_frame,self.height+2*self.y_frame))
		pygame.draw.rect(SCREEN,self.colour_1,(self.x_start,self.y_start,self.width,self.height))
		
		mouse_position = pygame.mouse.get_pos()
		mouse_pressed = pygame.mouse.get_pressed()

		if (mouse_position[0] >= self.x_start and mouse_position[0] <= self.x_start + self.width) and (mouse_position[1] >= self.y_start and mouse_position[1] <= self.y_start + self.height):
			pygame.draw.rect(SCREEN,self.colour_3,(self.x_start,self.y_start,self.width,self.height))
			if mouse_pressed[0] == 1 and self.action != "None":
				self.action()

		TEXT = pygame.font.SysFont("sarai", self.f_size)
		texting(self.text,TEXT,self.x_start+0.5*self.width,self.y_start+0.5*self.height,self.colour_2)

class s_button:
	def __init__(self,x_start,y_start,x_frame,y_frame,width,height,colour_1,colour_2,colour_3,number,choose):
		self.x_start = x_start
		self.y_start = y_start
		self.x_frame = x_frame
		self.y_frame = y_frame
		self.width = width
		self.height = height
		self.colour_1 = colour_1
		self.colour_2 = colour_2
		self.colour_3 = colour_3
		self.number = number
		self.choose = choose

		pygame.draw.rect(SCREEN,self.colour_2,(self.x_start-self.x_frame,self.y_start-self.y_frame,self.width+2*self.y_frame,self.height+2*self.y_frame))
		pygame.draw.rect(SCREEN,self.colour_1,(self.x_start,self.y_start,self.width,self.height))

		mouse_position = pygame.mouse.get_pos()
		mouse_pressed = pygame.mouse.get_pressed()

		if (mouse_position[0] >= self.x_start and mouse_position[0] <= self.x_start + self.width) and (mouse_position[1] >= self.y_start and mouse_position[1] <= self.y_start + self.height):
			if mouse_pressed[0] == 1:
				for i in range(len(self.choose)):
					self.choose[i] = 0
				self.choose[self.number] = 1

		if self.choose[self.number] == 1:
			pygame.draw.rect(SCREEN,self.colour_3,(self.x_start,self.y_start,self.width,self.height))

class cube:
	def __init__(self,start,image,dirnx=1,dirny=0):
		self.pos = start
		self.image = image
		self.dirnx = 1
		self.dirny = 0
        
	def move(self, dirnx, dirny):
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos = ((self.pos[0] + self.dirnx) % BOARD_WIDTH, (self.pos[1] + self.dirny) % BOARD_HEIGHT)

	def draw(self):
		i = self.pos[0]
		j = self.pos[1]
		SCREEN.blit(self.image, (X_14+i*FIELD_SIDE,Y_14+j*FIELD_SIDE))

class snake:
	def __init__(self,pos,image):
		self.body = []
		self.turns = {}
		self.image = image
		self.head = cube(pos,self.image)
		self.body.append(self.head)
		self.dirnx = 1
		self.dirny = 0

	def reset(self):
		self.body = []
		self.turns = {}
		self.dirnx = 1
		self.dirny = 0

	def move(self):
		keys = pygame.key.get_pressed()

		for key in keys:
			if self.dirnx == 0:
				if keys[pygame.K_a]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_d]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
			elif self.dirny == 0:
				if keys[pygame.K_w]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
				elif keys[pygame.K_s]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

		for i, c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0],turn[1])
				if i == len(self.body)-1:
					self.turns.pop(p)
			else:
				c.move(c.dirnx,c.dirny)

	def crashCheck(self):
		for x in range(len(self.body)):
			for i in self.body[x+1:]:
				if self.body[x].pos == i.pos:
					return True
		return False

	def addCube(self):
		tail = self.body[-1]
		dx, dy = tail.dirnx, tail.dirny

		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1]),self.image))
		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0]+1,tail.pos[1]),self.image))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]-1),self.image))
		elif dx == 0 and dy == -1:
			self.body.append(cube((tail.pos[0],tail.pos[1]+1),self.image))

		self.body[-1].dirnx = dx
		self.body[-1].dirny = dy

	def draw(self):
		for c in (self.body):
			c.draw()
