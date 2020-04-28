import pygame
from copy import deepcopy
from network import Network

pygame.init()
menu=pygame.image.load("entrance.jpg")
globe=pygame.image.load("globe.png")
disp_width=900
disp_height=750
STAT_FONT = pygame.font.SysFont("comicsans",50)
stat_font = pygame.font.SysFont("comicsans",70)
stat_font2=pygame.font.SysFont("comicsans",100)
width_bet_sq=88
#global colors
white=(240,240,240)
black=(0,0,0)
blue=(0,0,255)
brown=(213,125,58)
red=(255,0,0)
gameDisplay=pygame.display.set_mode((disp_width,disp_height))
tile_black=pygame.image.load("background.jpg")
#pieces of white
b_bishop=pygame.image.load("blackBishop.png")
b_king=pygame.image.load("blackKing.png")
b_queen=pygame.image.load("blackQueen.png")
b_pawn=pygame.image.load("blackPawn.png")
b_rook=pygame.image.load("blackRook.png")
b_knight=pygame.image.load("blackKnight.png")

#pieces of black
w_bishop=pygame.image.load("whiteBishop.png")
w_king=pygame.image.load("whiteKing.png")
w_queen=pygame.image.load("whiteQueen.png")
w_pawn=pygame.image.load("whitePawn.png")
w_rook=pygame.image.load("whiteRook.png")
w_knight=pygame.image.load("whiteKnight.png")



back=pygame.image.load("back.jpeg")
frame=pygame.image.load("frame.png")

tile_white=pygame.image.load("tile.jpeg")




class board:

	def __init__(self):
		self.board_x=185
		self.board_y=23
		self.board_width=704
		self.board_height=704
		self.color=white
		

	def draw_board(self):
		back2=pygame.transform.scale(back,(900,750))
		gameDisplay.blit(back2,(0,0,900,750))


		frame2=pygame.transform.scale(frame,(self.board_height+110,self.board_width+70))
		gameDisplay.blit(frame2,(self.board_x-40,self.board_y-40,self.board_height+110,self.board_width+70))

		
		# pygame.draw.rect(gameDisplay,white,(self.board_x,self.board_y,self.board_height,self.board_width))
		self.draw_checks()
	def draw_checks(self):

		color_alternate=1
		
		# this is 700 pixel long 704/8=88 pixels for each square
		check_width=88
		check_height=88
		start_check_x=self.board_x
		start_check_y=self.board_y

		for vert in range(8):
			for hori in range(8):
				if color_alternate==1:
					check_color=white
				else:
					check_color=black
				inc_x=check_width*hori
				inc_y=check_height*vert
				if check_color==white:
					pygame.draw.rect(gameDisplay,check_color,(start_check_x+inc_x,start_check_y+inc_y,check_width,check_height))

				elif check_color==black:
					tile_black2=pygame.transform.scale(tile_black,(88,88))
					gameDisplay.blit(tile_black2,(start_check_x+inc_x,start_check_y+inc_y,check_width,check_height))

				
				color_alternate*=-1

			color_alternate*=-1




chess_board=[[-2,-3,-4,-5,-6,-4,-3,-2],
			 [-1,-1,-1,-1,-1,-1,-1,-1],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [1,1,1,1,1,1,1,1],
			 [2,3,4,5,6,4,3,2]]


def conv_to_arr(pos):
	return ((pos[0]-185)//88,(pos[1]-23)//88)

def conv_to_pixel(pos):
	return ((185+pos[0]*88),(23+pos[1]*88))

def draw_rect(x,y,w,h,t,col):
	col=col
	pygame.draw.line(gameDisplay,col,(x,y),(x+w,y),t)
	pygame.draw.line(gameDisplay,col,(x+w,y),(x+w,y+h),t)
	pygame.draw.line(gameDisplay,col,(x+w,y+h),(x,y+h),t)
	pygame.draw.line(gameDisplay,col,(x,y+h),(x,y),t)

def select_peice():
	global chess_board,current_pos,turns

	pos=pygame.mouse.get_pos()

	arr_pos=conv_to_arr(pos)
	
	pos=conv_to_pixel(arr_pos)
	# print(arr_pos)
	if arr_pos[0]>=0 and arr_pos[0]<8 and arr_pos[1]>=0 and arr_pos[1]<8:
		if turns==1:
			if pygame.mouse.get_pressed()[0] and (chess_board[arr_pos[1]][arr_pos[0]] >0):
				draw_rect(pos[0],pos[1],width_bet_sq,width_bet_sq,4,(246,169,27))
				current_pos=pos
		if turns==-1:
			if pygame.mouse.get_pressed()[0] and (chess_board[arr_pos[1]][arr_pos[0]] <0):
				draw_rect(pos[0],pos[1],width_bet_sq,width_bet_sq,4,(246,169,27))
				current_pos=pos

def mark_current_pos():
	global current_pos

	draw_rect(current_pos[0],current_pos[1],width_bet_sq,width_bet_sq,4,(0,0,255))

def draw_peices():
	global chess_board
	#actually internally the array id flipped by row and column rememebr to reflip the array while d
	for i in range(8):
		for j in range(8):
		
			check_pos=chess_board[i][j]
			

			if check_pos==1:
				pixel_pos=conv_to_pixel((j,i))
				w_pawn2=pygame.transform.scale(w_pawn,(88,88))
				gameDisplay.blit(w_pawn2,(pixel_pos[0],pixel_pos[1],88,88))
				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==2:
				pixel_pos=conv_to_pixel((j,i))
				w_rook2=pygame.transform.scale(w_rook,(88,88))
				gameDisplay.blit(w_rook2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==3:
				pixel_pos=conv_to_pixel((j,i))
				w_knight2=pygame.transform.scale(w_knight,(88,88))
				gameDisplay.blit(w_knight2,(pixel_pos[0],pixel_pos[1],88,88))
				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==4:
				pixel_pos=conv_to_pixel((j,i))
				w_bishop2=pygame.transform.scale(w_bishop,(88,88))
				gameDisplay.blit(w_bishop2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==5:
				pixel_pos=conv_to_pixel((j,i))
				w_queen2=pygame.transform.scale(w_queen,(88,88))
				gameDisplay.blit(w_queen2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==6:
				pixel_pos=conv_to_pixel((j,i))
				w_king2=pygame.transform.scale(w_king,(88,88))
				gameDisplay.blit(w_king2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			
			if check_pos==-1:
				pixel_pos=conv_to_pixel((j,i))
				b_pawn2=pygame.transform.scale(b_pawn,(88,88))
				gameDisplay.blit(b_pawn2,(pixel_pos[0],pixel_pos[1],88,88))
				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==-2:
				pixel_pos=conv_to_pixel((j,i))
				b_rook2=pygame.transform.scale(b_rook,(88,88))
				gameDisplay.blit(b_rook2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==-3:
				pixel_pos=conv_to_pixel((j,i))
				b_knight2=pygame.transform.scale(b_knight,(88,88))
				gameDisplay.blit(b_knight2,(pixel_pos[0],pixel_pos[1],88,88))
				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==-4:
				pixel_pos=conv_to_pixel((j,i))
				b_bishop2=pygame.transform.scale(b_bishop,(88,88))
				gameDisplay.blit(b_bishop2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==-5:
				pixel_pos=conv_to_pixel((j,i))
				b_queen2=pygame.transform.scale(b_queen,(88,88))
				gameDisplay.blit(b_queen2,(pixel_pos[0],pixel_pos[1],88,88))

				# pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==-6:
				pixel_pos=conv_to_pixel((j,i))
				b_king2=pygame.transform.scale(b_king,(88,88))
				gameDisplay.blit(b_king2,(pixel_pos[0],pixel_pos[1],88,88))


#showing moves
def pawn(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]
	try:
		if chess_board[pos[1]][pos[0]]>0:
			# print(pos)
			
			if pos[1]==6:
				if chess_board[pos[1]-1][pos[0]]==0:
					avble_slots.append((pos[1]-1,pos[0]))
					if chess_board[pos[1]-2][pos[0]]==0:
						avble_slots.append((pos[1]-2,pos[0]))
			if pos[0]-1>=0:
				if chess_board[pos[1]-1][pos[0]-1]<0:
					kill_slots.append((pos[1]-1,pos[0]-1))
			if pos[0]+1<=7:
				if chess_board[pos[1]-1][pos[0]+1]<0:
					kill_slots.append((pos[1]-1,pos[0]+1))



			if chess_board[pos[1]-1][pos[0]]==0:
				# print((pos[1]-1,pos[0]))
				avble_slots.append((pos[1]-1,pos[0]))

		if chess_board[pos[1]][pos[0]]<0:
			if pos[1]==1:
				if chess_board[pos[1]+1][pos[0]]==0:
					avble_slots.append((pos[1]+1,pos[0]))
					if chess_board[pos[1]+2][pos[0]]==0:
						avble_slots.append((pos[1]+2,pos[0]))
			if pos[0]+1<=7:
				if chess_board[pos[1]+1][pos[0]+1]>0:
					kill_slots.append((pos[1]+1,pos[0]+1))

			if pos[0]-1>=0:
				if chess_board[pos[1]+1][pos[0]-1]>0:
					kill_slots.append((pos[1]+1,pos[0]-1))



			if chess_board[pos[1]+1][pos[0]]==0:
				avble_slots.append((pos[1]+1,pos[0]))



	except:
		pass

	return avble_slots,kill_slots

def rook(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]

	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]][pos[0]-xl]<0:
				kill_slots.append((pos[1],pos[0]-xl))
				break
			if chess_board[pos[1]][pos[0]-xl]==0:
				avble_slots.append((pos[1],pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while pos[0]+xl<8:
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]][pos[0]+xl]<0:
				kill_slots.append((pos[1],pos[0]+xl))
				break
			if chess_board[pos[1]][pos[0]+xl]==0:
				avble_slots.append((pos[1],pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while pos[1]-yl>-1:
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]]<0:
				kill_slots.append((pos[1]-yl,pos[0]))
				break
			if chess_board[pos[1]-yl][pos[0]]==0:
				avble_slots.append((pos[1]-yl,pos[0]))
			else:
				break
			yl+=1
		
		yl=1
		while pos[1]+yl<8:
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]]<0:
				kill_slots.append((pos[1]+yl,pos[0]))
				break
			if chess_board[pos[1]+yl][pos[0]]==0:
				avble_slots.append((pos[1]+yl,pos[0]))
			else:
				break
			yl+=1
	else:
		xl=1
		while (pos[0]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]][pos[0]-xl]>0:
				kill_slots.append((pos[1],pos[0]-xl))
				break
			if chess_board[pos[1]][pos[0]-xl]==0:
				avble_slots.append((pos[1],pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while pos[0]+xl<8:
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]][pos[0]+xl]>0:
				kill_slots.append((pos[1],pos[0]+xl))
				break
			if chess_board[pos[1]][pos[0]+xl]==0:
				avble_slots.append((pos[1],pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while pos[1]-yl>-1:
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]]>0:
				kill_slots.append((pos[1]-yl,pos[0]))
				break
			if chess_board[pos[1]-yl][pos[0]]==0:
				avble_slots.append((pos[1]-yl,pos[0]))
			else:
				break
			yl+=1
		
		yl=1
		while pos[1]+yl<8:
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]]>0:
				kill_slots.append((pos[1]+yl,pos[0]))
				break
			if chess_board[pos[1]+yl][pos[0]]==0:
				avble_slots.append((pos[1]+yl,pos[0]))
			else:
				break
			yl+=1


	return avble_slots,kill_slots


def knight(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]
	#case 1 2 hori right 1 vert , up
	
	if chess_board[pos[1]][pos[0]]>0:
		if pos[1]+1<=7 and pos[0]+2<=7:
			if chess_board[pos[1]+1][pos[0]+2]==0:
				avble_slots.append((pos[1]+1,pos[0]+2))
			if chess_board[pos[1]+1][pos[0]+2]<0:
				kill_slots.append((pos[1]+1,pos[0]+2))

		#case 2 2hori right 1 vert down
		if pos[1]-1>=0 and pos[0]+2<=7:
			if chess_board[pos[1]-1][pos[0]+2]==0:
				avble_slots.append((pos[1]-1,pos[0]+2))
			if chess_board[pos[1]-1][pos[0]+2]<0:
				kill_slots.append((pos[1]-1,pos[0]+2))

		# case 3 2 hori left 1 vert up
		if pos[1]+1<=7 and pos[0]-2>=0:
			if chess_board[pos[1]+1][pos[0]-2]==0:
				avble_slots.append((pos[1]+1,pos[0]-2))
			if chess_board[pos[1]+1][pos[0]-2]<0:
				kill_slots.append((pos[1]+1,pos[0]-2))

		#case 4 2 hori left 1 vert down
		if pos[1]-1>=0 and pos[0]-2>=0:
			if chess_board[pos[1]-1][pos[0]-2]==0:
				avble_slots.append((pos[1]-1,pos[0]-2))
			if chess_board[pos[1]-1][pos[0]-2]<0:
				kill_slots.append((pos[1]-1,pos[0]-2))

		#case 5 2 vert up 1 hori right
		if pos[1]+2<=7 and pos[0]+1<=7:
			if chess_board[pos[1]+2][pos[0]+1]==0:
				avble_slots.append((pos[1]+2,pos[0]+1))
			if chess_board[pos[1]+2][pos[0]+1]<0:
				kill_slots.append((pos[1]+2,pos[0]+1))

		#case 6 2 vert up 1 hori left
		if pos[1]+2<=7 and pos[0]-1>=0:
			if chess_board[pos[1]+2][pos[0]-1]==0:
				avble_slots.append((pos[1]+2,pos[0]-1))
			if chess_board[pos[1]+2][pos[0]-1]<0:
				kill_slots.append((pos[1]+2,pos[0]-1))

		#case 7 2 vert down 1 hori right
		if pos[1]-2>=0 and pos[0]+1<=7:
			if chess_board[pos[1]-2][pos[0]+1]==0:
				avble_slots.append((pos[1]-2,pos[0]+1))
			if chess_board[pos[1]-2][pos[0]+1]<0:
				kill_slots.append((pos[1]-2,pos[0]+1))

		#case 8 2 vert down 1 hori left
		if pos[1]-2>=0 and pos[0]-1>=0:
			if chess_board[pos[1]-2][pos[0]-1]==0:
				avble_slots.append((pos[1]-2,pos[0]-1))
			if chess_board[pos[1]-2][pos[0]-1]<0:
				kill_slots.append((pos[1]-2,pos[0]-1))
	else:
		if pos[1]+1<=7 and pos[0]+2<=7:
			if chess_board[pos[1]+1][pos[0]+2]==0:
				avble_slots.append((pos[1]+1,pos[0]+2))
			if chess_board[pos[1]+1][pos[0]+2]>0:
				kill_slots.append((pos[1]+1,pos[0]+2))

		#case 2 2hori right 1 vert down
		if pos[1]-1>=0 and pos[0]+2<=7:
			if chess_board[pos[1]-1][pos[0]+2]==0:
				avble_slots.append((pos[1]-1,pos[0]+2))
			if chess_board[pos[1]-1][pos[0]+2]>0:
				kill_slots.append((pos[1]-1,pos[0]+2))

		# case 3 2 hori left 1 vert up
		if pos[1]+1<=7 and pos[0]-2>=0:
			if chess_board[pos[1]+1][pos[0]-2]==0:
				avble_slots.append((pos[1]+1,pos[0]-2))
			if chess_board[pos[1]+1][pos[0]-2]>0:
				kill_slots.append((pos[1]+1,pos[0]-2))

		#case 4 2 hori left 1 vert down
		if pos[1]-1>=0 and pos[0]-2>=0:
			if chess_board[pos[1]-1][pos[0]-2]==0:
				avble_slots.append((pos[1]-1,pos[0]-2))
			if chess_board[pos[1]-1][pos[0]-2]>0:
				kill_slots.append((pos[1]-1,pos[0]-2))

		#case 5 2 vert up 1 hori right
		if pos[1]+2<=7 and pos[0]+1<=7:
			if chess_board[pos[1]+2][pos[0]+1]==0:
				avble_slots.append((pos[1]+2,pos[0]+1))
			if chess_board[pos[1]+2][pos[0]+1]>0:
				kill_slots.append((pos[1]+2,pos[0]+1))

		#case 6 2 vert up 1 hori left
		if pos[1]+2<=7 and pos[0]-1>=0:
			if chess_board[pos[1]+2][pos[0]-1]==0:
				avble_slots.append((pos[1]+2,pos[0]-1))
			if chess_board[pos[1]+2][pos[0]-1]>0:
				kill_slots.append((pos[1]+2,pos[0]-1))

		#case 7 2 vert down 1 hori right
		if pos[1]-2>=0 and pos[0]+1<=7:
			if chess_board[pos[1]-2][pos[0]+1]==0:
				avble_slots.append((pos[1]-2,pos[0]+1))
			if chess_board[pos[1]-2][pos[0]+1]>0:
				kill_slots.append((pos[1]-2,pos[0]+1))

		#case 8 2 vert down 1 hori left
		if pos[1]-2>=0 and pos[0]-1>=0:
			if chess_board[pos[1]-2][pos[0]-1]==0:
				avble_slots.append((pos[1]-2,pos[0]-1))
			if chess_board[pos[1]-2][pos[0]-1]>0:
				kill_slots.append((pos[1]-2,pos[0]-1))

	
	return avble_slots,kill_slots


def bishop(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]

	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]-xl][pos[0]-xl]<0:
				kill_slots.append((pos[1]-xl,pos[0]-xl))
				break
			if chess_board[pos[1]-xl][pos[0]-xl]==0:
				avble_slots.append((pos[1]-xl,pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while (pos[0]+xl<8) and (pos[1]+xl<8):
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]+xl][pos[0]+xl]<0:
				kill_slots.append((pos[1]+xl,pos[0]+xl))
				break
			if chess_board[pos[1]+xl][pos[0]+xl]==0:
				avble_slots.append((pos[1]+xl,pos[0]+xl))
			else:
				break
			xl+=1
		xl=1

		yl=1
		while (pos[1]-yl>-1) and (pos[0]+yl<8):
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]+yl]<0:
				kill_slots.append((pos[1]-yl,pos[0]+yl))
				break
			if chess_board[pos[1]-yl][pos[0]+yl]==0:
				avble_slots.append((pos[1]-yl,pos[0]+yl))
			else:
				break
			yl+=1
		
		yl=1
		while (pos[1]+yl<8) and (pos[0]-yl>-1):
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]-yl]<0:
				kill_slots.append((pos[1]+yl,pos[0]-yl))
				break
			if chess_board[pos[1]+yl][pos[0]-yl]==0:
				avble_slots.append((pos[1]+yl,pos[0]-yl))
			else:
				break
			yl+=1
	else:
		xl=1
		while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]-xl][pos[0]-xl]>0:
				kill_slots.append((pos[1]-xl,pos[0]-xl))
				break
			if chess_board[pos[1]-xl][pos[0]-xl]==0:
				avble_slots.append((pos[1]-xl,pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while (pos[0]+xl<8) and (pos[1]+xl<8):
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]+xl][pos[0]+xl]>0:
				kill_slots.append((pos[1]+xl,pos[0]+xl))
				break
			if chess_board[pos[1]+xl][pos[0]+xl]==0:
				avble_slots.append((pos[1]+xl,pos[0]+xl))
			else:
				break
			xl+=1
		xl=1

		yl=1
		while (pos[1]-yl>-1) and (pos[0]+yl<8):
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]+yl]>0:
				kill_slots.append((pos[1]-yl,pos[0]+yl))
				break
			if chess_board[pos[1]-yl][pos[0]+yl]==0:
				avble_slots.append((pos[1]-yl,pos[0]+yl))
			else:
				break
			yl+=1
		
		yl=1
		while (pos[1]+yl<8) and (pos[0]-yl>-1):
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]-yl]>0:
				kill_slots.append((pos[1]+yl,pos[0]-yl))
				break
			if chess_board[pos[1]+yl][pos[0]-yl]==0:
				avble_slots.append((pos[1]+yl,pos[0]-yl))
			else:
				break
			yl+=1

	return avble_slots,kill_slots


def queen(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]

	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]][pos[0]-xl]<0:
				kill_slots.append((pos[1],pos[0]-xl))
				break
			if chess_board[pos[1]][pos[0]-xl]==0:
				avble_slots.append((pos[1],pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while pos[0]+xl<8:
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]][pos[0]+xl]<0:
				kill_slots.append((pos[1],pos[0]+xl))
				break
			if chess_board[pos[1]][pos[0]+xl]==0:
				avble_slots.append((pos[1],pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while pos[1]-yl>-1:
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]]<0:
				kill_slots.append((pos[1]-yl,pos[0]))
				break
			if chess_board[pos[1]-yl][pos[0]]==0:
				avble_slots.append((pos[1]-yl,pos[0]))
			else:
				break
			yl+=1
		
		yl=1
		while pos[1]+yl<8:
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]]<0:
				kill_slots.append((pos[1]+yl,pos[0]))
				break
			if chess_board[pos[1]+yl][pos[0]]==0:
				avble_slots.append((pos[1]+yl,pos[0]))
			else:
				break
			yl+=1
	else:
		xl=1
		while (pos[0]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]][pos[0]-xl]>0:
				kill_slots.append((pos[1],pos[0]-xl))
				break
			if chess_board[pos[1]][pos[0]-xl]==0:
				avble_slots.append((pos[1],pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while pos[0]+xl<8:
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]][pos[0]+xl]>0:
				kill_slots.append((pos[1],pos[0]+xl))
				break
			if chess_board[pos[1]][pos[0]+xl]==0:
				avble_slots.append((pos[1],pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while pos[1]-yl>-1:
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]]>0:
				kill_slots.append((pos[1]-yl,pos[0]))
				break
			if chess_board[pos[1]-yl][pos[0]]==0:
				avble_slots.append((pos[1]-yl,pos[0]))
			else:
				break
			yl+=1
		
		yl=1
		while pos[1]+yl<8:
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]]>0:
				kill_slots.append((pos[1]+yl,pos[0]))
				break
			if chess_board[pos[1]+yl][pos[0]]==0:
				avble_slots.append((pos[1]+yl,pos[0]))
			else:
				break
			yl+=1
	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]-xl][pos[0]-xl]<0:
				kill_slots.append((pos[1]-xl,pos[0]-xl))
				break
			if chess_board[pos[1]-xl][pos[0]-xl]==0:
				avble_slots.append((pos[1]-xl,pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while (pos[0]+xl<8) and (pos[1]+xl<8):
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]+xl][pos[0]+xl]<0:
				kill_slots.append((pos[1]+xl,pos[0]+xl))
				break
			if chess_board[pos[1]+xl][pos[0]+xl]==0:
				avble_slots.append((pos[1]+xl,pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while (pos[1]-yl>-1) and (pos[0]+yl<8):
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]+yl]<0:
				kill_slots.append((pos[1]-yl,pos[0]+yl))
				break
			if chess_board[pos[1]-yl][pos[0]+yl]==0:
				avble_slots.append((pos[1]-yl,pos[0]+yl))
			else:
				break
			yl+=1
		
		yl=1
		while (pos[1]+yl<8) and (pos[0]-yl>-1):
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]-yl]<0:
				kill_slots.append((pos[1]+yl,pos[0]-yl))
				break
			if chess_board[pos[1]+yl][pos[0]-yl]==0:
				avble_slots.append((pos[1]+yl,pos[0]-yl))
			else:
				break
			yl+=1
	else:
		xl=1
		while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]-xl][pos[0]-xl]>0:
				kill_slots.append((pos[1]-xl,pos[0]-xl))
				break
			if chess_board[pos[1]-xl][pos[0]-xl]==0:
				avble_slots.append((pos[1]-xl,pos[0]-xl))
			else:
				break
			xl+=1
		
		xl=1
		while (pos[0]+xl<8) and (pos[1]+xl<8):
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]+xl][pos[0]+xl]>0:
				kill_slots.append((pos[1]+xl,pos[0]+xl))
				break
			if chess_board[pos[1]+xl][pos[0]+xl]==0:
				avble_slots.append((pos[1]+xl,pos[0]+xl))
			else:
				break
			xl+=1

		yl=1
		while (pos[1]-yl>-1) and (pos[0]+yl<8):
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]+yl]>0:
				kill_slots.append((pos[1]-yl,pos[0]+yl))
				break
			if chess_board[pos[1]-yl][pos[0]+yl]==0:
				avble_slots.append((pos[1]-yl,pos[0]+yl))
			else:
				break
			yl+=1
		
		yl=1
		while (pos[1]+yl<8) and (pos[0]-yl>-1):
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]-yl]>0:
				kill_slots.append((pos[1]+yl,pos[0]-yl))
				break
			if chess_board[pos[1]+yl][pos[0]-yl]==0:
				avble_slots.append((pos[1]+yl,pos[0]-yl))
			else:
				break
			yl+=1

	return avble_slots,kill_slots

def king(use_curr_pos,p):
	global current_pos,chess_board
	if use_curr_pos==True:
		pos=conv_to_arr(current_pos)
	else:
		pos=p
	# print(pos)
	avble_slots=[]
	kill_slots=[]
	if chess_board[pos[1]][pos[0]]>0:
		if pos[1]-1>=0:
			if chess_board[pos[1]-1][pos[0]]<0:
				kill_slots.append((pos[1]-1,pos[0]))
					
			if chess_board[pos[1]-1][pos[0]]==0:
				avble_slots.append((pos[1]-1,pos[0]))

		if pos[1]+1<8:
			if chess_board[pos[1]+1][pos[0]]<0:
				kill_slots.append((pos[1]+1,pos[0]))
					
			if chess_board[pos[1]+1][pos[0]]==0:
				avble_slots.append((pos[1]+1,pos[0]))

		if pos[0]-1>=0:
			if chess_board[pos[1]][pos[0]-1]<0:
				kill_slots.append((pos[1],pos[0]-1))
					
			if chess_board[pos[1]][pos[0]-1]==0:
				avble_slots.append((pos[1],pos[0]-1))

		if pos[0]+1<8:
			if chess_board[pos[1]][pos[0]+1]<0:
				kill_slots.append((pos[1],pos[0]+1))
					
			if chess_board[pos[1]][pos[0]+1]==0:
				avble_slots.append((pos[1],pos[0]+1))

		if pos[1]-1>=0 and pos[0]-1>=0:
			if chess_board[pos[1]-1][pos[0]-1]<0:
				kill_slots.append((pos[1]-1,pos[0]-1))
					
			if chess_board[pos[1]-1][pos[0]-1]==0:
				avble_slots.append((pos[1]-1,pos[0]-1))

		if pos[1]-1>=0 and pos[0]+1<8:
			if chess_board[pos[1]-1][pos[0]+1]<0:
				kill_slots.append((pos[1]-1,pos[0]+1))
					
			if chess_board[pos[1]-1][pos[0]+1]==0:
				avble_slots.append((pos[1]-1,pos[0]+1))

		if pos[1]+1<8 and pos[1]-1>=0:
			if chess_board[pos[1]+1][pos[0]-1]<0:
				kill_slots.append((pos[1]+1,pos[0]-1))
					
			if chess_board[pos[1]+1][pos[0]-1]==0:
				avble_slots.append((pos[1]+1,pos[0]-1))

		if pos[1]+1<8 and pos[0]+1>=0:
			if chess_board[pos[1]+1][pos[0]+1]<0:
				kill_slots.append((pos[1]+1,pos[0]+1))
					
			if chess_board[pos[1]+1][pos[0]+1]==0:
				avble_slots.append((pos[1]+1,pos[0]+1))
	else:
		if pos[1]-1>=0:
			if chess_board[pos[1]-1][pos[0]]>0:
				kill_slots.append((pos[1]-1,pos[0]))
					
			if chess_board[pos[1]-1][pos[0]]==0:
				avble_slots.append((pos[1]-1,pos[0]))

		if pos[1]+1<8:
			if chess_board[pos[1]+1][pos[0]]>0:
				kill_slots.append((pos[1]+1,pos[0]))
					
			if chess_board[pos[1]+1][pos[0]]==0:
				avble_slots.append((pos[1]+1,pos[0]))

		if pos[0]-1>=0:
			if chess_board[pos[1]][pos[0]-1]>0:
				kill_slots.append((pos[1],pos[0]-1))
					
			if chess_board[pos[1]][pos[0]-1]==0:
				avble_slots.append((pos[1],pos[0]-1))

		if pos[0]+1<8:
			if chess_board[pos[1]][pos[0]+1]>0:
				kill_slots.append((pos[1],pos[0]+1))
					
			if chess_board[pos[1]][pos[0]+1]==0:
				avble_slots.append((pos[1],pos[0]+1))

		if pos[1]-1>=0 and pos[0]-1>=0:
			if chess_board[pos[1]-1][pos[0]-1]>0:
				kill_slots.append((pos[1]-1,pos[0]-1))
					
			if chess_board[pos[1]-1][pos[0]-1]==0:
				avble_slots.append((pos[1]-1,pos[0]-1))

		if pos[1]-1>=0 and pos[0]+1<8:
			if chess_board[pos[1]-1][pos[0]+1]>0:
				kill_slots.append((pos[1]-1,pos[0]+1))
					
			if chess_board[pos[1]-1][pos[0]+1]==0:
				avble_slots.append((pos[1]-1,pos[0]+1))

		if pos[1]+1<8 and pos[0]-1>=0:
			if chess_board[pos[1]+1][pos[0]-1]>0:
				kill_slots.append((pos[1]+1,pos[0]-1))
					
			if chess_board[pos[1]+1][pos[0]-1]==0:
				avble_slots.append((pos[1]+1,pos[0]-1))

		if pos[1]+1<8 and pos[0]+1<8:
			
			if chess_board[pos[1]+1][pos[0]+1]>0:

				kill_slots.append((pos[1]+1,pos[0]+1))
					
			if chess_board[pos[1]+1][pos[0]+1]==0:
				avble_slots.append((pos[1]+1,pos[0]+1))

	return avble_slots,kill_slots





def determine_check_1():
	global current_pos,chess_board
	
	# print(pos)
	for i in range(8):
		for j in range(8):
			if chess_board[i][j]==6:
				pos=(j,i)

	avble_slots=[]
	kill_slots=[]

	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]][pos[0]-xl]<0:
				kill_slots.append((pos[1],pos[0]-xl))
				break
			if chess_board[pos[1]][pos[0]-xl]==0:
				avble_slots.append((pos[1],pos[0]-xl))
			else:
				break
			
			xl+=1
		
		xl=1
		while pos[0]+xl<8:
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]][pos[0]+xl]<0:
				kill_slots.append((pos[1],pos[0]+xl))
				break
			if chess_board[pos[1]][pos[0]+xl]==0:
				avble_slots.append((pos[1],pos[0]+xl))
			else:
				break
			
			xl+=1

		yl=1
		while pos[1]-yl>-1:
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]]<0:
				kill_slots.append((pos[1]-yl,pos[0]))
				break
			if chess_board[pos[1]-yl][pos[0]]==0:
				avble_slots.append((pos[1]-yl,pos[0]))
			else:
				break
			
			yl+=1
		
		yl=1
		while pos[1]+yl<8:
			# print(pos[0]+yl)
			
			
			
			if chess_board[pos[1]+yl][pos[0]]<0:
				kill_slots.append((pos[1]+yl,pos[0]))
				break
			if chess_board[pos[1]+yl][pos[0]]==0:
				avble_slots.append((pos[1]+yl,pos[0]))
			else:
				break
			
			yl+=1
	
	if chess_board[pos[1]][pos[0]]>0:
		xl=1
		while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
			# print(pos[0]-xl)
			
			
			if chess_board[pos[1]-xl][pos[0]-xl]<0:
				kill_slots.append((pos[1]-xl,pos[0]-xl))
				break
			if chess_board[pos[1]-xl][pos[0]-xl]==0:
				avble_slots.append((pos[1]-xl,pos[0]-xl))
			else:
				break
			
			xl+=1
		
		xl=1
		while (pos[0]+xl<8) and (pos[1]+xl<8):
			# print(pos[0]+xl)
			
			
			if chess_board[pos[1]+xl][pos[0]+xl]<0:
				kill_slots.append((pos[1]+xl,pos[0]+xl))
				break
			if chess_board[pos[1]+xl][pos[0]+xl]==0:
				avble_slots.append((pos[1]+xl,pos[0]+xl))
			else:
				break
			
			xl+=1

		yl=1
		while (pos[1]-yl>-1) and (pos[0]+yl<8):
			# print(pos[0]-yl)
			
			
			if chess_board[pos[1]-yl][pos[0]+yl]<0:
				kill_slots.append((pos[1]-yl,pos[0]+yl))
				break
			if chess_board[pos[1]-yl][pos[0]+yl]==0:
				avble_slots.append((pos[1]-yl,pos[0]+yl))
			else:
				break
			
			yl+=1
		
		yl=1
		while (pos[1]+yl<8) and (pos[0]-yl>-1):
			# print(pos[0]+yl)
			
			# print("hoooo")
			
			if chess_board[pos[1]+yl][pos[0]-yl]<0:
				kill_slots.append((pos[1]+yl,pos[0]-yl))
				break
			if chess_board[pos[1]+yl][pos[0]-yl]==0:
				avble_slots.append((pos[1]+yl,pos[0]-yl))
			else:
				break
			
			yl+=1
	#case 1 2 hori right 1 vert , up
	
	if chess_board[pos[1]][pos[0]]>0:
		if pos[1]+1<=7 and pos[0]+2<=7:
			if chess_board[pos[1]+1][pos[0]+2]==0:
				avble_slots.append((pos[1]+1,pos[0]+2))
			if chess_board[pos[1]+1][pos[0]+2]<0:
				kill_slots.append((pos[1]+1,pos[0]+2))

		#case 2 2hori right 1 vert down
		if pos[1]-1>=0 and pos[0]+2<=7:
			if chess_board[pos[1]-1][pos[0]+2]==0:
				avble_slots.append((pos[1]-1,pos[0]+2))
			if chess_board[pos[1]-1][pos[0]+2]<0:
				kill_slots.append((pos[1]-1,pos[0]+2))

		# case 3 2 hori left 1 vert up
		if pos[1]+1<=7 and pos[0]-2>=0:
			if chess_board[pos[1]+1][pos[0]-2]==0:
				avble_slots.append((pos[1]+1,pos[0]-2))
			if chess_board[pos[1]+1][pos[0]-2]<0:
				kill_slots.append((pos[1]+1,pos[0]-2))

		#case 4 2 hori left 1 vert down
		if pos[1]-1>=0 and pos[0]-2>=0:
			if chess_board[pos[1]-1][pos[0]-2]==0:
				avble_slots.append((pos[1]-1,pos[0]-2))
			if chess_board[pos[1]-1][pos[0]-2]<0:
				kill_slots.append((pos[1]-1,pos[0]-2))

		#case 5 2 vert up 1 hori right
		if pos[1]+2<=7 and pos[0]+1<=7:
			if chess_board[pos[1]+2][pos[0]+1]==0:
				avble_slots.append((pos[1]+2,pos[0]+1))
			if chess_board[pos[1]+2][pos[0]+1]<0:
				kill_slots.append((pos[1]+2,pos[0]+1))

		#case 6 2 vert up 1 hori left
		if pos[1]+2<=7 and pos[0]-1>=0:
			if chess_board[pos[1]+2][pos[0]-1]==0:
				avble_slots.append((pos[1]+2,pos[0]-1))
			if chess_board[pos[1]+2][pos[0]-1]<0:
				kill_slots.append((pos[1]+2,pos[0]-1))

		#case 7 2 vert down 1 hori right
		if pos[1]-2>=0 and pos[0]+1<=7:
			if chess_board[pos[1]-2][pos[0]+1]==0:
				avble_slots.append((pos[1]-2,pos[0]+1))
			if chess_board[pos[1]-2][pos[0]+1]<0:
				kill_slots.append((pos[1]-2,pos[0]+1))

		#case 8 2 vert down 1 hori left
		if pos[1]-2>=0 and pos[0]-1>=0:
			if chess_board[pos[1]-2][pos[0]-1]==0:
				avble_slots.append((pos[1]-2,pos[0]-1))
			if chess_board[pos[1]-2][pos[0]-1]<0:
				kill_slots.append((pos[1]-2,pos[0]-1))
	

	check=False
	check_available_slot=[]
	check_kill_slot=[]
	# print(kill_slots)
	for pieces in kill_slots:

		if chess_board[pieces[0]][pieces[1]]==-1:
			check_kill_slot+=pawn(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==-2:

			check_kill_slot+=rook(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==-3:
			check_kill_slot+=knight(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==-4:

			check_kill_slot+=bishop(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==-5:
			# print("hooo)")
			check_kill_slot+=queen(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==-6:
			check_kill_slot+=king(False,(pieces[1],pieces[0]))[1]



	# print(check_kill_slot)
	# print(pos)
	for kill in check_kill_slot:
		if kill==(pos[1],pos[0]):
			check=True

	return check

def determine_check_2():
	global current_pos,chess_board
	
	# print(pos)
	for i in range(8):
		for j in range(8):
			if chess_board[i][j]==-6:
				pos=(j,i)
	avble_slots=[]
	kill_slots=[]


	xl=1

	while (pos[0]-xl)>-1:
		# print(pos[0]-xl)
		
		
		if chess_board[pos[1]][pos[0]-xl]>0:

			kill_slots.append((pos[1],pos[0]-xl))
			break
		if chess_board[pos[1]][pos[0]-xl]==0:
			avble_slots.append((pos[1],pos[0]-xl))
		else:
			break
	
		xl+=1
	
	xl=1
	while pos[0]+xl<8:
		# print(pos[0]+xl)
		
		
		if chess_board[pos[1]][pos[0]+xl]>0:

			kill_slots.append((pos[1],pos[0]+xl))
			break
		if chess_board[pos[1]][pos[0]+xl]==0:
			avble_slots.append((pos[1],pos[0]+xl))
		else:
			break
		
		xl+=1

	yl=1
	while pos[1]-yl>-1:
		# print(pos[0]-yl)

		
		if chess_board[pos[1]-yl][pos[0]]>0:

			kill_slots.append((pos[1]-yl,pos[0]))
			break
		if chess_board[pos[1]-yl][pos[0]]==0:
			avble_slots.append((pos[1]-yl,pos[0]))
		else:
			break
	
		yl+=1
	
	yl=1
	while pos[1]+yl<8:
		# print(pos[0]+yl)
		
		
		
		if chess_board[pos[1]+yl][pos[0]]>0:
			# print("bbbbbbbbbbbbbad")

			kill_slots.append((pos[1]+yl,pos[0]))
			break

		if chess_board[pos[1]+yl][pos[0]]==0:
			avble_slots.append((pos[1]+yl,pos[0]))
		else:
			break
		
		yl+=1
	xl=1
	while (pos[0]-xl)>-1 and (pos[1]-xl)>-1:
		# print(pos[0]-xl)
		
	
		if chess_board[pos[1]-xl][pos[0]-xl]>0:
			kill_slots.append((pos[1]-xl,pos[0]-xl))
			break
		if chess_board[pos[1]-xl][pos[0]-xl]==0:
			avble_slots.append((pos[1]-xl,pos[0]-xl))
		else:
			break
		
		xl+=1
	
	xl=1
	while (pos[0]+xl<8) and (pos[1]+xl<8):
		# print(pos[0]+xl)
		
		
		if chess_board[pos[1]+xl][pos[0]+xl]>0:
			kill_slots.append((pos[1]+xl,pos[0]+xl))
			break
		if chess_board[pos[1]+xl][pos[0]+xl]==0:
			avble_slots.append((pos[1]+xl,pos[0]+xl))
		else:
			break
		
		xl+=1

	yl=1
	while (pos[1]-yl>-1) and (pos[0]+yl<8):
		# print(pos[0]-yl)
		
		
		if chess_board[pos[1]-yl][pos[0]+yl]>0:
			kill_slots.append((pos[1]-yl,pos[0]+yl))
			break
		if chess_board[pos[1]-yl][pos[0]+yl]==0:
			avble_slots.append((pos[1]-yl,pos[0]+yl))
		else:
			break
		
		yl+=1
	
	yl=1
	while (pos[1]+yl<8) and (pos[0]-yl>-1):
		# print(pos[0]+yl)
		
		
		
		if chess_board[pos[1]+yl][pos[0]-yl]>0:
			kill_slots.append((pos[1]+yl,pos[0]-yl))
			break
		if chess_board[pos[1]+yl][pos[0]-yl]==0:
			avble_slots.append((pos[1]+yl,pos[0]-yl))
		else:
			break

		
		yl+=1
	if pos[1]+1<=7 and pos[0]+2<=7:
			if chess_board[pos[1]+1][pos[0]+2]==0:
				avble_slots.append((pos[1]+1,pos[0]+2))
			if chess_board[pos[1]+1][pos[0]+2]>0:
				kill_slots.append((pos[1]+1,pos[0]+2))

	#case 2 2hori right 1 vert down
	if pos[1]-1>=0 and pos[0]+2<=7:
		if chess_board[pos[1]-1][pos[0]+2]==0:
			avble_slots.append((pos[1]-1,pos[0]+2))
		if chess_board[pos[1]-1][pos[0]+2]>0:
			kill_slots.append((pos[1]-1,pos[0]+2))

	# case 3 2 hori left 1 vert up
	if pos[1]+1<=7 and pos[0]-2>=0:
		if chess_board[pos[1]+1][pos[0]-2]==0:
			avble_slots.append((pos[1]+1,pos[0]-2))
		if chess_board[pos[1]+1][pos[0]-2]>0:
			kill_slots.append((pos[1]+1,pos[0]-2))

	#case 4 2 hori left 1 vert down
	if pos[1]-1>=0 and pos[0]-2>=0:
		if chess_board[pos[1]-1][pos[0]-2]==0:
			avble_slots.append((pos[1]-1,pos[0]-2))
		if chess_board[pos[1]-1][pos[0]-2]>0:
			kill_slots.append((pos[1]-1,pos[0]-2))

	#case 5 2 vert up 1 hori right
	if pos[1]+2<=7 and pos[0]+1<=7:
		if chess_board[pos[1]+2][pos[0]+1]==0:
			avble_slots.append((pos[1]+2,pos[0]+1))
		if chess_board[pos[1]+2][pos[0]+1]>0:
			kill_slots.append((pos[1]+2,pos[0]+1))

	#case 6 2 vert up 1 hori left
	if pos[1]+2<=7 and pos[0]-1>=0:
		if chess_board[pos[1]+2][pos[0]-1]==0:
			avble_slots.append((pos[1]+2,pos[0]-1))
		if chess_board[pos[1]+2][pos[0]-1]>0:
			kill_slots.append((pos[1]+2,pos[0]-1))

	#case 7 2 vert down 1 hori right
	if pos[1]-2>=0 and pos[0]+1<=7:
		if chess_board[pos[1]-2][pos[0]+1]==0:
			avble_slots.append((pos[1]-2,pos[0]+1))
		if chess_board[pos[1]-2][pos[0]+1]>0:
			kill_slots.append((pos[1]-2,pos[0]+1))

	#case 8 2 vert down 1 hori left
	if pos[1]-2>=0 and pos[0]-1>=0:
		if chess_board[pos[1]-2][pos[0]-1]==0:
			avble_slots.append((pos[1]-2,pos[0]-1))
		if chess_board[pos[1]-2][pos[0]-1]>0:
			kill_slots.append((pos[1]-2,pos[0]-1))

	check=False
	check_available_slot=[]
	check_kill_slot=[]
	# print(kill_slots)
	for pieces in kill_slots:

		if chess_board[pieces[0]][pieces[1]]==1:
			check_kill_slot+=pawn(False,(pieces[1],pieces[0]))[1]


		if chess_board[pieces[0]][pieces[1]]==2:

			check_kill_slot+=rook(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==3:
			check_kill_slot+=knight(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==4:
			check_kill_slot+=bishop(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==5:

			check_kill_slot+=queen(False,(pieces[1],pieces[0]))[1]

		if chess_board[pieces[0]][pieces[1]]==6:
			check_kill_slot+=king(False,(pieces[1],pieces[0]))[1]



	# print(check_kill_slot)
	for kill in check_kill_slot:
		if kill==(pos[1],pos[0]):
			check=True

	return check

def check_for_checkmates_2():
	global chess_board
	checking_pieces=[]
	checkmate=True
	for i in range(8):
		for j in range(8):
			if chess_board[i][j]<0:
				checking_pieces.append((j,i))

	temp_arr=deepcopy(chess_board)
	# print(turns)
	for pos in checking_pieces:

		if chess_board[pos[1]][pos[0]]==-1:
			available_slot,kill_slot=pawn(False,pos)

		if chess_board[pos[1]][pos[0]]==-2:
			available_slot,kill_slot=rook(False,pos)

		if chess_board[pos[1]][pos[0]]==-3:
			available_slot,kill_slot=knight(False,pos)

		if chess_board[pos[1]][pos[0]]==-4:
			available_slot,kill_slot=bishop(False,pos)

		if chess_board[pos[1]][pos[0]]==-5:
			available_slot,kill_slot=queen(False,pos)

		if chess_board[pos[1]][pos[0]]==-6:
			available_slot,kill_slot=king(False,pos)

		for slot in available_slot:
			king_found=False
			chess_board=deepcopy(temp_arr)

			move_iterator(pos,slot)
			for i in range(8):
				for j in range(8):
					if chess_board[i][j]==-6:
						king_found=True
			if king_found==False:
				chess_board=deepcopy(temp_arr)
			# for i in range(8):
			# 	print(chess_board[i])
			
			if determine_check_2()==False:
				checkmate=False
				break
		if determine_check_2()==False:
			break
			
			
		for slot in kill_slot:
			king_found=False
			chess_board=deepcopy(temp_arr)
			move_iterator(pos,slot)
			# for i in range(8):
			# 	print(chess_board[i])
			# print(slot)
			for i in range(8):
				for j in range(8):
					if chess_board[i][j]==-6:
						king_found=True
			if king_found==False:
				chess_board=deepcopy(temp_arr)
			if determine_check_2()==False:

				checkmate=False
				break
		if determine_check_2()==False:
			break
			
			
	chess_board=temp_arr
	return checkmate


def check_for_checkmates_1():
	global chess_board
	checking_pieces=[]
	checkmate=True
	for i in range(8):
		for j in range(8):
			if chess_board[i][j]>0:
				checking_pieces.append((j,i))
	# print(chess_board)
	temp_arr=deepcopy(chess_board)
	# print(turns)
	for pos in checking_pieces:

		if chess_board[pos[1]][pos[0]]==1:
			available_slot,kill_slot=pawn(False,pos)

		if chess_board[pos[1]][pos[0]]==2:
			available_slot,kill_slot=rook(False,pos)

		if chess_board[pos[1]][pos[0]]==3:
			available_slot,kill_slot=knight(False,pos)

		if chess_board[pos[1]][pos[0]]==4:
			available_slot,kill_slot=bishop(False,pos)

		if chess_board[pos[1]][pos[0]]==5:
			available_slot,kill_slot=queen(False,pos)

		if chess_board[pos[1]][pos[0]]==6:
			available_slot,kill_slot=king(False,pos)

		for slot in available_slot:
			king_found=False
			move_iterator(pos,slot)
			for i in range(8):
				for j in range(8):
					if chess_board[i][j]==6:
						king_found=True
			if king_found==False:
				chess_board=deepcopy(temp_arr)
			if determine_check_1()==False:
				checkmate=False
				break
			
			chess_board=temp_arr
		for slot in kill_slot:
			king_found=False
			move_iterator(pos,slot)
			# for i in range(8):
				# print(chess_board[i])
			# print(slot)
			for i in range(8):
				for j in range(8):
					if chess_board[i][j]==6:
						king_found=True
			if king_found==False:
				chess_board=deepcopy(temp_arr)
			if determine_check_1()==False:
				checkmate=False
				break
			
			chess_board=temp_arr
	chess_board=temp_arr

	return checkmate



def move_iterator(pos,slot):
	global chess_board
	#worked fine at 0 1 trying 1 0 to fix bugs
	chess_board[slot[0]][slot[1]]=chess_board[pos[1]][pos[0]]
	chess_board[pos[1]][pos[0]]=0














def move_peice(avble_slots,kill_slots):
	global current_pos,chess_board,killed_pieces,turns
	global posit,cur_pos
	pos=pygame.mouse.get_pos()
	pos=conv_to_arr(pos)
	cur_pos_conv=conv_to_arr(current_pos)
	selected_slot=(-1,-1)
	# print("================")
	# print(pos)
	
	# print(cur_pos_conv)
	# print(avble_slots)
	# print("+++++++++++++++++++")
	# for i in range(8):
	# 	print(chess_board[i])
	
	
	if pygame.mouse.get_pressed()[0]:
		
		

		for slot in avble_slots:
			if (pos[1],pos[0])==slot:
				selected_slot=pos
				posit=pos
				cur_pos=cur_pos_conv
				chess_board[pos[1]][pos[0]]=chess_board[cur_pos_conv[1]][cur_pos_conv[0]]
				chess_board[cur_pos_conv[1]][cur_pos_conv[0]]=0
				turns*=-1
				break

		for slot in kill_slots:
			if (pos[1],pos[0])==slot:
				selected_slot=pos
				posit=pos
				cur_pos=cur_pos_conv
				killed_pieces.append(chess_board[pos[1]][pos[0]])
				chess_board[pos[1]][pos[0]]=chess_board[cur_pos_conv[1]][cur_pos_conv[0]]
				chess_board[cur_pos_conv[1]][cur_pos_conv[0]]=0
				turns*=-1
				break

	return selected_slot









def show_possible_moves():
	global current_pos,chess_board,turns,check2,check1,checked_pos,update_check_pos
	pos=conv_to_arr(current_pos)
	available_slot=[]
	kill_slot=[]
	
	# 1 stands for white turn and -1 stands for blacks turn
	


	if chess_board[pos[1]][pos[0]]==1*turns:
		available_slot,kill_slot=pawn(True,(0,0))

	if chess_board[pos[1]][pos[0]]==2*turns:
		available_slot,kill_slot=rook(True,(0,0))

	if chess_board[pos[1]][pos[0]]==3*turns:
		available_slot,kill_slot=knight(True,(0,0))

	if chess_board[pos[1]][pos[0]]==4*turns:
		available_slot,kill_slot=bishop(True,(0,0))

	if chess_board[pos[1]][pos[0]]==5*turns:
		available_slot,kill_slot=queen(True,(0,0))

	if chess_board[pos[1]][pos[0]]==6*turns:
		available_slot,kill_slot=king(True,(0,0))

	

	for slot in available_slot:
		pixel_pos=conv_to_pixel((slot[1],slot[0]))
		draw_rect(pixel_pos[0],pixel_pos[1],88,88,5,(0,255,0))
		# pygame.draw.circle(gameDisplay,(239,216,69),(pixel_pos[0]+44,pixel_pos[1]+44),10)

	

	for slot in kill_slot:
		
		pixel_pos=conv_to_pixel((slot[1],slot[0]))
		draw_rect(pixel_pos[0],pixel_pos[1],88,88,5,(255,0,0))
		# pygame.draw.circle(gameDisplay,(0,255,0),(pixel_pos[0]+44,pixel_pos[1]+44),20)

	#checking conditions
	temp_chess_board=deepcopy(chess_board)
	# temp_chess_board=deepcopy(chess_board)
	# if check1==True or check2==True:
	# 	chess_board=temp_chess_board
	selected_pos=move_peice(available_slot,kill_slot)
	# print(turns)
	# if check2==True or check1==True:
	# 	selected_pos=checked_pos
	
	if determine_check_1():
		# pass
		print("check 1")
		text = STAT_FONT.render("CHECK",3, (255,0,0))
		gameDisplay.blit(text, (5,600))
		test=deepcopy(chess_board)
		result1=check_for_checkmates_1()
		if result1==True:

			print("black wins CHECKMATE")
			pygame.draw.rect(gameDisplay,(255,255,255),(230,350,620,60))

			text2 = stat_font.render("black wins CHECKMATE",3, (0,0,0))
			gameDisplay.blit(text2, (250,350))
			# exit()
		chess_board=test
		if turns==-1:
			chess_board=temp_chess_board
			turns*=-1
	if determine_check_2():
		# pass
		print("check 2")
		text = STAT_FONT.render("CHECK",3, (255,0,0))
		gameDisplay.blit(text, (5,100))
		test=deepcopy(chess_board)
		result2=check_for_checkmates_2()
		if result2==True:
			print("player 1 wins CHECKMATE")
			pygame.draw.rect(gameDisplay,(255,255,255),(230,350,620,60))

			text2 = stat_font.render("white wins CHECKMATE",3, (0,0,0))
			gameDisplay.blit(text2, (250,350))
			# exit()

		chess_board=test
		if turns==1:
			chess_board=temp_chess_board
			turns*=-1

def checkpos(pos,x,y,w,h):
	if pos[0]>=x and pos[0]<=x+w:
		if pos[1]>=y and pos[1]<=y+h:
			if pygame.mouse.get_pressed()[0]:
				return True
	else:
		return False


def P_Moves(board,color):

	possiblemoves=[]

	checking_pieces=[]
	for i in range(8):
		for j in range(8):
			if color==-1:
				if board[i][j]<0:
					checking_pieces.append((j,i))
			if color==1:
				if board[i][j]>0:
					checking_pieces.append((j,i))
	
	for pos in checking_pieces:
	
		if board[pos[1]][pos[0]]==1*color:
			available_slot,kill_slot=pawn(False,pos)

		if board[pos[1]][pos[0]]==2*color:
			available_slot,kill_slot=rook(False,pos)

		if board[pos[1]][pos[0]]==3*color:
			available_slot,kill_slot=knight(False,pos)

		if board[pos[1]][pos[0]]==4*color:
			available_slot,kill_slot=bishop(False,pos)

		if board[pos[1]][pos[0]]==5*color:
			available_slot,kill_slot=queen(False,pos)

		if board[pos[1]][pos[0]]==6*color:
			available_slot,kill_slot=king(False,pos)

		possiblemoves.append(((pos[1],pos[0]),available_slot+kill_slot))

			
	return possiblemoves

def move_maker(board,mover):

	move=mover[1]
	idd=mover[0]
	board[move[0]][move[1]]=board[idd[0]][idd[1]]
	board[idd[0]][idd[1]]=0
	
	return board


def minimaxR(depth,board,isMaximizing):
	possibleMoves=P_Moves(board,-1)
	bestmove=-9999
	bestFinalMove=((1,3),(3,3))

	for element in possibleMoves:
		idd =element[0]
		moves=element[1]
		# print("*"*50)
		# print(moves)
		# print("*"*50)
		for move in moves:
			b_board=deepcopy(board)
			t_board=move_maker(b_board,(idd,move))
			# for i in range(8):
				# print(t_board[i])
			value=max(bestmove,minimax(depth-1,t_board,-10000,10000,not isMaximizing))

			if value>bestmove:
				# print("best move :",bestmove)
				bestmove=value
				bestFinalMove=(idd,move)

	return bestFinalMove

def minimax(depth,board,alpha,beta,isMaximizing):
	if depth==0:
		return -evaluation(board)

	if isMaximizing:
		breaking=False
		possibleMoves=P_Moves(board,-1)
		bestmove=-9999
		for element in possibleMoves:
			idd=element[0]
			moves=element[1]
			for move in moves:
				t_board=move_maker(board,(idd,move))
				bestmove=max(bestmove,minimax(depth-1,t_board,alpha,beta,not isMaximizing))
				alpha=max(alpha,bestmove)
				if beta<=alpha:
					breaking=True
					return bestmove
			if breaking:
				break
		return bestmove

	else:
		possibleMoves=P_Moves(board,1)
		bestmove=9999
		breaking=False
		for element in possibleMoves:
			idd=element[0]
			moves=element[1]
			for move in moves:
				t_board=move_maker(board,(idd,move))
				bestmove=min(bestmove,minimax(depth-1,t_board,alpha,beta,not isMaximizing))
				beta=min(beta,bestmove)
				if(beta<=alpha):
					breaking=True
					return bestmove
			if breaking:
				break
		return bestmove


def evaluation(board):
	evaluate=0
	for i in range(8):
		for j in range(8):
			if board[i][j]<0:
				evaluate+=getpiece_val(abs(board[i][j]))
			elif board[i][j]>0:
				evaluate-=getpiece_val(abs(board[i][j]))
	# print(evaluate)
	
	return evaluate

def getpiece_val(piece):
	value=0
	if piece==1:
		value=10 #10
	elif piece==2:
		value=50 #50
	elif piece==3:
		value=30 # 30
	elif piece==4:
		value=30 #30
	elif piece==5:
		value=90#90
	elif piece==6:
		value=900#900

	return value




def hover(pos,x,y,w,h):
	if pos[0]>=x and pos[0]<=x+w:
		if pos[1]>=y and pos[1]<=y+h:
			return True
	else:
		return False

def front_logo():
	t=0

	for t in range(150):
		menu1=pygame.transform.scale(menu,(900,750))
		gameDisplay.blit(menu1,(0,0,900,750))
		
		text = stat_font2.render("Chess   360",3, (255,255,255))
		globe1=pygame.transform.scale(globe,(200,200))
		gameDisplay.blit(globe1,(430,340,200,200))
		gameDisplay.blit(text, (200,425))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				# run=False
				exit()




def main_menu():
	global choice

	enter=True
	col1=(255,255,255)
	col2=(255,255,255)
	col3=(255,255,255)
	while enter:
		menu1=pygame.transform.scale(menu,(900,750))
		gameDisplay.blit(menu1,(0,0,900,750))
		text = stat_font.render("Chess 360",3, (255,255,255))
		gameDisplay.blit(text, (350,125))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
				# exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_b:
					enter=False

		p=pygame.mouse.get_pos()

		box1=pygame.transform.scale(frame,(740,105))
		gameDisplay.blit(box1,(130,282,740,105))
		pygame.draw.rect(gameDisplay,col1,(200,300,600,75))
		text = STAT_FONT.render("pvp offline",3, (0,0,0))
		gameDisplay.blit(text, (360,325))


		# box2=pygame.transform.scale(frame,(740,105))
		gameDisplay.blit(box1,(130,410,740,105))
		pygame.draw.rect(gameDisplay,col2,(200,425,600,75))
		text = STAT_FONT.render("pvp online",3, (0,0,0))
		gameDisplay.blit(text, (360,450))

		gameDisplay.blit(box1,(130,534,740,105))
		pygame.draw.rect(gameDisplay,col3,(200,550,600,75))
		text = STAT_FONT.render("play against computer",3, (0,0,0))
		gameDisplay.blit(text, (360,575))

		if hover(p,200,300,600,75):
			col1=(230,230,230)
			
		else:
			col1=(255,255,255)
		
		if hover(p,200,425,600,75):
			col2=(230,230,230)
			
		else:
			col2=(255,255,255)


		if hover(p,200,550,600,75):
			col3=(230,230,230)
			
		else:
			col3=(255,255,255)

		if checkpos(p,200,300,600,75):
			choice=1
			enter=False
		if checkpos(p,200,425,600,75):
			choice=2
			enter=False
		if checkpos(p,200,550,600,75):
			choice=3
			enter=False


		pygame.display.update()





if __name__=="__main__":
	#185,23
	# 704-42,23
	choice=-1
	pygame.display.set_caption("chess 360")
	checked_pos=0
	update_check_pos=False
	gameloop=True

	

	
	front_logo()
	while gameloop:
		main_menu()
		n=Network()

		current_pos=(185,639)
		check1=False
		check2=False
		posit=(0,0)
		cur_pos=(0,0)
		killed_pieces=[]
		turns=1
		run=True
		b=board()
		while run:

			if choice==1:
				gameDisplay.fill(brown)


				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						run=False
						# exit()
				

				b.draw_board()
				text3 = STAT_FONT.render("TURN",3, (255,255,255))
				gameDisplay.blit(text3, (10,350))
				if turns==1:
					text4 = STAT_FONT.render("white's",3, (255,255,255))
					gameDisplay.blit(text4, (12,300))
				else:
					text4 = STAT_FONT.render("black's",3, (255,255,255))
					gameDisplay.blit(text4, (12,300))
				select_peice()
				mark_current_pos()
				draw_peices()
				show_possible_moves()
				
				pygame.display.update()

			if choice==3:
				gameDisplay.fill(brown)
				b.draw_board()
				text3 = STAT_FONT.render("TURN",3, (255,255,255))
				gameDisplay.blit(text3, (10,350))
				if turns==1:
					text4 = STAT_FONT.render("white's",3, (255,255,255))
					gameDisplay.blit(text4, (12,300))
				else:
					text4 = STAT_FONT.render("black's",3, (255,255,255))
					gameDisplay.blit(text4, (12,300))
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						run=False
						# exit()

				if turns==-1 :
					# chess_board[2][3]=-1
					chess_board_copy=deepcopy(chess_board)
					move=minimaxR(3,chess_board,True)
					# print(move)
					chess_board=move_maker(chess_board,move)
					# for i in range(8):
					# 	print(chess_board[i])
					if determine_check_1():
				# pass
						print("check 1")
						text = STAT_FONT.render("CHECK",3, (255,0,0))
						gameDisplay.blit(text, (5,600))
						chess_board=chess_board_copy
						test=deepcopy(chess_board)
						result1=check_for_checkmates_1()
						if result1==True:
							print("player 2 wins CHECKMATE")
							print("black wins CHECKMATE")
							pygame.draw.rect(gameDisplay,(255,255,255),(230,350,620,60))

							text2 = stat_font.render("black wins CHECKMATE",3, (0,0,0))
							gameDisplay.blit(text2, (250,350))
							# exit()
						chess_board=test
						if turns==-1:
							chess_board=test

							turns*=-1
					if determine_check_2():
				# pass
						print("check 2")
						chess_board=chess_board_copy
						test=deepcopy(chess_board)
						result2=check_for_checkmates_2()
						if result2==True:
							print("player 1 wins CHECKMATE")
							print("player 1 wins CHECKMATE")
							pygame.draw.rect(gameDisplay,(255,255,255),(230,350,620,60))

							text2 = stat_font.render("white wins CHECKMATE",3, (0,0,0))
							gameDisplay.blit(text2, (250,350))
							# exit()

						chess_board=test
						if turns==1:
							chess_board=test
							turns*=-1
				if turns==-1:
					turns=1

				b.draw_board()
				select_peice()
				mark_current_pos()
				
				if turns==1:
					show_possible_moves()
				draw_peices()
				pygame.display.update()
			if choice==2:
				try:
					gameDisplay.fill(brown)
				# num+=1
					for event in pygame.event.get():
						if event.type==pygame.QUIT:
							run=False
							# exit()
					

					b.draw_board()
					# if turns==1:
					select_peice()
					mark_current_pos()
					# chess_board_recvd=n.send(chess_board)
					# for i in range(8):	
					# 	print(chess_board_recvd)
					draw_peices()
				

					# pos_arr=n.send([(-1,-1),(-1,-1)])
					if turns==1:

						show_possible_moves()
						pos_arr=n.send([posit,cur_pos])
					
					if turns==-1:	
						pos_arr=n.send([(-1,-1),(-1,-1)])
						print(pos_arr)
						pos=pos_arr[0]
						cur_pos_conv=pos_arr[1]
						chess_board[pos[1]][pos[0]]=chess_board[cur_pos_conv[1]][cur_pos_conv[0]]
						chess_board[cur_pos_conv[1]][cur_pos_conv[0]]=0
						turns*=-1
					chess_board[0][0]=-2
					pygame.display.update()
				except:
					text2 = stat_font.render("waiting for other player..",3, (255,0,0))
					gameDisplay.blit(text2, (250,350))
					pygame.display.update()
			
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_e:
					
						exit()
		for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_e:
					
						exit()




