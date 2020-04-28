
import pygame,sys
import keyboard
from pygame.locals import *
import os
import random
import time
from pygame import *
pygame.init()
disp_h=600
disp_w=600
scr_size = (width,height) = (disp_h,disp_w)
FPS = 13


black = (0,0,0)
white = (255,255,255)
background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("snake game")





#global snake variables
ar_size=30
food_x=random.randint(0,ar_size-1)
food_y=random.randint(0,ar_size-1)
initial_snake_len=3




g_matrix=[]
for i in range(ar_size):
	g_matrix.append([])

for i in range(ar_size):
	for j in range(ar_size):
		g_matrix[i].append(0)

#position of the food:
g_matrix[food_x][food_y]=-1

		
def randomfood(self):
	food_x=random.randint(0,ar_size-1)
	food_y=random.randint(0,ar_size-1)
	g_matrix[food_x][food_y]=-1


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

class snake():
	def __init__(self):
		self.head=(10,7)
		self.header_x=0
		self.header_y=0
		self.tail=(10,10)
		self.speed=1
		self.length=3
		self.snake_arr=[]
		
		self.tracker=[]
		self.directions=1
		
		for i in range(initial_snake_len):
			self.snake_arr.append((self.head[0],self.head[1]+i))

	
	def init_snake(self):
		
		
		
		for i in range(len(self.snake_arr)):
			 g_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(i+1)



		
		# return self.play_matrix
	
	def updator(self):
		for i in range(len(self.snake_arr)):
			 g_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(i+1)

		# making the snake move by removing end of snake
		g_matrix[self.tail[1]][self.tail[0]]=0

	def searcher(self,num):
		self.updator()
		for y in range(ar_size-1):
			for x in range(ar_size-1):
				if (g_matrix[x][y]==num):
					break
			if (g_matrix[x][y]==num):
				break
		
		return (x,y)


	

	# def snake_director(self):
	# 	# initialising the snake
	# 	self.init_snake()
	# 	first=self.searcher(1)
	# 	second=self.searcher(2)

	# 	# UP
	# 	if(first[0]==second[0]):
	# 		if(first[1]>second[1]):
	# 			return 4
	# 	# DOWN
	# 	if(first[0]==second[0]):
	# 		if(first[1]<second[1]):
	# 			return 6

	# 	# LEFT
	# 	if(first[1]==second[1]):
	# 		if(first[0]<second[0]):
	# 			return 8
		
	# 	# RIGHT
	# 	if(first[1]==second[1]):
	# 		if(first[0]>second[0]):
	# 			return 2
	
		

	def mover(self):
		global food_x
		global food_y
		direction=self.directions
		#debugging purpose
		try:
			a=self.snake_arr[0]
		except:
			self.snake_arr.append((0,0))

		firsty=self.snake_arr[0]
		temp_a=firsty[0]
		temp_b=firsty[1]
		firsty=(temp_b,temp_a)

		# controls........................................................................
		


		self.header_x=self.snake_arr[0][0]
		self.header_y=self.snake_arr[0][1]

		for i in range(1,len(self.snake_arr)):
			
				if self.header_x==self.snake_arr[i][0]:
					if self.header_y==self.snake_arr[i][1]:
						pass

		if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
		
		
		
		if direction==8:
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				pass
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==2:
			self.snake_arr.reverse()
			if firsty[0]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				pass
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==4:
			self.snake_arr.reverse()
			if firsty[1]!=(0):

				
				self.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				pass
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==6:
			self.snake_arr.reverse()
			if firsty[1]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				pass
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
			
			
			self.updator()








		
			

		


	
	

		






def main():
	pop=100

	s=[]
	for i in range(pop):
		s.append(snake())


	while True:
		
		
		for i in range(pop):
			s[i].directions=random.choice([8,4,6,2])



		clock.tick(FPS)
		# pygame.time.delay(100)
		os.system("cls")
		

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		
		for i in range(pop):
			s[i].mover()
		
		
		
		pygame.display.update()
		screen.fill(white)
		
		for x in range(len(g_matrix)):
			for y in range(len(g_matrix)):
				if(g_matrix[x][y]!=0 and g_matrix[x][y]!=( -1) and g_matrix[x][y]!=1):
					pygame.draw.rect(screen,(0,255,0),(y*20,x*20,10,10))
				if(g_matrix[x][y]==1):
					pygame.draw.rect(screen,(0,0,255),(y*20,x*20,10,10))

					
		pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))


		
		
		print("\n\n")
		for i in range(len(g_matrix)):
			print(g_matrix[i])
		






main()



