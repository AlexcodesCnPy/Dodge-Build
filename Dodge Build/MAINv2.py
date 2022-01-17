import pygame
import math
import random

#-music
#title
#diffuculty
#game over screen


pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Dodge Build')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf',32)

class player:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.img = pygame.image.load('player.png')
		self.speed = 0

	def change(self,n,direction):
		self.x += n*direction
		if self.x >= 736:
			self.x = 736
		if self.x <= 0:
			self.x = 0

class block:
	SPEED_c = 0.98
	def __init__(self,x,y,next=None):
		self.x = x
		self.y = y
		self.img = pygame.image.load('boulders.png')
		self.speed = 0

	def fall(self,x,y):
		self.y += block.SPEED_c

	def add(self):
		self.next = block(random.randint(player1.x-150,player1.y+150), 0)

	def length(self):
		temp = self
		count = 0
		while (temp != None):
			count += 1

		return count

def B(img,x,y):
	screen.blit(img,(x,y))

def P(img,x,y):
	screen.blit(img,(x,y))

def collide(x1,x2,y1,y2):
	distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
	if distance <= 60: return True 
	else: return False

def showscore(i):
	score = font.render('Score:'+str(i),True,(255,0,0))
	screen.blit(score,(10,10))

def title():
	screen = pygame.display.set_mode(800,600)
	running = True
	while running:
		passd

def play():
	score = 0
	player1 = player(400,535)
	blocks = block(random.randint(player1.x-150,player1.x+150), 0)
	running = True
	n = 0.70
	d = 0
	while running:
		screen.fill((235,234,243))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_a,pygame.K_LEFT):
					d = -1			

				if event.key in (pygame.K_d,pygame.K_RIGHT):
					d = 1

			if event.type == pygame.KEYUP:
				d = 0 * d

				if event.type == pygame.KEYDOWN:
					if event.key in (pygame.K_a,pygame.K_LEFT):
						d = -1			

					if event.key in (pygame.K_d,pygame.K_RIGHT):
						d = 1

		blocks.fall(player1.x,player1.y)
		if blocks.y > 600:
			blocks = block(random.randint(int(player1.x-100),int(player1.x+100)), 0)
			score += 1
			block.SPEED_c += .2
		temp = blocks
		if collide(player1.x,temp.x,player1.y,temp.y):
			print('COLLISION')
			running = False
		


		player1.change(n,d)
		B(blocks.img,blocks.x,blocks.y)
		P(player1.img,player1.x,player1.y)
		showscore(score)
		pygame.display.update()




if __name__ == '__main__':
	play()
			
