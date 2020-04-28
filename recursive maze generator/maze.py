
import pygame
import time
import random

pygame.init()

width=800
height=800
width_s=10
gameDisplay=pygame.display.set_mode((width,height))


class box:

	def __init__(self,x,y):

		self.x=x
		self.y=y
		self.width=10
		self.height=10
		self.color=(200,0,200)
		self.white=(255,255,255)
		self.visited=False
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
				return None
			next_cell=stack.pop()
			# print(next_cell)
		else:
			next_cell=random.choice(availabe_slot)
		if len(availabe_slot)!=0:
			stack.append(current_cell)
		draw_boxes(boxes)
		# time.sleep(0.05)
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
		


	


boxes=create_boxes()
create_maze(boxes,start=(0,0))






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




