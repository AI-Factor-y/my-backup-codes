
import pygame
import random
import time
pygame.init()

width=500
height=500

width_s=50

gameDisplay=pygame.display.set_mode((width,height))

class line:

	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.wx=width_s
		self.wy=width_s
		self.color=(255,255,255)
		self.thick=2

	def drawX(self):


		pygame.draw.line(gameDisplay,self.color,(self.x,self.y),(self.x+self.wx,self.y),self.thick)

	def drawY(self):

		pygame.draw.line(gameDisplay,self.color,(self.x,self.y),(self.x,self.y+self.wy),self.thick)


def create_linesX(x1,y1,x2,y2):
	lines=[]
	print(x2,x1)
	limit=int((x2-x1)//width_s)

	for i in range(limit):
		lines.append(line(x1,y1))
		x1+=width_s


	return lines

def create_linesY(x1,y1,x2,y2):
	lines=[]
	
	limit=int((y2-y1)//width_s)
	for i in range(limit):
		lines.append(line(x1,y1))
		y1+=width_s


	return lines

def draw_maze():
	

	x1_hori=0
	y1_hori=height//2
	x2_hori=width 
	y2_hori=height//2

	x1_vert=width//2
	y1_vert=0
	x2_vert=width//2 
	y2_vert=height

	drawn_lines_x=[]
	drawn_lines_y=[]
	while True:

		gameDisplay.fill(51)

		linesX=create_linesX(x1_hori,y1_hori,x2_hori,y2_hori)
		if len(linesX)==0:

			break
		for i in range(random.randint(1,3)):
			if len(linesX)==0:
				break
			linesX.pop(random.randint(0,len(linesX)-1))
		for line_ in linesX:
			drawn_lines_x.append(line_)
			line_.drawX()

		for line_ in drawn_lines_x:
			
			line_.drawX()

		linesY=create_linesY(x1_vert,y1_vert,x2_vert,y2_vert)

		if len(linesY)==0:
			break

		for i in range(random.randint(1,3)):
			if len(linesY)==0:
				break
			linesY.pop(random.randint(0,len(linesY)-1))
		for line_ in linesY:
			drawn_lines_y.append(line_)

		for line_ in drawn_lines_y:
			
			line_.drawY()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()

		y1_hori=int(y1_hori/2)
		y2_hori=int(y2_hori/2)
		x2_hori=int(x2_hori/2)
		x1_hori=0

		x1_vert=int(x1_vert/2)
		x2_vert=int(x2_hori/2)
		y2_vert=int(y2_vert/2)
		y1_vert=0



		pygame.display.update()
		time.sleep(0.5)



draw_maze()
time.sleep(20)


run=False
while run:

	gameDisplay.fill(51)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	

	pygame.display.update()



# def create_maze():
# 	gap_x=width//width_s
# 	gap_y=height//width_s
# 	x1=x2=random.randint(0,gap_x)*width_s
# 	y1=0
# 	y2=height
# 	current_line=line(x1,y1,x2,y2)
# 	# randon_gap_y=random.randint(0,gap_y)*width_s

# 	for _ in range(random.randint(0,3)):

# 		y=random.randint(0,gap_y)*height
# 		current_line.draw(x1,y)




