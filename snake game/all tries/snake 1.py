import pygame
import keyboard
from pygame.locals import *
import os
import random
import time

#global snake variables
ar_size=30
food_x=random.randint(0,ar_size-1)
food_y=random.randint(0,ar_size-1)
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


class snake():
	def __init__(self):
		self.head=(10,7)
		self.tail=(10,10)
		self.speed=1
		self.length=3
		self.snake_arr=[]
		self.play_matrix=[]
		self.tracker=[]
		self.play_matrix=g_matrix()
		for i in range(initial_snake_len):
			self.snake_arr.append((self.head[0],self.head[1]+i))

	
	def init_snake(self):
		
		
		
		for i in range(initial_snake_len):
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
		
		return (x,y)


	

	def snake_director(self):
		# initialising the snake
		self.init_snake()
		first=self.searcher(1)
		second=self.searcher(2)

		# UP
		if(first[0]==second[0]):
			if(first[1]>second[1]):
				return 4
		# DOWN
		if(first[0]==second[0]):
			if(first[1]<second[1]):
				return 6

		# LEFT
		if(first[1]==second[1]):
			if(first[0]<second[0]):
				return 8
		
		# RIGHT
		if(first[1]==second[1]):
			if(first[0]>second[0]):
				return 2



	def mover(self):
		
		direction=1
		firsty=self.searcher(1)
		# controls........................................................................
		
		if direction==8:
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				exit()
			self.snake_arr.reverse()
			self.tail=self.snake_arr.pop()
			self.updator()

		if direction==2:
			self.snake_arr.reverse()
			if firsty[0]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				exit()
			self.snake_arr.reverse()
			self.tail=self.snake_arr.pop()
			self.updator()

		if direction==4:
			self.snake_arr.reverse()
			if firsty[1]!=(0):

				
				self.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				exit()
			self.snake_arr.reverse()
			self.tail=self.snake_arr.pop()
			self.updator()

		if direction==6:
			self.snake_arr.reverse()
			if firsty[1]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				exit()
			self.snake_arr.reverse()
			self.tail=self.snake_arr.pop()
			self.updator()









		
			

		


	
	

		






def main():
	


	snak=snake()

	while True:
		if keyboard.is_pressed('w'):
			snak.directions=8
			
		time.sleep(0.5) 
		snak.mover()

		
		print(snak.snake_arr)
		for i in range(len(snak.play_matrix)):
			print(snak.play_matrix[i])
		






main()



