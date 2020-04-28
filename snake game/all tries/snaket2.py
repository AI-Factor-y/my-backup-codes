import neat
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
	
		


def mover(obj):
	global food_x
	global food_y
	direction=obj.directions
	firsty=obj.searcher(1)
	# controls........................................................................
	pygame.display.update()
	screen.fill(white)


	obj.header_x=obj.snake_arr[0][0]
	obj.header_y=obj.snake_arr[0][1]

	# for i in range(1,len(obj.snake_arr)):
		
	# 		if obj.header_x==obj.snake_arr[i][0]:
	# 			if obj.header_y==obj.snake_arr[i][1]:
	# 				exit()

	if obj.snake_arr[0][0]==food_y and obj.snake_arr[0][1]==food_x:

			food_x=random.randint(0,ar_size-1)
			food_y=random.randint(0,ar_size-1)
			obj.play_matrix[food_x][food_y]=-1
	
	for i in range(len(obj.snake_arr)):
		pygame.draw.rect(screen,(0,255,0),(obj.snake_arr[i][0]*20,obj.snake_arr[i][1]*20,10,10))

	pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))
	

	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	
	
	if direction==8:
		obj.snake_arr.reverse()
		if firsty[0]!=0:
			
			obj.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
		else:
			pass
		obj.snake_arr.reverse()
		if obj.snake_arr[0][0]==food_y and obj.snake_arr[0][1]==food_x:

			food_x=random.randint(0,ar_size-1)
			food_y=random.randint(0,ar_size-1)
			obj.play_matrix[food_x][food_y]=-1
			
		else:
			obj.tail=obj.snake_arr.pop()
			
		obj.updator()

	if direction==2:
		obj.snake_arr.reverse()
		if firsty[0]!=(ar_size-1):

			
			obj.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
		else:
			pass
		obj.snake_arr.reverse()
		if obj.snake_arr[0][0]==food_y and obj.snake_arr[0][1]==food_x:
			food_x=random.randint(0,ar_size-1)
			food_y=random.randint(0,ar_size-1)
			obj.play_matrix[food_x][food_y]=-1
			
		else:
			obj.tail=obj.snake_arr.pop()
			
		obj.updator()

	if direction==4:
		obj.snake_arr.reverse()
		if firsty[1]!=(0):

			
			obj.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
		else:
			pass
		obj.snake_arr.reverse()
		if obj.snake_arr[0][0]==food_y and obj.snake_arr[0][1]==food_x:
			food_x=random.randint(0,ar_size-1)
			food_y=random.randint(0,ar_size-1)
			obj.play_matrix[food_x][food_y]=-1
			
		else:
			obj.tail=obj.snake_arr.pop()
			
		obj.updator()

	if direction==6:
		obj.snake_arr.reverse()
		if firsty[1]!=(ar_size-1):

			
			obj.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
		else:
			pass
		obj.snake_arr.reverse()
		if obj.snake_arr[0][0]==food_y and obj.snake_arr[0][1]==food_x:
			food_x=random.randint(0,ar_size-1)
			food_y=random.randint(0,ar_size-1)
			obj.play_matrix[food_x][food_y]=-1
			
		else:
			obj.tail=obj.snake_arr.pop()
		
		
		obj.updator()








		
			

		


def gameplay(genomes,config):
	global food_y
	global food_x
	while True:
		nets=[]
		ge=[]
		snakes=[]
		
	    
		for genome_id, genome in genomes:
			genome.fitness = 0  # start with fitness level of 0
			net = neat.nn.FeedForwardNetwork.create(genome, config)
			nets.append(net)
			snakes.append(snake())
			ge.append(genome)

	     





		

		# if keyboard.is_pressed('i'):
		# 	snak.directions=8
		# if keyboard.is_pressed('l'):
		# 	snak.directions=6
		# if keyboard.is_pressed('j'):
		# 	snak.directions=4
		# if keyboard.is_pressed('m'):
		# 	snak.directions=2
		# if keyboard.is_pressed('h'):
		# 	snak.directions=1
		for x,snak in enumerate(snakes):
			ge[x].fitness+=0.1
			distance=((snak.snake_arr[0][0]-food_y)**2+(snak.snake_arr[0][1]-food_x)**2)**0.5
			s_head_x=snak.snake_arr[0][0]
			s_head_y=snak.snake_arr[0][1]
			s_food_x=food_y
			s_food_y=food_x
			s_direction=snak.snake_director()

			output=nets[x].activate((int(distance),int(s_head_x),int(s_head_y),int(s_food_x),int(s_food_y)))
			
			if(output[0]>0.75):
				snak.directions=8
			if(output[1]>0.75):
				snak.directions=6
			if(output[2]>0.75):
				snak.directions=4
			if(output[3]>0.75):
				snak.directions=1

			mover(snak)




		clock.tick(FPS)
		# pygame.time.delay(100)
		# os.system("cls")
		

	
	

		






def main(config_path):
	config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

	p=neat.Population(config)
	p.add_reporter(neat.StdOutReporter(True))
	stats=neat.StatisticsReporter()
	p.add_reporter(stats)
	winner=p.run(gameplay,50)
	
	# snak=snake()

	


		
		# print(snak.snake_arr)
		# print("\n\n")
		# for i in range(len(snak.play_matrix)):
		# 	print(snak.play_matrix[i])
if __name__=="__main__":
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"config-feedforward.txt")
    main(config_path)
    
		








		
		
		

		# if keyboard.is_pressed('i'):
		# 	s.directions=2
		# 	snak.directions=8

		# if keyboard.is_pressed('l'):
		# 	snak.directions=6
		# 	s.directions=4
		# if keyboard.is_pressed('j'):
		# 	snak.directions=4
		# 	s.directions=6
		# if keyboard.is_pressed('m'):
		# 	snak.directions=2
		# 	s.directions=8
		# if keyboard.is_pressed('h'):
		# 	snak.directions=1
		# 	s.directions=1
		# clock.tick(60)
		# # pygame.time.delay(100)
		# os.system("cls")
		# mover(snak)
		# mover(s)

		
		# print(snak.snake_arr)
		# print(s.snake_arr)
		# print("\n\n")
		
		

		# for i in range(len(g_matrix)):
		# 	print(g_matrix[i])
		




main()



