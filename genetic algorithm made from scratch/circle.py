import pygame
import math
pygame.init()

width=700
height=600
gamedisplay=pygame.display.set_mode((width,height))

radius=100
theta=0
run=True
clock=pygame.time.Clock()
path=[]
path2=[]
while run:
	gamedisplay.fill(0)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
	
			run=False
	theta+=0.02
	x=width/2 + radius*math.cos(theta)-100
	y=height/2 + radius*math.sin(theta)
	x,y=int(x),int(y)
	pygame.draw.circle(gamedisplay,(255,255,255),(x,y),10)
	path.append((x,y))

	for p in path:
		pygame.draw.circle(gamedisplay,(255,255,255),p,1)
	if len(path)>1000:
		path.pop()

	x1=width/2 + radius*math.cos(-theta+math.pi)
	y1=height/2 + radius*math.sin(-theta+math.pi)
	x1,y1=int(x1),int(y1)
	pygame.draw.circle(gamedisplay,(255,255,255),(x1,y1),10)
	path2.append((x1,y1))

	for p in path2:
		pygame.draw.circle(gamedisplay,(255,255,255),p,1)
	if len(path)>1000:
		path.pop()
	pygame.display.update()