import pygame
import random
import math
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Im dodging Teh build')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf',32)
score_value = 0
textY1 = 455
textX1  = 455
scoreY = 10
scoreX = 10

w = False

#GAME Objects
def collision(x1,y1,x2,y2):
	distance = math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
	if distance < 60:
		return True
	else:
		return False

def showscore(x,y):
	global score_value 
	score = font.render('Score:'+str(score_value),True,(255,0,0))
	screen.blit(score,(x,y))

def play():
	pointer = 1


	global numb
	global score_value
	#Game Objects
	playerImg = pygame.image.load('player.png')
	playerX = 400
	playerY = 535
	playerSpeed = 0


	blockImg = pygame.image.load('boulders.png')
	blockX = random.randint(playerX-60,playerX+60)
	blockY = 10	
	blockSpeed= 9.8/10

	print(blockY)		
	def player(x,y):
		screen.blit(playerImg,(x,y))

	def blocks(x,y):
		screen.blit(blockImg,(x,y))

	'''def updateblocks():
		for i in range(numB):
			blockImg.append(pygame.image.load('boulders.png'))
			blockX.append(random.randint(0,728))
			blockY.append(10)'''

	running = True
	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("PLAYER QUIT")
				running = False
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_a,pygame.K_LEFT) :
					playerSpeed = .5 * (-1)

				if event.key in (pygame.K_d,pygame.K_RIGHT):
					playerSpeed = .5 * 1

			if event.type == pygame.KEYUP:
					playerSpeed *= 0


		playerX += playerSpeed
		if playerX > 736:
			playerX = 736
		if playerX < 0:
			playerX = 0

		screen.fill((235,234,243))
		
		blockY += blockSpeed
		if blockY > 600:
			blockY = -1
			blockX = random.randint(0,728)
			blockSpeed += 0.02
			score_value += 1
		if collision(playerX,playerY,blockX,blockY):
			global w
			w = True
			running = False
			print('COLLISION')
	
		blocks(blockX,blockY,)

		player(playerX,playerY)
		
		showscore(scoreX,scoreY)
		pygame.display.update()


if __name__ == '__main__':
	play()

####### end syntax ###########

