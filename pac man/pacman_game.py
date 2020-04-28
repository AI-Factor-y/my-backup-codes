''''
Pacman classic game by abhinav p


'''






import numpy as np
import time
import random
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



''' 0=food
	1=wall
	2=big food
	3=pacman
	4=ghost1
	5=ghost2
	8=empty position
	'''

#global variable gallery
path=[]
backpath=[]
direction=4
blink_pac=1
score=0   #for scoring systems

# level=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# 	   [1,2,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
# 	   [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
# 	   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
# 	   [1,0,1,0,1,1,0,1,1,8,8,1,1,0,1,1,0,1,0,1],
# 	   [1,0,0,0,0,0,0,1,4,8,8,5,1,0,0,0,0,0,0,1],
# 	   [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
# 	   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
# 	   [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
# 	   [1,0,0,0,0,1,0,0,0,0,3,0,0,0,1,0,0,0,2,1],
# 	   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#construct a level creator============================

'''
in the level creator file ::::
= and + stands for walls
- stands for open space
space(' ') stands for food
* stands for big food
p stands for pacman
g stands for ghosts
'''
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
# ==========================================================================



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
		delay=70
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

		if self.delayer2(100):
			self.move_ghost()
	def move_ghost(self):
		global level,path,eat_ghosts,backpath
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
				pygame.mixer.music.stop()
				pygame.mixer.music.load('pacmandie.mp3')
				pygame.mixer.music.set_volume(0.6)

				pygame.mixer.music.play(0)
				time.sleep(2)
				print("gameOver")#exit and game over when pac man hits a ghost

				self.introscreen()
				gameover=True
				break
			if gameOver:
				break
			

	def introscreen(self):
		global width,height,level,game,score
		intro =True
		pygame.mixer.music.load("intro.mp3")
		pygame.mixer.music.play(-1)
		
		while intro:
			gameDisplay.blit(background,(0,0,width,height))
			text = STAT_FONT.render("  Game Over",1, (255,255,255))
			gameDisplay.blit(text, (width/2-80,120))
			text1 = STAT_FONT.render("        Score : "+str(score),1, (255,0,0))
			gameDisplay.blit(text1, (width/2+140,120))
			
			highscore=np.load("highscores.npy")
			highscore=np.append(highscore,score)
			np.save("highscores",highscore)
			high=int(np.max(highscore))
			text3 = STAT_FONT.render("Highscore : "+str(high),1, (255,0,0))
			gameDisplay.blit(text3, (width/2-340,120))
			text2 = STAT_FONT.render("press any key to start",1, (255,255,255))
			gameDisplay.blit(text2, (width/2-130,height-40))
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					intro=False
				if event.type==pygame.QUIT:
					exit()

			pygame.display.update()
		pygame.mixer.music.stop()
		level=create_level()
		self.__init__()




	def valid_move(self,move):
		global level
		if level[move[0]][move[1]]==1:
			return False
		else:
			return True

	def update_level(self,old_pos,new_pos):
		global level,scary_ghost_timer,eat_ghosts,blink_pac,score  #activates when the pacman eats a big food ability to kill ghosts
		level[new_pos[0]][new_pos[1]]=3
		level[old_pos[0]][old_pos[1]]=8

		blink_pac*=-1
		if new_pos in self.food:
			score+=1
			pygame.mixer.music.load('pacmaneat.mp3')
			pygame.mixer.music.set_volume(0.1)
			pygame.mixer.music.play(0)
			
			self.food.pop(self.food.index((new_pos)))
		if new_pos in self.big_food:
			score+=5
			self.big_food.pop(self.big_food.index((new_pos)))
			eat_ghosts=True
		if eat_ghosts==True:
			pygame.mixer.music.load('pacmanghost.mp3')
			pygame.mixer.music.set_volume(0.3)
			pygame.mixer.music.play(0)
			scary_ghost_timer+=1
			if scary_ghost_timer>20:
				eat_ghosts=False
				pygame.mixer.music.stop()
				scary_ghost_timer=0

			if new_pos in self.ghosts:
				score+=5
				died=self.ghosts.pop(self.ghosts.index((new_pos)))
				self.eaten_ghost.append(died)

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

class display:
	global width,height,gameDisplay
	global level

	def __init__(self):
		global level
		self.pacman=pacman_game()
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
		
		while run:

			gameDisplay.fill(0)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit()
					run=False

			self.show_frame()
			active_move=self.get_move(active_move)
			direction=active_move
			self.pacman.move_pacman(active_move)

			pygame.display.update()


#implementing astar algorithm for ghosts========================

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


def introscreen_first():
		global width,height,level,game
		intro =True
		pygame.mixer.music.load("intro.mp3")
		pygame.mixer.music.play(-1)
		
		while intro:
			gameDisplay.blit(background,(0,0,width,height))
			
			text2 = STAT_FONT.render("press any key to start",1, (255,255,255))
			gameDisplay.blit(text2, (width/2-140,height-40))
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					intro=False
				if event.type==pygame.QUIT:
					exit()

			pygame.display.update()
		pygame.mixer.music.stop()
		level=create_level()
		


#main function====================================================

if __name__=="__main__":
	#==========game name==============
	pygame.display.set_caption("pacman classic")
	#==================================
	start_value=0  #starting the global game timer for recieving inputs
	start_value2=0 #for path finding of ghosts
	scary_ghost_timer=0
	eat_ghosts=False
	introscreen_first()
	game=display()
	game.RunGame()

					

	

