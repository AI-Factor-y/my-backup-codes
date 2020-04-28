import numpy as np
import keras.backend.tensorflow_backend as backend
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Activation, Flatten
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import tensorflow as tf
from collections import deque
import time
import random
from tqdm import tqdm
import os
# from PIL import Image
# import cv2
from copy import deepcopy
import pygame

pygame.init()
#dummy file for hightscores
# np.save("hightscores",np.array([]))

STAT_FONT = pygame.font.SysFont("comicsans",35)
game_wall=pygame.image.load("wall.png")
game_wall=pygame.transform.scale(game_wall,(40,40))

pacman_i=[pygame.image.load("pacman-l.png"),pygame.image.load("pacman-r.png"),pygame.image.load("pacman-u.png"),pygame.image.load("pacman-d.png")]
pacman_img=[]
for pac in pacman_i:
	pac=pygame.transform.scale(pac,(28,28))
	pacman_img.append(pac)

ghosts_i=[pygame.image.load("ghost1.png"),pygame.image.load("ghost2.png"),pygame.image.load("ghost3.png"),pygame.image.load("ghost4.png")]
ghost_img=[]
for gst in ghosts_i:
	gst=pygame.transform.scale(gst,(28,28))
	ghost_img.append(gst)

dead_g=pygame.image.load("eyes.png")
dead_g=pygame.transform.scale(dead_g,(28,28))

scary_g=pygame.image.load("deadgw.png")
scary_g=pygame.transform.scale(scary_g,(28,28))


DISCOUNT = 0.99
REPLAY_MEMORY_SIZE = 50_000  # How many last steps to keep for model training
MIN_REPLAY_MEMORY_SIZE = 1_000  # Minimum number of steps in a memory to start training
MINIBATCH_SIZE = 64  # How many steps (samples) to use for training
UPDATE_TARGET_EVERY = 5  # Terminal states (end of episodes)
MODEL_NAME = '2x256'
MIN_REWARD = -200  # For model save
MEMORY_FRACTION = 0.20

EPISODES = 20_000

epsilon = 1  # not a constant, going to be decayed
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.001

#  Stats settings
AGGREGATE_STATS_EVERY = 200  # episodes
SHOW_PREVIEW = True

path=[]
backpath=[]
direction=4
blink_pac=1
  
def create_level():
	file=open("data_file.txt")

	lines=file.readlines()
	

	arr=[]
	for i in range(len(lines)):
		arr.append([])

	for i in range(len(lines)):
		for _ in range(len(lines[1])-1):
			arr[i].append(0)
	k=0
	for x,line in enumerate(lines):
		
		for y,elem in enumerate(line):
			if elem=='=':
				arr[x][y]=1
			elif elem=='+':
				arr[x][y]=1
			elif elem=='-':
				arr[x][y]=8
			elif elem=='g':
				arr[x][y]=4+k
				k+=1
			elif elem=='p':
				arr[x][y]=3
			elif elem=='*':
				arr[x][y]=2

	return arr

#creating new level from level data of the text file
level=create_level()

numpy_lvl=np.array(level)

#main display and game control section====================================

width=750     #1000  #controls the display size
height=int((numpy_lvl.shape[0]/numpy_lvl.shape[1])*width)
game_speed=0.5 # game speed is not of its meaning ... increase of game speed actually decreases the speed
gameDisplay=pygame.display.set_mode((width,height))
background=pygame.image.load("back.jpg")
background=pygame.transform.scale(background,(width,height))


### path functions##################
class Node:
  

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position


def return_path(current_node,maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    
    
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    
    path = path[::-1]
    start_value = 0
    
    return path


def search(maze, cost, start, end,max_iterations,set_limit):
   
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    
    yet_to_visit_list = []  
    
    visited_list = [] 
    
    yet_to_visit_list.append(start_node)
    
 
    outer_iterations = 0
    # max_iterations = (len(maze) // 2) ** 10



    move  =  [[-1, 0 ], # go up
              [ 0, -1], # go left
              [ 1, 0 ], # go down
              [ 0, 1 ]] # go right


    no_rows, no_columns = np.shape(maze)
    

    
    while len(yet_to_visit_list) > 0:
        
        
        outer_iterations += 1    

        
        
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        if outer_iterations > max_iterations and set_limit==True:
            
            return return_path(current_node,maze) 
       
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        
        if current_node == end_node:
            return return_path(current_node,maze)

        
        children = []

        for new_position in move: 

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
            if (node_position[0] > (no_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (no_columns -1) or 
                node_position[1] < 0):
                continue

            
            if maze[node_position[0]][node_position[1]] == 1 or maze[node_position[0]][node_position[1]] == -1:
                continue

            
            new_node = Node(current_node, node_position)

            
            children.append(new_node)

        
        for child in children:
            
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            
            child.g = current_node.g + cost
            
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + 
                       ((child.position[1] - end_node.position[1]) ** 2)) 

            child.f = child.g + child.h

            
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) >0:
                continue

            
            yet_to_visit_list.append(child)


# def introscreen_first():
# 		global width,height,level,game
# 		intro =True
# 		pygame.mixer.music.load("intro.mp3")
# 		pygame.mixer.music.play(-1)
		
# 		while intro:
# 			gameDisplay.blit(background,(0,0,width,height))
			
# 			text2 = STAT_FONT.render("press any key to start",1, (255,255,255))
# 			gameDisplay.blit(text2, (width/2-140,height-40))
# 			for event in pygame.event.get():
# 				if event.type==pygame.KEYDOWN:
# 					intro=False
# 				if event.type==pygame.QUIT:
# 					exit()

# 			pygame.display.update()
# 		pygame.mixer.music.stop()
# 		level=create_level()

def add_diamension(arr,width,height):

	for i in range(height):
		for j in range(width):
			arr[i][j]=[arr[i][j]]

	arr=np.array(arr)
	return arr
def remove_diamension(arr,width,height):
	
	for i in range(height):
		for j in range(width):
			
			arr[i][j]=arr[i][j][0]

	
	return arr


class pacman_game:

	global level

	def __init__(self):
		global level
		
		numpy_lvl=np.array(level)

		self.width=numpy_lvl.shape[1]
		self.height=numpy_lvl.shape[0]

		self.ghost_num=self.get_ghost_num()
		self.initial_ghost_pos=(5,9)
		self.pacman=(None,None)
		self.food=[]
		self.big_food=[]
		self.ghosts=[]
		self.eaten_ghost=[]
		self.walls=[]
		# self.MIN_REWARD=
		self.FOOD_REWARD=25
		self.GHOST_REWARD=50
		self.DIE_NEG_REWARD=300
		self.BIG_FOOD_REWARD=100
		self.reward=10

		self.find_all()  #finds all positions

	
	def get_ghost_num(self):
		global level
		k=0
		for i in range(self.height):
			for j in range(self.width):
				if level[i][j]==4+k:
					k+=1
		return k

	def find_all(self):
		global level
		for i in range(self.height):
			for j in range(self.width):
				if level[i][j]==3:
					self.pacman=(i,j)

				elif level[i][j]==0:
					self.food.append((i,j))

				elif level[i][j]==2:
					self.big_food.append((i,j))

				elif level[i][j]==1:
					self.walls.append((i,j))
				
	
	

		for ghost in range(self.ghost_num):

			for i in range(self.height):
				for j in range(self.width):
					if level[i][j]==4+ghost:
						self.ghosts.append((i,j))

	def move_pacman(self,move):
		global level,game_speed
		level=remove_diamension(level,self.width,self.height)
		delay=1
		conv=[8,2,4,6]
		move=conv[move]
		if move==8:

			move=(self.pacman[0]-1,
				  self.pacman[1])
			if self.valid_move(move) and self.delayer(delay):
				self.update_level(self.pacman,move)
				self.pacman=move


		elif move==2:
			move=(self.pacman[0]+1,
				  self.pacman[1])
			if self.valid_move(move) and self.delayer(delay):
				self.update_level(self.pacman,move)
				self.pacman=move

		elif move==6:
			move=(self.pacman[0],
				  self.pacman[1]+1)
			if self.valid_move(move) and self.delayer(delay):
				self.update_level(self.pacman,move)
				self.pacman=move

		elif move==4:
			move=(self.pacman[0],
				  self.pacman[1]-1)
			if self.valid_move(move) and self.delayer(delay):
				self.update_level(self.pacman,move)
				self.pacman=move

		if self.delayer2(3):
			self.move_ghost()
		
		return add_diamension(level,self.width,self.height), self.reward, done
	def move_ghost(self):
		global level,path,eat_ghosts,backpath,done
		gameOver=False
		path=[]

		start=[]
		end=[]

		start_death=[]
		end_death=self.initial_ghost_pos
		backpath=[]
		cost=1
		for i,ghost in enumerate(self.eaten_ghost):
			start_death.append(ghost)
		if len(self.eaten_ghost)>0:
			for y in range(len(self.eaten_ghost)):
				backpath.append(search(level,cost, start_death[y], end_death,10,True))
			for y in range(len(self.eaten_ghost)):
				if len(backpath[y])>1:
					
					self.eaten_ghost[y]=backpath[y][1]
			y=0
			norm=0
			while y<len(self.eaten_ghost)-norm:
				
					# print(self.eaten_ghost[y])
				if self.eaten_ghost[y]==end_death:
					reborn_ghost=self.eaten_ghost.pop(y)
					self.ghosts.append(reborn_ghost)
					y-=1
					norm+=1
					# print("appended")
				y+=1


		for i,ghost in enumerate(self.ghosts):
			start.append(ghost)
			if eat_ghosts:
				end.append((self.pacman[0],self.width-self.pacman[1]-4*i))
			else:
				end.append((self.pacman[0],self.pacman[1]-4*i))

		
		



		
		prev_paths=deepcopy(path)
		
		


		
		for x in range(len(self.ghosts)):
			path.append(search(level,cost, start[x], end[x],10,True))

		for x in range(len(self.ghosts)):
			if path[x]==None:
				prev_paths[x].pop(0)
				path[x]=prev_paths[x]

			if len(path[x])>1 :  #the find ghost which actually targets the pacman
				self.ghosts[x]=path[x][1]
			# else:
			# 	print("gameOver")  #gameover scene required
			# 	if self.ghosts[x]==self.pacman:
			# 		exit()

			if self.ghosts[x]==self.pacman and eat_ghosts==False:
				self.reward=-self.DIE_NEG_REWARD
				# pygame.mixer.music.stop()
				# pygame.mixer.music.load('pacmandie.mp3')
				# pygame.mixer.music.set_volume(0.6)

				# pygame.mixer.music.play(0)
				# time.sleep(2)
				# print("gameOver")#exit and game over when pac man hits a ghost

				# self.introscreen()
				gameover=True
				done=True
				break
			if gameOver:
				break
		
			

	# def introscreen(self):
	# 	global width,height,level,game,reward
	# 	intro =True
	# 	pygame.mixer.music.load("intro.mp3")
	# 	pygame.mixer.music.play(-1)
		
	# 	while intro:
	# 		gameDisplay.blit(background,(0,0,width,height))
	# 		text = STAT_FONT.render("  Game Over",1, (255,255,255))
	# 		gameDisplay.blit(text, (width/2-80,120))
	# 		text1 = STAT_FONT.render("        Score : "+str(reward),1, (255,0,0))
	# 		gameDisplay.blit(text1, (width/2+140,120))
			
	# 		highreward=np.load("highrewards.npy")
	# 		highreward=np.append(highreward,reward)
	# 		np.save("highrewards",highreward)
	# 		high=int(np.max(highreward))
	# 		text3 = STAT_FONT.render("Highreward : "+str(high),1, (255,0,0))
	# 		gameDisplay.blit(text3, (width/2-340,120))
	# 		text2 = STAT_FONT.render("press any key to start",1, (255,255,255))
	# 		gameDisplay.blit(text2, (width/2-130,height-40))
	# 		for event in pygame.event.get():
	# 			if event.type==pygame.KEYDOWN:
	# 				intro=False
	# 			if event.type==pygame.QUIT:
	# 				exit()

	# 		pygame.display.update()
	# 	pygame.mixer.music.stop()
	# 	level=create_level()
	# 	self.__init__()




	def valid_move(self,move):
		global level
		# print(move)
		if level[move[0]][move[1]]==1:
			return False
		else:
			return True

	def update_level(self,old_pos,new_pos):
		global level,scary_ghost_timer,eat_ghosts,blink_pac  #activates when the pacman eats a big food ability to kill ghosts
		level[new_pos[0]][new_pos[1]]=3
		level[old_pos[0]][old_pos[1]]=8

		blink_pac*=-1
		if new_pos in self.food:
			self.reward=self.FOOD_REWARD 
			# pygame.mixer.music.load('pacmaneat.mp3')
			# pygame.mixer.music.set_volume(0.1)
			# pygame.mixer.music.play(0)
			
			self.food.pop(self.food.index((new_pos)))
		if new_pos in self.big_food:
			self.reward=self.BIG_FOOD_REWARD
			self.big_food.pop(self.big_food.index((new_pos)))
			eat_ghosts=True
		if eat_ghosts==True:
			# pygame.mixer.music.load('pacmanghost.mp3')
			# pygame.mixer.music.set_volume(0.3)
			# pygame.mixer.music.play(0)
			scary_ghost_timer+=1
			if scary_ghost_timer>20:
				eat_ghosts=False
				# pygame.mixer.music.stop()
				scary_ghost_timer=0

			if new_pos in self.ghosts:
				self.reward=self.GHOST_REWARD
				died=self.ghosts.pop(self.ghosts.index((new_pos)))
				self.eaten_ghost.append(died)
		# for i in range(self.height):
		# 	for j in range(self.width):
		# 		if level[i][j]==4:
		# 			level[i][j]=0
		# for ghosts in self.ghosts:
		# 	level[ghosts[0]][ghosts[1]]=4
		
	def delayer(self,delay):
		global start_value,game_speed
		
		if start_value>(1000):
			start_value=1
		start_value+=1
		if start_value%delay==0:

			return True
		else:
			return False
	def delayer2(self,delay):
		global start_value2,game_speed
		
		if start_value2>1000:
			start_value2=1
		start_value2+=1
		if start_value2%delay==0:

			return True
		else:
			return False


class display_ENV:
	global width,height,gameDisplay
	global level

	def __init__(self):
		global level
		self.pacman=pacman_game()
		self.width=width
		self.height=height
		#colors===============
		self.OBSERVATION_SPACE_VALUES=(np.array(level).shape[0],np.array(level).shape[1],1)
		self.white=(255,255,255)
		self.red=(255,0,0)
		self.yellow=(239,228,26)
		self.blue=(0,0,255)
		self.green=(0,255,0)
		self.black=(0,0,0)
		#=====================
		self.ACTION_SPACE_SIZE=4
		self.scaleX=self.width//self.pacman.width
		self.scaleY=self.height//self.pacman.height

	def reset(self):
		global level
		level=create_level()
		self.pacman=pacman_game()
		# self.pacman.ghosts=[]
		# self.pacman.eaten_ghost=[]
		self.width=width
		self.height=height
		#colors===============
		self.white=(255,255,255)
		self.red=(255,0,0)
		self.yellow=(239,228,26)
		self.blue=(0,0,255)
		self.green=(0,255,0)
		self.black=(0,0,0)
		#=====================
		self.scaleX=self.width//self.pacman.width
		self.scaleY=self.height//self.pacman.height
		
		return add_diamension(level,self.pacman.width,self.pacman.height)


	def rectangle(self,x,y,w,h,color,t):

		pygame.draw.line(gameDisplay,color,(x,y),(x+w,y),t)
		pygame.draw.line(gameDisplay,color,(x+w,y),(x+w,y+h),t)
		pygame.draw.line(gameDisplay,color,(x+w,y+h),(x,y+h),t)
		pygame.draw.line(gameDisplay,color,(x,y+h),(x,y),t)



	def show_frame(self):
		global level,eat_ghosts,direction,blink_pac,game_wall
		#wall
		for wall in self.pacman.walls:
			# pygame.draw.rect(gameDisplay,self.blue,(wall[1]*self.scaleY,wall[0]*self.scaleX,self.scaleY,self.scaleX))
					
			# gameDisplay.blit(game_wall,(wall[1]*self.scaleY,wall[0]*self.scaleX,self.scaleY,self.scaleX))			# pygame.draw.rect(gameDisplay,self.black,(wall[1]*self.scaleY+10,wall[0]*self.scaleX-10,self.scaleY,self.scaleX))									 
			self.rectangle(wall[1]*self.scaleY,wall[0]*self.scaleX,self.scaleY,self.scaleX,self.blue,5)
		
			

		#food

		for food in self.pacman.food:
			pygame.draw.circle(gameDisplay,self.yellow,(food[1]*self.scaleY+self.scaleY//2,food[0]*self.scaleX+self.scaleX//2),5)

		for food in self.pacman.big_food:
			pygame.draw.circle(gameDisplay,self.yellow,(food[1]*self.scaleY+self.scaleY//2,food[0]*self.scaleX+self.scaleX//2),10)

		#pacman
		# pygame.draw.circle(gameDisplay,self.yellow,(self.pacman.pacman[1]*self.scaleY+self.scaleY//2,self.pacman.pacman[0]*self.scaleX+self.scaleX//2),15)
		
		pac_dir=0
		if direction==4:
			pac_dir=0
		elif direction==6:
			pac_dir=1
		elif direction==8:
			pac_dir=2
		elif direction==2:
			pac_dir=3
		if blink_pac==1:
			gameDisplay.blit(pacman_img[pac_dir],(self.pacman.pacman[1]*self.scaleY+self.scaleY//2-15,self.pacman.pacman[0]*self.scaleX+self.scaleX//2-15))
		else:
			pygame.draw.circle(gameDisplay,self.yellow,(self.pacman.pacman[1]*self.scaleY+self.scaleY//2,self.pacman.pacman[0]*self.scaleX+self.scaleX//2),15)
			
		#ghosts
		for x,ghost in enumerate(self.pacman.ghosts):

			if eat_ghosts:
				
				gameDisplay.blit(scary_g,(ghost[1]*self.scaleY+self.scaleY//2-15,ghost[0]*self.scaleX+self.scaleX//2-15))
			else:
				
				gameDisplay.blit(ghost_img[x],(ghost[1]*self.scaleY+self.scaleY//2-15,ghost[0]*self.scaleX+self.scaleX//2-15))
				# pygame.draw.circle(gameDisplay,self.red,(ghost[1]*self.scaleY+self.scaleY//2,ghost[0]*self.scaleX+self.scaleX//2),15)


		for y,ghosts in enumerate(self.pacman.eaten_ghost):
			
			# pygame.draw.circle(gameDisplay,self.white,(ghosts[1]*self.scaleY+self.scaleY//2,ghosts[0]*self.scaleX+self.scaleX//2),15)

			gameDisplay.blit(dead_g,(ghosts[1]*self.scaleY+self.scaleY//2-15,ghosts[0]*self.scaleX+self.scaleX//2-15))


		for i in range(self.pacman.height):
			for j in range(self.pacman.width):
				if level[i][j][0]==4:
					level[i][j][0]=0

		for ghost in self.pacman.ghosts:

			level[ghost[0]][ghost[1]][0]=4


	def get_move(self,active_move):
		keys=pygame.key.get_pressed()
		choice=None
		if keys[pygame.K_i]:

			choice=8
		elif keys[pygame.K_m]:
			choice=2
		elif keys[pygame.K_j]:
			choice=4
		elif keys[pygame.K_l]:
			choice=6

		if choice is not None:
			if self.validate_move(choice):
				return choice

		return active_move

	def validate_move(self,move):# two step validaton one for ai part and other for non ai
		if move==8:

			move=(self.pacman.pacman[0]-1,
				  self.pacman.pacman[1])
			if self.pacman.valid_move(move):
				return True
				


		elif move==2:
			move=(self.pacman.pacman[0]+1,
				  self.pacman.pacman[1])
			if self.pacman.valid_move(move):
				return True

		elif move==6:
			move=(self.pacman.pacman[0],
				  self.pacman.pacman[1]+1)
			if self.pacman.valid_move(move):
				return True
				

		elif move==4:
			move=(self.pacman.pacman[0],
				  self.pacman.pacman[1]-1)
			if self.pacman.valid_move(move):
				return True
				



	def RunGame(self):
		global level,direction
		run=True
		active_move=None
		clock=pygame.time.Clock()
		
		while run:  # same as while done

			gameDisplay.fill(0)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					# exit()
					run=False

			self.show_frame()
			active_move=self.get_move(active_move)
			direction=active_move
			self.pacman.move_pacman(active_move)

			pygame.display.update()

class DQNAgent:
    def __init__(self):

        # Main model
        self.model = self.create_model()

        # Target network
        self.target_model = self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        # An array with last n steps for training
        self.replay_memory = deque(maxlen=REPLAY_MEMORY_SIZE)

        # Custom tensorboard object
        # self.tensorboard = ModifiedTensorBoard(log_dir="logs/{}-{}".format(MODEL_NAME, int(time.time())))

        # Used to count when to update target network with main network's weights
        self.target_update_counter = 0

    def create_model(self):
        model = Sequential()

        model.add(Conv2D(16, (2, 2), input_shape=env.OBSERVATION_SPACE_VALUES))  # OBSERVATION_SPACE_VALUES = (10, 10, 3) a 10x10 RGB image.
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(16, (2, 2)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))
        model.add(Conv2D(32, (2, 2)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(256))

        model.add(Dense(env.ACTION_SPACE_SIZE, activation='linear'))  # ACTION_SPACE_SIZE = how many choices (9)
        model.compile(loss="mse", optimizer=Adam(lr=0.001), metrics=['accuracy'])
        return model

    # Adds step's data to a memory replay array
    # (observation space, action, reward, new observation space, done)
    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)

    # Trains main network every step during episode
    def train(self, terminal_state, step):

        # Start training only if certain number of samples is already saved
        if len(self.replay_memory) < MIN_REPLAY_MEMORY_SIZE:
            return

        # Get a minibatch of random samples from memory replay table
        minibatch = random.sample(self.replay_memory, MINIBATCH_SIZE)

        # Get current states from minibatch, then query NN model for Q values
        current_states = np.array([transition[0] for transition in minibatch])
        
        current_qs_list = self.model.predict(current_states)

        # Get future states from minibatch, then query NN model for Q values
        # When using target network, query it, otherwise main network should be queried
        new_current_states = np.array([transition[3] for transition in minibatch])
        future_qs_list = self.target_model.predict(new_current_states)

        X = []
        y = []

        # Now we need to enumerate our batches
        for index, (current_state, action, reward, new_current_state, done) in enumerate(minibatch):

            # If not a terminal state, get new q from future states, otherwise set it to 0
            # almost like with Q Learning, but we use just part of equation here
            if not done:
                max_future_q = np.max(future_qs_list[index])
                new_q = reward + DISCOUNT * max_future_q
            else:
                new_q = reward

            # Update Q value for given state
            current_qs = current_qs_list[index]
            current_qs[action] = new_q

            # And append to our training data
            X.append(current_state)
            y.append(current_qs)

        # Fit on all samples as one batch, log only on terminal state
        self.model.fit(np.array(X)/255, np.array(y), batch_size=MINIBATCH_SIZE, verbose=0, shuffle=False if terminal_state else None)

        # Update target network counter every episode
        if terminal_state:
            self.target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
        if self.target_update_counter > UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    # Queries main network for Q values given current observation space (environment state)
    def get_qs(self, state):
        return self.model.predict(np.array(state).reshape(-1, *state.shape)/255)[0]


env=display_ENV()

ep_rewards=[-200]
random.seed(1)
np.random.seed(1)
tf.random.set_seed(1)


agent=DQNAgent()

for episode in tqdm(range(1, EPISODES + 1), ascii=True, unit='episodes'):

	episode_reward=0
	step=1

	current_state=env.reset()
	for i in range(current_state.shape[0]):
		for j in range(current_state.shape[1]):
			if current_state[i][j][0] in [4,5,6,7]:
				current_state[i][j][0]=4


	start_value=0  #starting the global game timer for recieving inputs
	start_value2=0 #for path finding of ghosts
	scary_ghost_timer=0
	eat_ghosts=False

	prev_action=0
	done=False
	
	while not done:
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()
				# pass
		if np.random.random()>epsilon:

			action=np.argmax(agent.get_qs(current_state))
		else:

			action=np.random.randint(0,4)


		if not env.validate_move(action):
			action=prev_action

		new_state,reward,done=env.pacman.move_pacman(action)
		prev_action=action
		episode_reward += reward

		if SHOW_PREVIEW and not episode % AGGREGATE_STATS_EVERY:
			gameDisplay.fill(0)
			env.show_frame()

			pygame.display.update()
			

		# for i in range(11):
		# 	print(level[i])
		# os.system("cls")
		# env.show_frame()
		# pygame.display.update()
		agent.update_replay_memory((current_state, action, reward, new_state, done))

		agent.train(done,step)

		current_state=new_state

		step+=1
	pygame.display.update()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit()
			
	ep_rewards.append(episode_reward)

	if not episode % AGGREGATE_STATS_EVERY or episode==1:

		average_reward = sum(ep_rewards[-AGGREGATE_STATS_EVERY:])/len(ep_rewards[-AGGREGATE_STATS_EVERY:])
		min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
		max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])

		if min_reward>=MIN_REWARD:
			# agent.model.save(f'models/{MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f}avg_{min_reward:_>7.2f}min__{int(time.time())}.model')
			pass
	if epsilon > MIN_EPSILON:
		epsilon *= EPSILON_DECAY
		epsilon = max(MIN_EPSILON,epsilon)

