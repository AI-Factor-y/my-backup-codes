
import pygame
import time
import random

pygame.init()
pygame.display.set_caption("mazes")

width=600
height=600
width_s=5
gameDisplay=pygame.display.set_mode((width,height))


class box:

	def __init__(self,x,y):

		self.x=x
		self.y=y
		self.width=width_s
		self.height=width_s
		self.color=(200,0,200)
		self.white=(255,255,255)
		self.visited=False
		self.solve_visit=False
		self.wall=[True,True,True,True]   # [top,right,bottom,left]

	def draw(self):
		if self.visited:

			pygame.draw.rect(gameDisplay,self.color,(self.y*self.height,self.x*self.width,self.width,self.height))
		self.draw_rect(self.y*self.height,self.x*self.width,self.width,self.height,self.white,2)

	def draw_rect(self,x,y,w,h,color,t):

		if self.wall[0]:
			pygame.draw.line(gameDisplay,color,(x,y),(x+w,y),t)
		if self.wall[1]:
			pygame.draw.line(gameDisplay,color,(x+w,y),(x+w,y+h),t)
		if self.wall[2]:
			pygame.draw.line(gameDisplay,color,(x+w,y+h),(x,y+h),t)
		if self.wall[3]:
			pygame.draw.line(gameDisplay,color,(x,y+h),(x,y),t)

	



def create_boxes():

	all_boxes=[]
	t_box=box(0,0)
	for i in range(width//t_box.width):
		for j in range(height//t_box.height):

			all_boxes.append(box(i,j))

	return all_boxes

def draw_boxes(boxes):
	gameDisplay.fill(51)
	for box_ in boxes:
		if box_.visited==True:
			box_.draw()
	pygame.display.update()

def decode_pos(pos):
	i,j=pos
	
	return (i)*(height//width_s)+j

def neighbours(cur_box,boxes):

	if cur_box.x>0:
		top_n=boxes[decode_pos((cur_box.x-1,cur_box.y))]
	else:
		top_n=None

	if cur_box.y<(width//cur_box.width)-1:
		left_n=boxes[decode_pos((cur_box.x,cur_box.y+1))]
	else:
		left_n=None

	if cur_box.x<(height//cur_box.height)-1:
		bot_n=boxes[decode_pos((cur_box.x+1,cur_box.y))]
	else:
		bot_n=None

	if cur_box.y>0:
		right_n=boxes[decode_pos((cur_box.x,cur_box.y-1))]
	else:
		right_n=None

	return [top_n,left_n,bot_n,right_n]


stack=[]	

def create_maze(boxes,start=(0,0)):
	global stack
	pos=decode_pos(start)
	
	current_cell=boxes[pos]
	while True:
		
		current_cell.visited=True
		
		surr=neighbours(current_cell,boxes)
		availabe_slot=[]
		for n in surr:
			if n!=None and n.visited==False:
				availabe_slot.append(n)

		
		# print(len(availabe_slot))
		if len(availabe_slot)==0:
			if len(stack)==0:
				print("maze finished")
				return boxes
			next_cell=stack.pop()
			# print(next_cell)
		else:
			next_cell=random.choice(availabe_slot)
		if len(availabe_slot)!=0:
			stack.append(current_cell)
		draw_boxes(boxes)
		# time.sleep(0.2)
		next_cell.color=(200,0,0)
		current_cell.color=(70,70,70)
		direction_x=next_cell.x-current_cell.x 

		direction_y=next_cell.y-current_cell.y

		if direction_y==1:
			current_cell.wall[1]=False
			next_cell.wall[3]=False
		if direction_y==-1:
			current_cell.wall[3]=False
			next_cell.wall[1]=False
		if direction_x==1:
			current_cell.wall[2]=False
			next_cell.wall[0]=False
		if direction_x==-1:
			current_cell.wall[0]=False
			next_cell.wall[2]=False



		for event in pygame.event.get():

			if event.type==pygame.QUIT:
				exit()



		current_cell=next_cell
	
	


	




stack=[]

def search_wall(cur,new):
	direction_x=new.x-cur.x 

	direction_y=new.y-cur.y

	if direction_y==1:
		if cur.wall[1]:
			return False
		else:
			return True
	
	if direction_y==-1:
		if cur.wall[3]:
			return False
		else:
			return True

	if direction_x==-1:
		if cur.wall[0]:
			return False
		else:
			return True

	if direction_x==1:
		if cur.wall[2]:
			return False
		else:
			return True

	


def solve_maze(boxes,start=(0,0),end=(10,10)):
	global stack
	pos=decode_pos(start)
	
	current_cell=boxes[pos]
	path=[]
	while True:
		
		current_cell.solve_visit=True
		if current_cell.x==end[0]:
			if current_cell.y==end[1]:
				print("path found")
				return path
		surr=neighbours(current_cell,boxes)
		availabe_slot=[]
		for n in surr:
			if n!=None:
				print(search_wall(current_cell,n))
			if n!=None and n.solve_visit==False and search_wall(current_cell,n):
				availabe_slot.append(n)

		
		print(len(availabe_slot))
		if len(availabe_slot)==0:
			if len(stack)==0:
				print("maze finished")
				return None
			next_cell=stack.pop()
			path.pop()
			# print(next_cell)
		else:
			next_cell=random.choice(availabe_slot)
			path.append(next_cell)
		if len(availabe_slot)!=0:
			stack.append(current_cell)
		draw_boxes(boxes)
		time.sleep(0.02)
		next_cell.color=(239,166,75)
		current_cell.color=(200,0,200)
		
		



		for event in pygame.event.get():

			if event.type==pygame.QUIT:
				exit()



		current_cell=next_cell
into=True
while into:
	for event in pygame.event.get():

			if event.type==pygame.QUIT:
				into=False

boxes=create_boxes()
boxes=create_maze(boxes,start=(0,0))
got=False
while not got:
	draw_boxes(boxes)

	pos=pygame.mouse.get_pos()

	if pygame.mouse.get_pressed()[0]:
		start_pos=pos
		start_pos=(start_pos[1]//width_s,start_pos[0]//width_s)
		position=decode_pos(start_pos)
		boxes[position].color=(0,0,200)


	if pygame.mouse.get_pressed()[2]:
		end_pos=pos 
		end_pos=(end_pos[1]//width_s,end_pos[0]//width_s)
		position=decode_pos(end_pos)
		boxes[position].color=(0,255,0)



	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			got=True






# print(boxes)
path=solve_maze(boxes,start=start_pos,end=end_pos)

for p in path:
	x_pos=p.x
	y_pos=p.y

	position=decode_pos((x_pos,y_pos))

	boxes[position].color=(0,200,0)


got=False
while not got:
	draw_boxes(boxes)

	



	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			got=True







if __name__=="__main__":


	run=True

	while run:

		gameDisplay.fill(51)

		# boxes=create_boxes()

		draw_boxes(boxes)

		for event in pygame.event.get():

			if event.type==pygame.QUIT:
				run=False

		pygame.display.update()




