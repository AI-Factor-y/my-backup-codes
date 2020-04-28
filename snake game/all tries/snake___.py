
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
starter=1
path=0

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

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
   
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

   
    while len(open_list) > 0:

        
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        
        open_list.pop(current_index)
        closed_list.append(current_node)

        
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:                
                path.append(current.position)
                current = current.parent
            return path[::-1] 
        
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

           
            new_node = Node(current_node, node_position)

         
            children.append(new_node)

     
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            
            open_list.append(child)

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
	food_x=random.randint(0,ar_size-1)
	food_y=random.randint(0,ar_size-1)
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
		self.play_matrix=g_matrix()
		for i in range(initial_snake_len):
			self.snake_arr.append((self.head[0],self.head[1]+i))

	
	def init_snake(self):
		
		
		
		for i in range(len(self.snake_arr)):
			 self.play_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(1)



		
		# return self.play_matrix
	
	def updator(self):
		for i in range(len(self.snake_arr)):
			 self.play_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(1)

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
		# initialising the snake function returns the direction opposite to snake direction
		self.init_snake()
		first=self.snake_arr[0]
		second=self.snake_arr[1]

		# UP
		if(first[0]==second[0]):
			if(first[1]>second[1]):
				return 8
		# DOWN
		if(first[0]==second[0]):
			if(first[1]<second[1]):
				return 2

		# LEFT
		if(first[1]==second[1]):
			if(first[0]<second[0]):
				return 6
		
		# RIGHT
		if(first[1]==second[1]):
			if(first[0]>second[0]):
				return 4
	
		

	def mover(self):
		d=self.snake_director()
		# if keyboard.is_pressed('i') and d!=8:
		# 	self.directions=8
		# if keyboard.is_pressed('l') and d!=6:
		# 	self.directions=6
		# if keyboard.is_pressed('j') and d!=4:
		# 	self.directions=4
		# if keyboard.is_pressed('m') and d!=2:
		# 	self.directions=2
		# if keyboard.is_pressed('h'):
		# 	self.directions=1
		
		global food_x,path,starter
		global food_y
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

		for i in range(1,len(self.snake_arr)):
			
				if self.header_x==self.snake_arr[i][0]:
					if self.header_y==self.snake_arr[i][1]:
						exit()
						

		if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				self.play_matrix[food_x][food_y]=-1
		
		pygame.draw.rect(screen,(0,0,255),(self.snake_arr[0][0]*20,self.snake_arr[0][1]*20,10,10))
		for i in range(1,len(self.snake_arr)):
			pygame.draw.rect(screen,(0,255,0),(self.snake_arr[i][0]*20,self.snake_arr[i][1]*20,10,10))

		pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))
		if starter==1:
			nextpos = astar(self.play_matrix,(self.header_x,self.header_y),(food_x,food_y))
			starter=0

		# nextpos=(20,20)
		if(nextpos[path]>self.header_x):
			direction=6
		if nextpos[path]<self.header_x:
			direction=4
		if nextpos[path]==self.header_x:
			if nextpos[path]>self.header_y:
				direction=2
			if nextpos[path]<self.header_y:
				direction=8


		path+=1
		
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

				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				self.play_matrix[food_x][food_y]=-1
				nextpos = astar(self.play_matrix,(self.header_x,self.header_y),(food_x,food_y))
				path=0
				
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
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				self.play_matrix[food_x][food_y]=-1
				nextpos = astar(self.play_matrix,(self.header_x,self.header_y),(food_x,food_y))
				path=0
				
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
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				self.play_matrix[food_x][food_y]=-1
				nextpos = astar(self.play_matrix,(self.header_x,self.header_y),(food_x,food_y))
				path=0
				
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
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				self.play_matrix[food_x][food_y]=-1
				nextpos = astar(self.play_matrix,(self.header_x,self.header_y),(food_x,food_y))
				path=0
				
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



