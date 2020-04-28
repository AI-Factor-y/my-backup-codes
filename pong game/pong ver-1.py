import pygame
import time
import os
import random
pygame.init()

STAT_FONT = pygame.font.SysFont("comicsans",30)

gameDisplay = pygame.display.set_mode((600,700))

clock = pygame.time.Clock()


gameExit=False
Player_Vel = 10

choic=[-2,2]



class Player:

	global Player_Vel

	def __init__(self,x):
		
		self.x = x
		self.vel = Player_Vel
		self.r=255
		self.b=255
		self.g=255
		self.ball_x=random.randint(15,580)
		self.ball_y=random.randint(15,300)
		self.ball_vel_y=random.choice(choic)
		self.ball_vel_x=random.choice(choic)
	def move_ball(self):
		

		self.ball_x+=self.ball_vel_x
		self.ball_y+=self.ball_vel_y
		pygame.draw.circle(gameDisplay,(255,0,0),(self.ball_x,self.ball_y),10)
	def player_disp(self):
		pygame.draw.rect(gameDisplay,(self.r,self.b,self.g),(self.x-45,685,90,10))

	def move(self,direction):


		if direction == 1:

			self.x += Player_Vel

		elif direction == -1:

			self.x -= Player_Vel



	def wall(self):
		

		gameover=False

		
		if self.ball_x==590 or self.ball_x==10:
			self.ball_vel_x*=-1
		if self.ball_y<=10:
			self.ball_vel_y*=-1
		if self.ball_y>=665 :
			if self.ball_x >= (self.x-50) and self.ball_x <= (self.x+50):
				self.ball_vel_y *= -1

		if self.ball_y > 700:
			gameover=True
		return gameover

		
	




def main():
	global gameExit,ball_x,ball_y,gen
	p=Player(50)
	dir_p=0
	

	p.move_ball()

	while not gameExit:
		keys = pygame.key.get_pressed()
		gameDisplay.fill((0,0,0))
		
		p.player_disp()

		
		clock.tick(60)
		
		if  keys[pygame.K_RIGHT]:
			
			dir_p=1

		elif keys[pygame.K_LEFT]:
			
			dir_p=-1
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			pygame.key.set_repeat(0)
		else:
			if event.type == pygame.KEYUP:
				dir_p = 0
		
		

		

				
		
		
		
			p.move(dir_p)
			p.wall()

			p.move_ball()

		pygame.display.update()

main()
