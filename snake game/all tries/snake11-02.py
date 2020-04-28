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

alldead=False
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
		self.dead=False
		self.got_food=False
		self.foodx=random.randint(0,ar_size-1)
		self.foody=random.randint(0,ar_size-1)
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


	

	def snake_director(self):
		# initialising the snake
		self.init_snake()
		first=self.snake_arr[0]
		second=self.snake_arr[1]

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
						self.dead=True

		if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				self.got_food=True
		
		
		
		if direction==8:
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead=True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:

				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==2:
			self.snake_arr.reverse()
			if firsty[0]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead=True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==4:
			self.snake_arr.reverse()
			if firsty[1]!=(0):

				
				self.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead=True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==6:
			self.snake_arr.reverse()
			if firsty[1]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead-True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==food_y and self.snake_arr[0][1]==food_x:
				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
			
			
			self.updator()








		
			

		


	
	

		






def gameplay(genomes,config):
	Snakes=[]
	nets=[]
	ge=[]
	global food_x
	global food_y

	food_x=random.randint(0,ar_size-1)
	food_y=random.randint(0,ar_size-1)
	g_matrix[food_x][food_y]=-1
	
	for genome_id, genome in genomes:
		genome.fitness = 0  # start with fitness level of 0
		net = neat.nn.FeedForwardNetwork.create(genome, config)
		nets.append(net)
		Snakes.append(snake())
		ge.append(genome)
	

	
	timer=0
	mega_timer=0
	while True:
		if(len(Snakes)==0):
			for i in range(ar_size):
				for j in range(ar_size):
					g_matrix[i][j]=0
			break
		
		for x,snak in enumerate(Snakes):
			if(snak.dead==True):
				ge[x].fitness-=5
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)
			if(snak.got_food==True):
				ge[x].fitness+=30
				timer=0
		mega_timer+=0.1
		timer+=0.1
		if mega_timer>20:
			for x,snak in enumerate(Snakes):
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)

		if timer>6:
			for x,snak in enumerate(Snakes):
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)

		for x,snak in enumerate(Snakes):
			

			try:
				a=snak.snake_arr[0]

			except:
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)
				continue
			distance=((snak.snake_arr[0][0]-food_y)**2+(snak.snake_arr[0][1]-food_x)**2)**0.5
			s_head_x=snak.snake_arr[0][0]
			s_head_y=snak.snake_arr[0][1]
			s_food_x=food_y
			s_food_y=food_x
			try:
				direction=snak.snake_director()
			except:
				direction=0
		

			output=nets[x].activate((int(distance),int(s_head_x),int(s_head_y),int(s_food_x),int(s_food_y),direction))
			if(output[0]>0.5):
				snak.directions=8
			elif(output[1]>0.5):
				snak.directions=6
			elif(output[2]>0.5):
				snak.directions=4
			elif(output[3]>0.5):
				snak.directions=2



			snak.mover()


		clock.tick(FPS)
		# pygame.time.delay(100)
		
		

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		
		
		
		
		pygame.display.update()
		screen.fill(white)
		
		for x in range(len(g_matrix)):
			for y in range(len(g_matrix)):
				if(g_matrix[x][y]!=0 and g_matrix[x][y]!=( -1) and g_matrix[x][y]!=1):
					pygame.draw.rect(screen,(0,255,0),(y*20,x*20,10,10))
				if(g_matrix[x][y]==1):
					pygame.draw.rect(screen,(0,0,255),(y*20,x*20,10,10))

					
		pygame.draw.rect(screen,(255,0,0),(food_y*20,food_x*20,10,10))


		
		
		
		
		
			

def main(config_path):
    
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

    p=neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats=neat.StatisticsReporter()
    p.add_reporter(stats)
    winner=p.run(gameplay,20000)
    
   # isGameQuit = introscreen()
    '''
    if not isGameQuit:
        gameplay()
        '''

if __name__=="__main__":
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"config-feedforward.txt")
    main(config_path)
    









