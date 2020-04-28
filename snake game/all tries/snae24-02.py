
import neat
import pygame,sys
import keyboard
from pygame.locals import *
import os
import random
import time
import pygame
import math
pygame.init()
disp_h=600
disp_w=600
scr_size = (width,height) = (disp_h,disp_w)
FPS = 13
mini=[]  # a array used for relative seperation fitness determination
alldead=False
black = (0,0,0)
white = (255,255,255)
background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("snake game")

ar_size=30

initial_snake_len=3

g_matrix=[]
for i in range(ar_size):
	g_matrix.append([])

for i in range(ar_size):
	for j in range(ar_size):
		g_matrix[i].append(0)

class snake:
	def __init__(self):
		self.head=(10,7)
		self.tail=(10,10)
		self.length=initial_snake_len
		self.snake_arr=[]
		self.dead=False
		self.direction=2
		self.header_x=0
		self.header_y=0
		self.score=0
		self.foodx=random.randint(2,ar_size-2)
		self.foody=random.randint(2,ar_size-2)
		for i in range(self.length):
			self.snake_arr.append((self.head[0],self.head[1]+i))
		g_matrix[self.foodx][self.foody]=-1
	def updator(self):
		for i in range(len(self.snake_arr)):
			 g_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=(i+1)

		# making the snake move by removing end of snake
		g_matrix[self.tail[1]][self.tail[0]]=0

	def snake_director(self):
		# initialising the snake reverse direction
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
	

def gameplay(genomes,config):
	snakes=[]
	nets=[]
	ge=[]
	global mini
	for genome_id, genome in genomes:
		genome.fitness = 0  # start with fitness level of 0
		net = neat.nn.FeedForwardNetwork.create(genome, config)
		nets.append(net)
		snakes.append(snake())
		ge.append(genome)

	timer=0
	score=[]
	while True:

			#pfitness parameters
			wall_fitness_decrement=900
			food_fitness_increment=4500
			self_die_fitness_decrement=500
			no_improvement_decrement=800
			nearest_fitness_increment=10
			nearest_fitness_decrement=10
			if(len(snakes)==0):
				for i in range(ar_size):
					for j in range(ar_size):
						g_matrix[i][j]=0
				break
			timer+=0.1
			if timer>20:
				for x,snak in enumerate(snakes):
				
					ge[x].fitness-=no_improvement_decrement
					snakes.pop(x)
					ge.pop(x)
					nets.pop(x)

				for i in range(ar_size-1):
					for j in range(ar_size-1):
						g_matrix[i][j]=0
				break
			for x,snak in enumerate(snakes):

				distance=((snak.snake_arr[0][0]-snak.foody)**2+(snak.snake_arr[0][1]-snak.foodx)**2)**0.5
				s_head_x=snak.snake_arr[0][0]
				s_head_y=snak.snake_arr[0][1]
				s_food_x=snak.foody
				s_food_y=snak.foodx
				o1=0
				o2=0
				o3=0
				o4=0
				#adding additional fitness to closer and away species
				mini.append((abs(s_head_x-s_food_x),abs(s_head_y-s_food_y)))
				try:
					fit_x=mini[0][0]-mini[1][0]
					fit_y=mini[0][1]-mini[1][1]
					if(mini[0][0]>mini[1][0]):
						#increase fitness
						ge[x].fitness+=nearest_fitness_increment

					else:
						ge[x].fitness-=nearest_fitness_decrement
					if(mini[0][1]>mini[1][1]):
						ge[x].fitness+=nearest_fitness_increment
					else:
						ge[x].fitness-=nearest_fitness_decrement
				except:
					fit_x=ar_size-1
					fit_y=ar_size-1
					
					pass
				if(len(mini)==2):
					mini=[]
				if s_head_x+1==ar_size-1 :
					o1=1
				if s_head_x-1==0:
					o2=1
				if s_head_y+1==ar_size-1:
					o3=1
				if s_head_y-1==0:
					o4=1
				#checking whether food is there in current row or column
				if(s_head_x==s_food_x):
					row_food=1
				else:
					row_food=0
				if(s_head_y==s_food_y):
					column_food=1
				else:
					column_food=0
				# print(len(snak.snake_arr))
			#here b1 b2 b3 b4 are testers of positions of the body of the snake 
				b1,b2,b3,b4=0,0,0,0
				future_key=1
				for s in snak.snake_arr:
					
					if s_head_x+future_key==s[0] and [s_head_y]==s[1]:
						b1=1
					
					if s_head_x-future_key==s[0] and s_head_y==s[1]:
						b2=1
					
					if s_head_x==s[0] and s_head_y-future_key==s[1]:
						b3=1
					
					if s_head_x==s[0] and s_head_y+future_key==s[1]:
						b4=1
					
				# print("b1 :",b1,"b2 : ",b2,"b3 :",b3,"b4 :",b4)
					# print("s[0]",s[0])
				
				
				try:
					angle=math.degrees(math.atan((s_food_x-s_head_x)/(s_food_y-s_head_y)))
				except:
					angle=90
				d=snak.snake_director()
				
				
				output=nets[x].activate((int(distance),o1,o2,o3,o4,b1,b2,b3,b4,row_food,column_food,fit_y,fit_x,int(s_head_x),int(s_head_y),int(s_food_x),int(s_food_y),int(d),int(angle),int((s_head_x-s_food_x)),int((s_head_y-s_food_y))))
				
				if(output[0]>0.75) and d!=2:
					snak.directions=2
				elif(output[1]>0.75) and d!=6:
					snak.directions=6
				elif(output[2]>0.75) and d!=4:
					snak.directions=4
				elif d!=8:
					snak.directions=8
				
				
			

			# moving function is now activated
			for x,snak in enumerate(snakes):
				direction=snak.directions
				firsty=snak.snake_arr[0]
				temp_a=firsty[0]
				temp_b=firsty[1]
				firsty=(temp_b,temp_a)
				snak.header_x=snak.snake_arr[0][0]
				snak.header_y=snak.snake_arr[0][1]
				snake_direction=snak.snake_director()
				self_hit_dead=False
				for i in range(1,len(snak.snake_arr)):
					if snak.header_x==snak.snake_arr[i][0]:
						if snak.header_y==snak.snake_arr[i][1]:
							for i in snak.snake_arr:
								g_matrix[i[0]][i[1]]=0
							ge[x].fitness-=self_die_fitness_decrement
							snakes.pop(x)
							nets.pop(x)
							ge.pop(x)
							self_hit_dead=True
				
				if self_hit_dead:
					continue
				
				if direction==8:
					snak.snake_arr.reverse()
					if firsty[0]!=0:
						
						snak.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
					else:
						for i in snak.snake_arr:
								g_matrix[i[0]][i[1]]=0
						ge[x].fitness-=wall_fitness_decrement # fitness decrease by hitting walls
						snakes.pop(x)
						nets.pop(x)
						ge.pop(x)
						
					snak.snake_arr.reverse()
					if snak.snake_arr[0][0]==snak.foody and snak.snake_arr[0][1]==snak.foodx:
						g_matrix[snak.foodx][snak.foody]=0
						snak.foodx=random.randint(2,ar_size-2)
						snak.foody=random.randint(2,ar_size-2)	
						g_matrix[snak.foodx][snak.foody]=-1
						snak.score+=1
						ge[x].fitness+=food_fitness_increment
						timer=0
					else:
						snak.tail=snak.snake_arr.pop()
					
					snak.updator()

				if direction==2:
					snak.snake_arr.reverse()
					if firsty[0]!=(ar_size-1):
						snak.snake_arr.append((firsty[1],firsty[0]+1))           #in tthe first tuple 1 corresponds to x and 0 to y
					else:
						for i in snak.snake_arr:
								g_matrix[i[0]][i[1]]=0
						ge[x].fitness-=20 # fitness decrease by hitting walls
						snakes.pop(x)
						nets.pop(x)
						ge.pop(x)
					snak.snake_arr.reverse()
					if snak.snake_arr[0][0]==snak.foody and snak.snake_arr[0][1]==snak.foodx:
						g_matrix[snak.foodx][snak.foody]=0
						snak.foodx=random.randint(2,ar_size-2)
						snak.foody=random.randint(2,ar_size-2)	
						g_matrix[snak.foodx][snak.foody]=-1
						snak.score+=1
						ge[x].fitness+=food_fitness_increment
						timer=0 #increase fitness upon getting food
					else:
						snak.tail=snak.snake_arr.pop()
					snak.updator()
				if direction==4:
					snak.snake_arr.reverse()
					if firsty[1]!=(0):
						snak.snake_arr.append((firsty[1]-1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
					else:
						for i in snak.snake_arr:
								g_matrix[i[0]][i[1]]=0
						ge[x].fitness-=wall_fitness_decrement # fitness decrease by hitting walls
						snakes.pop(x)
						nets.pop(x)
						ge.pop(x)	
					snak.snake_arr.reverse()
					if snak.snake_arr[0][0]==snak.foody and snak.snake_arr[0][1]==snak.foodx:
						g_matrix[snak.foodx][snak.foody]=0
						snak.foodx=random.randint(2,ar_size-2)
						snak.foody=random.randint(2,ar_size-2)	
						g_matrix[snak.foodx][snak.foody]=-1
						snak.score+=1
						ge[x].fitness+=food_fitness_increment
						timer=0 #increase fitness upon getting food	
					
					else:
						snak.tail=snak.snake_arr.pop()
						
					snak.updator()
				if direction==6:
					snak.snake_arr.reverse()
					if firsty[1]!=(ar_size-1):

						
						snak.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
					else:
						ge[x].fitness-=wall_fitness_decrement # fitness decrease by hitting walls
						snakes.pop(x)
						nets.pop(x)
						ge.pop(x)
					snak.snake_arr.reverse()
					if snak.snake_arr[0][0]==snak.foody and snak.snake_arr[0][1]==snak.foodx:
						g_matrix[snak.foodx][snak.foody]=0
						snak.foodx=random.randint(2,ar_size-2)
						snak.foody=random.randint(2,ar_size-2)	
						g_matrix[snak.foodx][snak.foody]=-1
						snak.score+=1
						ge[x].fitness+=food_fitness_increment
						timer=0 #increase fitness upon getting food	
					else:
						snak.tail=snak.snake_arr.pop()
		
					snak.updator()

			clock.tick(FPS)
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

			for snak in snakes:
				pygame.draw.rect(screen,(255,0,0),(snak.foody*20,snak.foodx*20,10,10))

def main(confg_path):
	config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

	p=neat.Population(config)
	p.add_reporter(neat.StdOutReporter(True))
	stats=neat.StatisticsReporter()
	p.add_reporter(stats)
	winner=p.run(gameplay,2000)

if __name__=="__main__":
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"config-feedforward.txt")
    main(config_path)
					







