
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


def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def load_sprite_sheet(
        sheetname,
        nx,
        ny,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('sprites',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect


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



		
		# return g_matrix
	
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
		global food_x
		global food_y
		direction=self.directions
		firsty=self.searcher(1)
		# controls........................................................................
		pygame.display.update()
		screen.fill(white)


		self.header_x=self.snake_arr[0][0]
		self.header_y=self.snake_arr[0][1]

		for i in range(1,len(self.snake_arr)):
			
				if self.header_x==self.snake_arr[i][0]:
					if self.header_y==self.snake_arr[i][1]:
						exit()

		if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
		
		for i in range(len(self.snake_arr)):
			pygame.draw.rect(screen,(0,255,0),(self.snake_arr[i][0]*20,self.snake_arr[i][1]*20,10,10))

		pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))
		

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		
		
		if direction==8:
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				exit()
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
				exit()
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
				exit()
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
				exit()
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				food_x=random.randint(0,ar_size-1)
				food_y=random.randint(0,ar_size-1)
				g_matrix[food_x][food_y]=-1
				
			else:
				self.tail=self.snake_arr.pop()
			
			
			self.updator()








		
			

		


	
	

		






def main():
	

	
	snak=snake()
	s=snake()
	while True:
		
		
		

		if keyboard.is_pressed('i'):
			snak.directions=8
			s.directions=2
		if keyboard.is_pressed('l'):
			snak.directions=6
			s.directions=4
		if keyboard.is_pressed('j'):
			snak.directions=4
			s.directions=6
		if keyboard.is_pressed('m'):
			snak.directions=2
			s.directions=8
		if keyboard.is_pressed('h'):
			snak.directions=1
			s.directions=1
		clock.tick(FPS)
		# pygame.time.delay(100)
		os.system("cls")
		snak.mover()
		s.mover()

		
		print(snak.snake_arr)
		print("\n\n")
		for i in range(len(snak.g_matrix)):
			print(snak.g_matrix[i])
		






main()



