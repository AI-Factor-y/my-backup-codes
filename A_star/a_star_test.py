import pygame
import time
import os

pygame.init()


white=(255,255,255)
black=(0,0,0)
draw_arr=[]

clock = pygame.time.Clock()


	

	
if __name__=="__main__":
	start=0
	wall=[]
	end=0
	flag=0
	l_exit=False
	gameDisplay = pygame.display.set_mode((600,600))
	while True:
		if pygame.mouse.get_pressed()==(1,0,0):
			pos=pygame.mouse.get_pos()
			pygame.draw.circle(gameDisplay,white,pos,4)
			wall.append((pos[0]//6,pos[1]//6))
		if pygame.mouse.get_pressed()==(0,0,1):
			pos=pygame.mouse.get_pos()
			if flag==0:
				start=pos
			else:
				end=pos
			pygame.draw.circle(gameDisplay,(255,0,0),pos,6)
			flag=1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				l_exit=True
				break
		if l_exit:
			break

		pygame.display.update()

	print(start)
	print(end)
