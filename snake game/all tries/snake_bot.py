
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
food_x=random.randint(6,ar_size-6)
food_y=random.randint(6,ar_size-6)
initial_snake_len=3


def g_matrix():

		mat=[]
		for i in range(ar_size):
			mat.append([])

		for i in range(ar_size):
			for j in range(ar_size):
				mat[i].append(0)

		#position of the food:
		mat[food_x][food_y]=-1

		return mat
def randomfood(self):
	food_x=random.randint(6,ar_size-6)
	food_y=random.randint(6,ar_size-6)
	self.play_matrix[food_x][food_y]=-1


def translate(value, leftMin, leftMax, rightMin, rightMax):
   
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

   
    valueScaled = float(value - leftMin) / float(leftSpan)

  
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
		self.play_matrix=[]
		self.tracker=[]
		self.directions=1
		self.ini_up=False
		self.ini_down=False
		self.ini_right=False
		self.ini_left=False
		self.gotfood=True
		self.play_matrix=g_matrix()
		for i in range(initial_snake_len):
			self.snake_arr.append((self.head[0],self.head[1]+i))

	
	def init_snake(self):
		
		
		
		for i in range(len(self.snake_arr)):
			 self.play_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(i+1)



		
		# return self.play_matrix
	
	def updator(self):
		for i in range(len(self.snake_arr)):
			 self.play_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(i+1)

		# making the snake move by removing end of snake
		self.play_matrix[self.tail[1]][self.tail[0]]=0

	def searcher(self,num):
		self.updator()
		for y in range(ar_size-1):
			for x in range(ar_size-1):
				if (self.play_matrix[x][y]==num):
					break
			if (self.play_matrix[x][y]==num):
				break
		print(y,x)
		
		return (x,y)


	

	def snake_director(self):
		# initialising the snake function returns the direction same  to snake direction
		self.init_snake()
		first=self.snake_arr[0]
		second=self.snake_arr[1]

		# UP
		if(first[0]==second[0]):
			if(first[1]>second[1]):
				return 2
		# DOWN
		if(first[0]==second[0]):
			if(first[1]<second[1]):
				return 8

		# LEFT
		if(first[1]==second[1]):
			if(first[0]<second[0]):
				return 4
		
		# RIGHT
		if(first[1]==second[1]):
			if(first[0]>second[0]):
				return 6
	
		

	def mover(self):
		obstacle_left=False
		obstacle_up=False
		obstacle_right=False
		obstacle_down=False
		obstacle=False

		escape=False
		global food_x
		global food_y
		d=self.snake_director()
		headx=self.snake_arr[0][0]
		heady=self.snake_arr[0][1]
		foodx=food_y
		foody=food_x
		#case when the snake is at the real back of the food or in line with the food

		if foodx==headx and foody>heady and d==8 and self.gotfood==True:
			self.directions=6
			escape=True
		if foodx==headx and foody<heady and d==2 and self.gotfood==True:
			self.directions=4
			escape=True
		if foody==heady and foodx>headx and d==4 and self.gotfood==True:
			self.directions=8
			escape=True
		if foody==heady and foodx<headx and d==6 and self.gotfood==True:
			self.directions=2
			escape=True

		
		# try:
			# if d==6 or d==4:
			# 	for i in range(heady-5,heady):
			# 		if self.play_matrix[headx][i]>1:
			# 			obstacle_up=True
			# 	for j in range(heady+1,heady+5):
			# 		if self.play_matrix[headx][j]>1:
			# 			obstacle_down=True
			# if d==2 or d==8:
			# 	for i in range(headx-5,headx):
			# 		if self.play_matrix[i][heady]>1:
			# 			obstacle_right=True
			# 	for j in range(headx+1,headx+5):
			# 		if self.play_matrix[j][heady]>1:
			# 			obstacle_left=True
		# 	if d==8:
		# 		if self.play_matrix[headx][heady-1]>1:
		# 			self.directions=4
		# 			obstacle=True
		# 	if d==2:
		# 		if self.play_matrix[headx][heady+1]>1:
		# 			self.directions=6
		# 			obstacle=True
		# 	if d==4:
		# 		if self.play_matrix[headx-1][heady]>1:
		# 			self.directions=2
		# 			obstacle=True
		# 	if d==6:
		# 		if self.play_matrix[headx+1][heady]>1:
		# 			self.directions=8
		# 			obstacle=True
		# except:
		# 	passif d==8:
		# 		if self.play_matrix[headx][heady-1]>1:
		# 			self.directions=4
		# 			obstacle=True
		# 	if d==2:
		# 		if self.play_matrix[headx][heady+1]>1:
		# 			self.directions=6
		# 			obstacle=True
		# 	if d==4:
		# 		if self.play_matrix[headx-1][heady]>1:
		# 			self.directions=2
		# 			obstacle=True
		# 	if d==6:
		# 		if self.play_matrix[headx+1][heady]>1:
		# 			self.directions=8
		# 			obstacle=True

		# print(obstacle)



		# print("obstacle_up : ",obstacle_up)
		# print("obstacle_down :",obstacle_down)
		# print("obstacle_left",obstacle_left)
		# print("obstacle_right",obstacle_right)
		try:
			if d==8:
				if self.play_matrix[headx][heady-1]>1:
					self.directions=4
					obstacle=True
			if d==2:
				if self.play_matrix[headx][heady+1]>1:
					self.directions=6
					obstacle=True
			if d==4:
				if self.play_matrix[headx-1][heady]>1:
					self.directions=2
					obstacle=True
			if d==6:
				if self.play_matrix[headx+1][heady]>1:
					self.directions=8
					obstacle=True
		except:
			pass

		if escape==False and obstacle== False:
			if d==8 and self.gotfood==True:
				self.ini_up=True
			if d==2 and self.gotfood==True:
				self.ini_down=True
			if d==6 and self.gotfood==True:
				self.ini_right=True
			if d==4 and self.gotfood==True:
				self.ini_left=True

			self.gotfood=False


			#ai part
			if self.ini_up:
				if headx<foodx and obstacle_right==False and d!=4:
					self.directions=6
				if headx>foodx and obstacle_left==False and d!=6:
					self.directions=4
				if headx==foodx:
					if heady>foody and obstacle_up==False and d!=2:
						self.directions=8
					if heady<foody and obstacle_down==False and d!=8:
						self.directions=2
					if heady==foody:
						self.ini_up=False
						self.gotfood=True
			if self.ini_down:
				if headx<foodx and obstacle_right==False and d!=4:
					self.directions=6
				if headx>foodx and obstacle_left==False and d!=6:
					self.directions=4
				if headx==foodx:
					if heady>foody and obstacle_up==False and d!=2:
						self.directions=8
					if heady<foody and obstacle_down==False and d!=8:
						self.directions=2
					if heady==foody:
						self.ini_down=False
						self.gotfood=True
			if self.ini_right:
				if heady>foody and obstacle_up==False and d!=2:
					self.directions=8
				if heady<foody and obstacle_down==False and d!=8:
					self.directions=2
				if heady==foody:
					if headx<foodx and obstacle_right==False and d!=4:
						self.directions=6
					if headx>foodx and obstacle_left==False and d!=6:
						self.directions=4
					if headx==foodx:
						self.ini_right=False
						self.gotfood=True
			if self.ini_left:
				if heady>foody and obstacle_up==False and d!=2:
					self.directions=8
				if heady<foody and obstacle_down==False and d!=8:
					self.directions=2
				if heady==foody:
					if headx<foodx and obstacle_right==False and d!=4:
						self.directions=6
					if headx>foodx and obstacle_left==False and d!=6:
						self.directions=4
					if headx==foodx:
						self.ini_left=False
						self.gotfood=True

			# if self.ini_up:
			# 	if headx<foodx and d!=4:
			# 		self.directions=6
			# 	if headx>foodx and d!=6:
			# 		self.directions=4
			# 	if headx==foodx:
			# 		if heady>foody and d!=2:
			# 			self.directions=8
			# 		if heady<foody and d!=8:
			# 			self.directions=2
			# 		if heady==foody:
			# 			self.ini_up=False
			# 			self.gotfood=True
			# if self.ini_down:
			# 	if headx<foodx and d!=4:
			# 		self.directions=6
			# 	if headx>foodx and d!=6:
			# 		self.directions=4
			# 	if headx==foodx:
			# 		if heady>foody and d!=2:
			# 			self.directions=8
			# 		if heady<foody and d!=8:
			# 			self.directions=2
			# 		if heady==foody:
			# 			self.ini_down=False
			# 			self.gotfood=True
			# if self.ini_right:
			# 	if heady>foody and d!=2:
			# 		self.directions=8
			# 	if heady<foody and d!=8:
			# 		self.directions=2
			# 	if heady==foody:
			# 		if headx<foodx and d!=4:
			# 			self.directions=6
			# 		if headx>foodx and d!=6:
			# 			self.directions=4
			# 		if headx==foodx:
			# 			self.ini_right=False
			# 			self.gotfood=True
			# if self.ini_left:
			# 	if heady>foody and d!=2:
			# 		self.directions=8
			# 	if heady<foody and d!=8:
			# 		self.directions=2
			# 	if heady==foody:
			# 		if headx<foodx and d!=4:
			# 			self.directions=6
			# 		if headx>foodx and d!=6:
			# 			self.directions=4
			# 		if headx==foodx:
			# 			self.ini_left=False
			# 			self.gotfood=True








		
		
		direction=self.directions

		
		
		firsty=self.snake_arr[0]
		temp_a=firsty[0]
		temp_b=firsty[1]
		firsty=(temp_b,temp_a)

		# controls........................................................................
		pygame.display.update()
		screen.fill(white)
		try:
			snake_direction=self.snake_director()
		except:
			snake_direction=0
		
		self.header_x=self.snake_arr[0][0]
		self.header_y=self.snake_arr[0][1]
		flag=0
		for i in range(1,len(self.snake_arr)):
			
				if self.header_x==self.snake_arr[i][0]:
					if self.header_y==self.snake_arr[i][1]:
						# exit()
						flag=1
						break
				if flag==1:
					break
						

		if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(6,ar_size-6)
				food_y=random.randint(6,ar_size-6)
				self.play_matrix[food_x][food_y]=-1
		
		pygame.draw.rect(screen,(0,0,255),(self.snake_arr[0][0]*20,self.snake_arr[0][1]*20,10,10))
		for i in range(1,len(self.snake_arr)):
			pygame.draw.rect(screen,(0,255,0),(self.snake_arr[i][0]*20,self.snake_arr[i][1]*20,10,10))

		pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))
		
		
		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		
		
		if direction==8 :
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.snake_arr.append((firsty[1],ar_size-1))
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(6,ar_size-6)
				food_y=random.randint(6,ar_size-6)
				self.play_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==2:
			self.snake_arr.reverse()
			if firsty[0]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.snake_arr.append((firsty[1],0))   
				
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(6,ar_size-6)
				food_y=random.randint(6,ar_size-6)
				self.play_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==4:
			self.snake_arr.reverse()
			if firsty[1]!=(0):

				
				self.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.snake_arr.append((ar_size-1,firsty[0]))
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(6,ar_size-6)
				food_y=random.randint(6,ar_size-6)
				self.play_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==6:
			self.snake_arr.reverse()
			if firsty[1]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.snake_arr.append((0,firsty[0]))
				
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(6,ar_size-6)
				food_y=random.randint(6,ar_size-6)
				self.play_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
			
			
			self.updator()

def main():
	
	speeder=0
	
	snak=snake()

	while True:
		# speeder+=0.01		
		

		
		clock.tick(FPS+int(speeder))
		# pygame.time.delay(100)
		# os.system("cls")
		snak.mover()

		
		
		# for i in range(len(snak.play_matrix)):
		# 	print(snak.play_matrix[i])
		






main()



