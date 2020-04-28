import pygame
import sys


sys.setrecursionlimit(10**6)
pygame.init()
fill_img=pygame.image.load("fill.png")
brush_img=pygame.image.load("brush.png")
clear_img=pygame.image.load("clear.png")
disp_width=800
disp_height=600

gameDisplay = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("floodfill")
clock = pygame.time.Clock()

white=(255,255,255)
black=(0,0,0)
violet=(245,35,199)
blue=(0,0,255)
light_blue=(91,180,248)
red=(255,0,0)
green=(0,255,0)
light_green=(159,236,81)
yellow=(245,228,47)
orange=(231,134,42)
brown=(190,107,39)

main_arr_size=100
main_arr=[]
for _ in range(100):
	main_arr.append([])
for i in range(100):
	for _ in range(100):
		main_arr[i].append((0,(0,0,0)))

class node:

	def __init__(self,parent,pos):
		self.parent=parent
		self.position=pos


def clear_disp():
	global main_arr,closedlists
	main_arr=[]
	for _ in range(100):
		main_arr.append([])
	for i in range(100):
		for _ in range(100):
			main_arr[i].append((0,(0,0,0)))
	closedlists=[]

color=[white,violet,blue,light_blue,red,green,light_green,yellow,orange,black]

def draw_rect(x,y,w,h,t):
	col=black
	pygame.draw.line(gameDisplay,col,(x,y),(x+w,y),t)
	pygame.draw.line(gameDisplay,col,(x+w,y),(x+w,y+h),t)
	pygame.draw.line(gameDisplay,col,(x+w,y+h),(x,y+h),t)
	pygame.draw.line(gameDisplay,col,(x,y+h),(x,y),t)


def colorpanel():
	global current_color,flag
	pygame.draw.line(gameDisplay,black,(0,525),(800,525),5)

	pygame.draw.line(gameDisplay,black,(700,0),(700,525),5)

	for i in range(len(color)):
		x_pos=30+i*75
		y_pos=540
		width=50
		height=50
		if color[i]==current_color:
			draw_rect(x_pos,y_pos,width,height,12)
		else:
			draw_rect(x_pos,y_pos,width,height,3)

		

		pygame.draw.rect(gameDisplay,color[i],(x_pos,y_pos,width,height))

		mousex=pygame.mouse.get_pos()[0]
		mousey=pygame.mouse.get_pos()[1]
		# print(gameDisplay.get_at((mousex,mousey)))
		if mousex>=x_pos and mousex<=x_pos+width:
			if mousey>=y_pos and mousey<=y_pos+height:
				if pygame.mouse.get_pressed()[0]==True:
					current_color=color[i]

	fill_icon=pygame.transform.scale(fill_img,(50,50))
	gameDisplay.blit(fill_icon,(720,100,50,50))
	# pygame.draw.rect(gameDisplay,black,(720,100,50,50))
	if flag==1:
		draw_rect(710,90,80,80,5)
	elif flag==-1:
		draw_rect(710,200,80,80,5)
	else:
		draw_rect(710,300,80,80,5)
	if mousex>=720 and mousex<=720+width:
			if mousey>=100 and mousey<=100+height:
				if pygame.mouse.get_pressed()[0]==True:
					flag=1
	brush_icon=pygame.transform.scale(brush_img,(50,50))
	gameDisplay.blit(brush_icon,(720,210,50,50))
	# pygame.draw.rect(gameDisplay,black,(720,210,50,50))
	if mousex>=720 and mousex<=720+width:
			if mousey>=210 and mousey<=210+height:
				if pygame.mouse.get_pressed()[0]==True:
					flag=-1
	clear_icon=pygame.transform.scale(clear_img,(50,50))
	gameDisplay.blit(clear_icon,(720,320,50,50))
	if mousex>=720 and mousex<=720+width:
			if mousey>=320 and mousey<=320+height:
				if pygame.mouse.get_pressed()[0]==True:
					clear_disp()
					flag=2





def append_shape():
	global current_color,draw_arr
	mousex=pygame.mouse.get_pos()[0]
	mousey=pygame.mouse.get_pos()[1]
	
	if pygame.mouse.get_pressed()[0]==True:
		# draw_arr.append((mousex,mousey,current_color))
		main_arr[mousex//8][mousey//8]=(1,current_color)

def draw_shape():
	global draw_arr,main_arr
	# for draw in draw_arr:
	# 	x=draw[0]
	# 	y=draw[1]
	# 	col=draw[2]
	# 	if(y<520):
	# 		pygame.draw.circle(gameDisplay,col,(x,y),5)
	for i in range(main_arr_size):
		for j in range(main_arr_size):
			if j<64 and i<87:
				if main_arr[i][j][0]==1:
					pygame.draw.rect(gameDisplay,main_arr[i][j][1],(i*(800//main_arr_size),j*(800//main_arr_size),12,12))

def get_target():
	global target
	mousex=pygame.mouse.get_pos()[0]
	mousey=pygame.mouse.get_pos()[1]
	if mousey<520:
		if pygame.mouse.get_pressed()[0]==True:
			 target=gameDisplay.get_at((mousex,mousey))



def issafe(x,y,target):

	return ((x>=0 and x<=87) and (y>=0 and y<=64)) and gameDisplay.get_at((x,y))==target

def floodfill(x,y,replace_color):
	global target,row,col,main_arr_size,closedlists
	get_target()
	openlist=[]
	closedlist=[]

	start_node=node(None,(x,y))
	openlist.append(start_node)

	while len(openlist)!=0:

		current_node=openlist[0]
		current_index=0

		openlist.pop(current_index)
		closedlist.append(current_node)
		children=[]
		for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            
			node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            
			if node_position[0] >= 87 or node_position[0] < 0 or node_position[1] > 64 or node_position[1] < 0:
				continue
			# print(node_position)
			if gameDisplay.get_at((node_position[0]*8,node_position[1]*8)) != target:
				continue

           
			new_node = node(current_node, node_position)

         
			children.append(new_node)

		for child in children:

			for closed_child in closedlist:
				if child == closed_child:
					continue

			openlist.append(child)
		#try to remove try except later
		try:
			for o in openlist:
				pygame.draw.rect(gameDisplay,replace_color,(o.position[0]*8,o.position[1]*8,8,8))
			for c in closedlist:
				pygame.draw.rect(gameDisplay,replace_color,(o.position[0]*8,o.position[1]*8,8,8))
		except:
			pass

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_x:
					openlist=[]
		pygame.display.update()
	closedlists.append((replace_color,closedlist))
	
	




if __name__=="__main__":
	gamePlay=True
	
	closedlists=[]
	target=(0,0,0,255)
	row=[-1,-1,-1,0,0,1,1,1]
	col=[-1,0,1,-1,1,-1,0,1]


	flag=-1
	current_color=black
	draw_arr=[]
	while gamePlay:

		gameDisplay.fill(white)
		colorpanel()
		if flag!=1:
			append_shape()
		
		for c in closedlists:

			for i in range(len(c[1])):
				pygame.draw.rect(gameDisplay,c[0],(c[1][i].position[0]*8,c[1][i].position[1]*8,8,8))

		draw_shape()
		if flag==1:
			mousex=pygame.mouse.get_pos()[0]
			mousey=pygame.mouse.get_pos()[1]
			if mousey<520 and mousex<700:
				if pygame.mouse.get_pressed()[0]==True:

					floodfill(mousex//8,mousey//8,current_color)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gamePlay=False

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_c:
					# print("haiii")
					clear_disp()
				if event.key==pygame.K_f:
					# print("haiii")
					flag*=-1
		
		

		pygame.display.update()