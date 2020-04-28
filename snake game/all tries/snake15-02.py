
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

initial_snake_len=3




g_matrix=[]
for i in range(ar_size):
	g_matrix.append([])

for i in range(ar_size):
	for j in range(ar_size):
		g_matrix[i].append(0)

#position of the food:

		



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
		self.score=0
		self.dead=False
		self.got_food=False
		self.foodx=random.randint(0,ar_size-1)
		self.foody=random.randint(0,ar_size-1)
		self.tracker=[]
		self.directions=1
		
		for i in range(initial_snake_len):
			self.snake_arr.append((self.head[0],self.head[1]+i))
		g_matrix[self.foodx][self.foody]=-1

	
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
		# initialising the snake reverse direction
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


		if self.snake_arr[0][0]==self.foody and self.snake_arr[0][1]==self.foodx:

				self.got_food=True
		try:
			snake_direction=self.snake_director()
		except:
			snake_direction=0
		if direction==8:
			self.snake_arr.reverse()
			if firsty[0]!=0:
				
				self.snake_arr.append((firsty[1],firsty[0]-1))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead=True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==self.foody and self.snake_arr[0][1]==self.foodx:

				
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
			if self.snake_arr[0][0]==self.foody and self.snake_arr[0][1]==self.foodx:
				
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
			if self.snake_arr[0][0]==self.foody and self.snake_arr[0][1]==self.foodx:
				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
				
			self.updator()

		if direction==6:
			self.snake_arr.reverse()
			if firsty[1]!=(ar_size-1):

				
				self.snake_arr.append((firsty[1]+1,firsty[0]))           #in tthe first tuple 1 corresponds to x and 0 to y
			else:
				self.dead=True
			self.snake_arr.reverse()
			if self.snake_arr[0][0]==self.foody and self.snake_arr[0][1]==self.foodx:
				
				self.got_food=True
				
			else:
				self.tail=self.snake_arr.pop()
			
		
			self.updator()

		if self.got_food==True:
			g_matrix[self.foodx][self.foody]=0
			self.foodx=random.randint(0,ar_size-1)
			self.foody=random.randint(0,ar_size-1)	
			g_matrix[self.foodx][self.foody]=-1
			print("got food")	
			self.score+=1
			self.got_food=False
			
		if self.dead==True:
			for i in range(0,len(self.snake_arr)):
				g_matrix[self.snake_arr[i][1]][self.snake_arr[i][0]]=0









		
			

		


	
	

		






def gameplay(genomes,config):
	Snakes=[]
	nets=[]
	ge=[]
	global food_x
	global food_y

	
	
	for genome_id, genome in genomes:
		genome.fitness = 0  # start with fitness level of 0
		net = neat.nn.FeedForwardNetwork.create(genome, config)
		nets.append(net)
		Snakes.append(snake())
		ge.append(genome)
	

	
	timer=0
	mega_timer=0
	score=[]
	while True:
		if(len(Snakes)==0):
			for i in range(ar_size):
				for j in range(ar_size):
					g_matrix[i][j]=0
			break
		
		for x,snak in enumerate(Snakes):
			if snak.dead!=True:
				ge[x].fitness+=snak.score+1000
			try:
				# ge[x].fitness-=0
				ge[x].fitness-=(abs(snak.snake_arr[0][0]-snak.foody))
				ge[x].fitness-=(abs(snak.snake_arr[0][1]-snak.foodx))
				pass
			except:
				pass
			if(snak.dead==True):
				ge[x].fitness-=60
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)
			
			
				# ge[x].fitness-=1
			
			
		mega_timer+=0.1
		timer+=0.1
		if mega_timer>20:
			for x,snak in enumerate(Snakes):
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)

		


		if timer>8:
			for x,snak in enumerate(Snakes):
					if len(snak.snake_arr)==3:
						ge[x].fitness-=0



		for x,snak in enumerate(Snakes):
			food_pos_x=0
			wall_x=-1
			flag_x=0
			food_pos_y=0
			wall_y=-1
			flag_y=0

			food_pos_X=0
			wall_X=-1
			flag_X=0
			food_pos_Y=0
			wall_Y=-1
			flag_Y=0
			try:
				for i in range(0,snak.snake_arr[0][0]):
					food_pos_x+=1   #also gives the distance to the wall
					if(i==snak.foodx and snak.snake_arr[0][1]==snak.foody):
						flag_x=1
						break

				if flag_x==0:
					wall_x=food_pos_x
					food_pos_x=0

				
				for i in range(0,snak.snake_arr[0][1]):
					food_pos_y+=1   #also gives the distance to the wall
					if(i==snak.foody and snak.snake_arr[0][0]==snak.foodx):
						flag_y=1
						break

				if flag_y==0:
					wall_y=food_pos_y
					food_pos_y=0

				for i in range(snak.snake_arr[0][0],ar_size-1):
					food_pos_X+=1   #also gives the distance to the wall
					if(i==snak.foodx and snak.snake_arr[0][1]==snak.foody):
						flag_X=1
						break

				if flag_X==0:
					wall_X=food_pos_X
					food_pos_X=0

				
				for i in range(snak.snake_arr[0][1]):
					food_pos_Y+=1   #also gives the distance to the wall
					if(i==snak.foody and snak.snake_arr[0][0]==snak.foodx):
						flag_Y=1
						break

				if flag_Y==0:
					wall_Y=food_pos_Y
					food_pos_Y=0
			except:
				food_pos_Y=-1
				food_pos_Y=-1
				food_pos_X=-1
				food_pos_x=-1
				wall_Y=-1
				wall_X=-1
				wall_x=-1
				wall_y=-1
			


			try:
				a=snak.snake_arr[0]

			except:
				Snakes.pop(x)
				nets.pop(x)
				ge.pop(x)
				continue
			distance1=((snak.snake_arr[0][0]-snak.foody)**2+(snak.snake_arr[0][1]-snak.foodx)**2)**0.5
			# distance2=(((snak.snake_arr[0][0]+1)-snak.foody)**2+(snak.snake_arr[0][1]-snak.foodx)**2)**0.5
			# distance3=(((snak.snake_arr[0][0])-snak.foody)**2+((snak.snake_arr[0][1]+1)-snak.foodx)**2)**0.5
			# distance4=(((snak.snake_arr[0][0]-1)-snak.foody)**2+(snak.snake_arr[0][1]-snak.foodx)**2)**0.5
			# distance5=(((snak.snake_arr[0][0])-snak.foody)**2+((snak.snake_arr[0][1]-1)-snak.foodx)**2)**0.5
			# distance6=(((snak.snake_arr[0][0]-1)-snak.foody)**2+(snak.snake_arr[0][1]-1-snak.foodx)**2)**0.5
			# distance7=(((snak.snake_arr[0][0]+1)-snak.foody)**2+(snak.snake_arr[0][1]+1-snak.foodx)**2)**0.5
			o1=0
			o2=0
			o3=0
			o4=0
#food distance


			s_head_x=snak.snake_arr[0][0]
			s_head_y=snak.snake_arr[0][1]
			s_food_x=snak.foody
			s_food_y=snak.foodx 

			fd=[abs(s_head_x+1-s_food_x),abs(s_head_x-1-s_food_x),abs(s_head_y+1-s_food_y),abs(s_head_y-1-s_food_y)]
			if(fd[0]>fd[1]):
				f1=1
			else:
				f1=0
			if(fd[2]>fd[3]):
				f2=1
			else:
				f2=0
			
			if s_head_x+1==ar_size-1:
				o1=1
			if s_head_x-1==0:
				o2=1
			if s_food_y+1==ar_size-1:
				o3=1
			if s_food_y-1==0:
				o4=1
			try:
				angle=math.degrees(math.atan((s_food_x-s_head_x)/(s_food_y-s_head_y)))
				
			except:
				angle=90
				# print(angle)
			try:
				direction=snak.snake_director()
				d=snak.snake_director()
			except:
				direction=0
				d=0
			# (s_head_x-s_food_x),(s_head_y-s_food_y)
			# try:#dont do this here rectify the error
			output=nets[x].activate((int(distance1),o1,o2,o3,o4,f1,f2,int(s_head_x),int(s_head_y),int(s_food_x),int(s_food_y),direction,angle,wall_x,wall_y,wall_X,wall_Y))
			print("*****************************")
			print(s_head_x-s_food_x)
			print(s_head_y-s_food_y)
			print("******************************")
			# except:
				# pass
# 
			if(output[0]>0.75) and d!=2:
				snak.directions=2
			elif(output[1]>0.75) and d!=6:
				snak.directions=6
			elif(output[2]>0.75) and d!=4:
				snak.directions=4
			elif d!=8:
				snak.directions=8



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

					
		for snak in Snakes:
			pygame.draw.rect(screen,(255,0,0),(snak.foody*20,snak.foodx*20,10,10))


		
		
		for snak in Snakes:
			score.append(snak.score)
		
		# os.system("cls")
		try:
			# print(max(score))
			pass
		except:
			pass
		# for i in range(len(g_matrix)):
		# 	print(g_matrix[i])

		
		
			

def main(config_path):
    
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

    p=neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats=neat.StatisticsReporter()
    p.add_reporter(stats)
    winner=p.run(gameplay,2000)
    
   # isGameQuit = introscreen()
    '''
    if not isGameQuit:
        gameplay()
        '''

if __name__=="__main__":
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"config-feedforward.txt")
    main(config_path)
    









