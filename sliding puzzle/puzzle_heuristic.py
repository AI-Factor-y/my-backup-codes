from copy import deepcopy,copy
import pygame
import random
import time

pygame.init()
background_img=pygame.image.load("background.jpg")
frame=pygame.image.load("frame.png")
frame2=pygame.image.load("frame.png")
tile1=pygame.image.load("tile.jpeg")
tile2=pygame.image.load("tile.jpeg")
STAT_FONT = pygame.font.SysFont("comicsans",50)
stat_font_sm=pygame.font.SysFont("comicsans",30)
disp_width=800
disp_height=600
gameDisplay = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("the wooden works")
clock = pygame.time.Clock()

silver=(137,117,248)
brown=(201,126,61)
black=(0,0,0)
white=(255,255,255)
blue=(40,47,140)
def draw_background():
	global background_img
	background_img=pygame.transform.scale(background_img,(disp_width,disp_height+20))
	gameDisplay.blit(background_img,(0,0))

class square:
	

	def __init__(self,number,pos):
		self.num=number
		self.pos=pos

	def draw_square(self):
		global tile1,tile2
		x_pos=145+self.pos[0]*100
		y_pos=195+self.pos[1]*100
		tile1=pygame.transform.scale(tile1,(90,90))
		gameDisplay.blit(tile1,(x_pos,y_pos,90,90))
		# pygame.draw.rect(gameDisplay,white,(x_pos,y_pos,90,90))
		text = STAT_FONT.render(str(self.num),3, (255,0,0))
		gameDisplay.blit(text, (x_pos+33,y_pos+30))

class model_square:
	

	def __init__(self,number,pos):
		self.num=number
		self.pos=pos

	def draw_square(self):
		global tile1,tile2
		x_pos=555+self.pos[0]*60
		y_pos=205+self.pos[1]*60
		tile2=pygame.transform.scale(tile2,(55,55))
		gameDisplay.blit(tile2,(x_pos,y_pos))
		# pygame.draw.rect(gameDisplay,white,(x_pos,y_pos,55,55))
		text = stat_font_sm.render(str(self.num),3, (255,0,0))
		gameDisplay.blit(text, (x_pos+23,y_pos+20))
#145+3x90

# 400+100=500-40=460 ,,, 400-80=320-10x2=300/3=100
def board():
	board_size=380
	global frame
	frame=pygame.transform.scale(frame,(board_size,board_size))
	gameDisplay.blit(frame,(100,150))
	# pygame.draw.rect(gameDisplay,silver,(100,150,board_size,board_size))
	pygame.draw.rect(gameDisplay,black,(139,189,302,302))
def info_board():
	board_size=215
	global frame2
	frame2=pygame.transform.scale(frame2,(board_size+6,board_size+15))
	gameDisplay.blit(frame2,(533,180))

	# pygame.draw.rect(gameDisplay,silver,(550,200,board_size,board_size))
	pygame.draw.rect(gameDisplay,black,(550,200,188,185))


def search(p):
	global squares
	for sq in squares:
		if sq.pos==p:
			return sq.num-1

def search2(p):
	global squar
	for sq in squar:
		if sq.pos==p:
			return sq.num-1

def move_squares_solution(dir):
	global blank,temp_squares,squar
	squar=deepcopy(temp_squares)
	
	
	# for x,t in enumerate(temp_squares):
	# 	squar[x].pos=t.pos



	
	try:
		if dir=='d':
			posit=search2((blank[0],blank[1]-1))

			squar[posit].pos=(squar[posit].pos[0],
								squar[posit].pos[1]+1)
			
			if blank[1]>0:
				blank=(blank[0],blank[1]-1)
				
		if dir=='u':
			posit=search2((blank[0],blank[1]+1))
			squar[posit].pos=(squar[posit].pos[0],
								squar[posit].pos[1]-1)
			
			if blank[1]<2:
				blank=(blank[0],blank[1]+1)
				

		if dir=='r':
			posit=search2((blank[0]-1,blank[1]))
			squar[posit].pos=(squar[posit].pos[0]+1,
								squar[posit].pos[1])
			
			if blank[0]>0:
				blank=(blank[0]-1,blank[1])
				
		if dir=='l':
			posit=search2((blank[0]+1,blank[1]))
			squar[posit].pos=(squar[posit].pos[0]-1,
								squar[posit].pos[1])
			
			if blank[0]<2:
				blank=(blank[0]+1,blank[1])

		
				

	except:
		pass
def move_squares(dir):
	global blank,temp_squares,squares
	
	try:
		if dir=='d':
			posit=search((blank[0],blank[1]-1))

			squares[posit].pos=(squares[posit].pos[0],
								squares[posit].pos[1]+1)
			
			if blank[1]>0:
				blank=(blank[0],blank[1]-1)
				
		if dir=='u':
			posit=search((blank[0],blank[1]+1))
			squares[posit].pos=(squares[posit].pos[0],
								squares[posit].pos[1]-1)
			
			if blank[1]<2:
				blank=(blank[0],blank[1]+1)
				

		if dir=='r':
			posit=search((blank[0]-1,blank[1]))
			squares[posit].pos=(squares[posit].pos[0]+1,
								squares[posit].pos[1])
			
			if blank[0]>0:
				blank=(blank[0]-1,blank[1])
				
		if dir=='l':
			posit=search((blank[0]+1,blank[1]))
			squares[posit].pos=(squares[posit].pos[0]-1,
								squares[posit].pos[1])
			
			if blank[0]<2:
				blank=(blank[0]+1,blank[1])

		
				

	except:
		pass

def move_squares2(dir):
	global blank,temp_squares
	
	try:
		if dir=='d':
			posit=search((blank[0],blank[1]-1))

			temp_squares[posit].pos=(temp_squares[posit].pos[0],
								temp_squares[posit].pos[1]+1)
			
			if blank[1]>0:
				blank=(blank[0],blank[1]-1)
				
		if dir=='u':
			posit=search((blank[0],blank[1]+1))
			temp_squares[posit].pos=(temp_squares[posit].pos[0],
								temp_squares[posit].pos[1]-1)
			
			if blank[1]<2:
				blank=(blank[0],blank[1]+1)
				

		if dir=='r':
			posit=search((blank[0]-1,blank[1]))
			temp_squares[posit].pos=(temp_squares[posit].pos[0]+1,
								temp_squares[posit].pos[1])
			
			if blank[0]>0:
				blank=(blank[0]-1,blank[1])
				
		if dir=='l':
			posit=search((blank[0]+1,blank[1]))
			temp_squares[posit].pos=(temp_squares[posit].pos[0]-1,
								temp_squares[posit].pos[1])
			
			if blank[0]<2:
				blank=(blank[0]+1,blank[1])

		
				

	except:
		pass
def shuffle(n):
	for i in range(n):
		move_squares(random.choice(['u','d','r','l']))
		move_squares2(random.choice(['u','d','r','l']))

def check_solve():
	global solved_state,solved
	i=0
	solved=True
	for s in squares:
		
		if s.pos!=solved_state[i]:
			solved=False
		i+=1

	if solved==True:
		text = STAT_FONT.render("SOLVED,congratutions",1, (0,0,0))
		gameDisplay.blit(text, (200,550))

def check_heuristic():
	global squar
	heuris=0
	
	i=0
	for s in squar:
		# print(s.pos)
		if s.pos!=solved_state[i]:
			heuris+=1
		i+=1
	

	return heuris

def check_solution():
	global solved_state,temp_squares
	i=0
	solved=True
	print("--------------------")
	
	for s in temp_squares:
		
		if s.pos!=solved_state[i]:
			solved=False
		i+=1

	if solved==True:
		return True
	else:
		return False




def heuristic():
	#possible cases left right top down
	#we are using number of mismatch heuristic
	global solved_state,solved,squares,temp_squares,squar
	heuristics=[]
	# print(squares[0].pos)
	
	# for x,s in enumerate(squares):
	# 	temp_squares[x].pos=s.pos


	# for s in temp_squares:
	# 			print(s.pos)
	# print(temp_squares[0].pos)
	cases=[]
	possible_moves=['u','d','r','l']
	solution=[]
	while check_solution()==False:

		for mov in possible_moves:
			move_squares_solution(mov)
			for s in squar:
				print(s.pos)
			# print(sample[0].pos)
			print("-"*50)
			cases.append(squar)
			heuristics.append(check_heuristic())
		print(heuristics)
		temp_squares=cases[heuristics.index(min(heuristics))]

		solution.append(possible_moves[heuristics.index(min(heuristics))])
		print(possible_moves[heuristics.index(min(heuristics))])
		heuristics=[]

	print(solution)















if __name__=="__main__":
	blank=(2,2)
	solved=True
	squares=[]
	squar=[]
	temp_squares=[]
	info_squares=[]
	solved_state=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2)]
	#making squares:
	num=0
	for i in range(3):
		for j in range(3):
			num+=1
			squares.append(square(num,(j,i)))
	num=0
	for i in range(3):
		for j in range(3):
			num+=1
			temp_squares.append(square(num,(j,i)))
	num=0
	for i in range(3):
		for j in range(3):
			num+=1
			info_squares.append(model_square(num,(j,i)))
	num=0
	for i in range(3):
		for j in range(3):
			num+=1
			squar.append(square(num,(j,i)))
	squar.pop(8)
	squares.pop(8)
	info_squares.pop(8)
	temp_squares.pop(8)
	shuffle(10000)
	moves=0
	gamePlay=True
	timer=0
	heuristic()
	start=time.time()
	while gamePlay:


		# gameDisplay.fill(blue)
		draw_background()
		board()
		info_board()
		check_solve()
		text = STAT_FONT.render("moves : "+str(moves),1, (255,255,255))
		gameDisplay.blit(text, (550,70))
		stop=time.time()
		
		if solved==False:
			timer_txt = STAT_FONT.render("time : "+str('%.1f'%(stop-start))+" sec",1, (255,255,255))
			timer=stop-start
			gameDisplay.blit(timer_txt, (20,70))
		else:
			timer_txt = STAT_FONT.render("time taken : "+str('%.1f'%(timer))+" sec",1, (255,255,255))
			gameDisplay.blit(timer_txt, (20,70))

		for sq in squares:
			sq.draw_square()

		for model in info_squares:
			model.draw_square()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gamePlay=False
			
			# if solved==False:
			# 	if event.type==pygame.KEYDOWN:

			# 		if event.key==pygame.K_w:
			# 			move_squares('u')
			# 			moves+=1
			# 		if event.key==pygame.K_s:
			# 			move_squares('d')
			# 			moves+=1
			# 		if event.key==pygame.K_d:
			# 			move_squares('r')
			# 			moves+=1
			# 		if event.key==pygame.K_a:
			# 			move_squares('l')
			# 			moves+=1

		

		pygame.display.update()





