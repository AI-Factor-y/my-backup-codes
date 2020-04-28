import pygame
from copy import deepcopy
from network import Network
import os

pygame.init()

disp_width=900
disp_height=750

width_bet_sq=88
#global colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
brown=(213,125,58)
red=(255,0,0)
gameDisplay=pygame.display.set_mode((disp_width,disp_height))




class board:

	def __init__(self):
		self.board_x=185
		self.board_y=23
		self.board_width=704
		self.board_height=704
		self.color=white
		

	def draw_board(self):
		
		pygame.draw.rect(gameDisplay,white,(self.board_x,self.board_y,self.board_height,self.board_width))
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
				pygame.draw.rect(gameDisplay,check_color,(start_check_x+inc_x,start_check_y+inc_y,check_width,check_height))
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

def draw_rect(x,y,w,h,t):
	col=blue
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
				draw_rect(pos[0],pos[1],width_bet_sq,width_bet_sq,4)
				current_pos=pos
		if turns==-1:
			if pygame.mouse.get_pressed()[0] and (chess_board[arr_pos[1]][arr_pos[0]] <0):
				draw_rect(pos[0],pos[1],width_bet_sq,width_bet_sq,4)
				current_pos=pos

def mark_current_pos():
	global current_pos

	draw_rect(current_pos[0],current_pos[1],width_bet_sq,width_bet_sq,4)

def draw_peices():
	global chess_board
	#actually internally the array id flipped by row and column rememebr to reflip the array while d
	for i in range(8):
		for j in range(8):
			if chess_board[i][j]>0:
				piece_color=blue
				check_pos=chess_board[i][j]
			else:
				piece_color=red
				check_pos=chess_board[i][j]*-1

			if check_pos==1:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==2:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==3:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==4:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==5:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			if check_pos==6:
				pixel_pos=conv_to_pixel((j,i))

				pygame.draw.circle(gameDisplay,piece_color,(pixel_pos[0]+44,pixel_pos[1]+44),10)
			

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
		pygame.draw.circle(gameDisplay,(239,216,69),(pixel_pos[0]+44,pixel_pos[1]+44),10)

	

	for slot in kill_slot:
		
		pixel_pos=conv_to_pixel((slot[1],slot[0]))
		pygame.draw.circle(gameDisplay,(0,255,0),(pixel_pos[0]+44,pixel_pos[1]+44),20)

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
		test=deepcopy(chess_board)
		result1=check_for_checkmates_1()
		if result1==True:
			print("player 2 wins CHECKMATE")
			exit()
		chess_board=test
		if turns==-1:
			chess_board=temp_chess_board
			turns*=-1
	if determine_check_2():
		# pass
		print("check 2")
		test=deepcopy(chess_board)
		result2=check_for_checkmates_2()
		if result2==True:
			print("player 1 wins CHECKMATE")
			exit()

		chess_board=test
		if turns==1:
			chess_board=temp_chess_board
			turns*=-1


if __name__=="__main__":
	#185,23
	# 704-42,23
	n=Network()

	checked_pos=0
	update_check_pos=False
	
	posit=(0,0)
	cur_pos=(0,0)
	current_pos=(185,639)
	check1=False
	check2=False
	killed_pieces=[]
	turns=-1
	run=True
	b=board()
	while run:
		gameDisplay.fill(brown)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
				exit()
		

		b.draw_board()
		# if turns==1:
		select_peice()
		mark_current_pos()
		# chess_board_recvd=n.send(chess_board)
		# for i in range(8):	
		# 	print(chess_board_recvd)
		draw_peices()
	
		# pos_arr=n.send([(-1,-1),(-1,-1)])
		
		if turns==-1:
			show_possible_moves()
			pos_arr=n.send([posit,cur_pos])
		else:
			pos_arr=n.send([(-1,-1),(-1,-1)])
			pos=pos_arr[0]
			cur_pos_conv=pos_arr[1]
			chess_board[pos[1]][pos[0]]=chess_board[cur_pos_conv[1]][cur_pos_conv[0]]
			chess_board[cur_pos_conv[1]][cur_pos_conv[0]]=0
			if pos!=(-1,-1):
				turns*=-1
		chess_board[0][0]=-2



			# turns=1
		# try:
		# 	for i in range(8):
		# 		print(chess_board_recvd[i])
		# except:
		# 	pass
		os.system('cls')
		# try:
		# 	for i in range(8):
		# 		for j in range(8):
		# 			if chess_board_recvd[i][j]==0:
		# 				chess_board[i][j]=0
		# 			if chess_board_recvd[i][j]<0:
		# 				chess_board[i][j]=chess_board_recvd[i][j]
					
		# except:
		# 	pass
		# turns=1
		# try:
		# 	if (chess_board_recvd!=chess_board):
		# 		# print("hoho changed")
		# 		turns=1
		# 		chess_board=chess_board_recvd
		# except:
		# 	pass
		
		pygame.display.update()

