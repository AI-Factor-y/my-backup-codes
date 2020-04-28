import pygame
import time
import os
import numpy as np
# import tensorflow as tf 
# from tensorflow import keras
# import numpy as np 
# from matplotlib.pyplot import plt


pygame.init()
# gameDisplay = pygame.display.set_mode((400,400))

clock = pygame.time.Clock()


#global convolution search strategic matrices 




white=(255,255,255)
black=(0,0,0)
draw_arr=[]






width=40
# for i in range(20):
# 	draw_arr.append([])
for i in range(0,400,width):
	for j in range(0,400,width):
		draw_arr.append((i,j))


def rectangle(x,y,w,h,b_color):
	pygame.draw.line(gameDisplay,(255,255,255),(x,y),(x+w,y),5)
	pygame.draw.line(gameDisplay,(255,255,255),(x,y),(x,y+h),5)
	pygame.draw.line(gameDisplay,(255,255,255),(x+w,y),(x+w,y+h),5)
	pygame.draw.line(gameDisplay,(255,255,255),(x,y+h),(x+w,y+h),5)
	pygame.draw.rect(gameDisplay,b_color,(x,y,w,h))

def inside(cor,x,y,w,h):
	if(cor[0]>=x and cor[0]<=x+w) and (cor[1]>=y and cor[1]<=y+h):
		return True
	else:
		return False


def draw_grid():
	global draw_arr,status_arr
	
	while True:
		gameDisplay.fill((0,0,0))
		for i in range(len(draw_arr)):
			
			if(inside(pygame.mouse.get_pos(),draw_arr[i][0],draw_arr[i][1],width,width) and pygame.mouse.get_pressed()==(1,0,0)) :
				status_arr[int(draw_arr[i][0]/width)][int(draw_arr[i][1]/width)]=1

			
			rectangle(draw_arr[i][0],draw_arr[i][1],width,width,black)

		for i in range(10):
			for j in range(10):
				if status_arr[i][j]==1:
					rectangle(i*width,j*width,width,width,white)
		master_flag=0
		# print(pygame.mouse.get_pos())
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					pygame.display.quit()
					master_flag=1
					break
				if master_flag==1:
					break
				if event.type==pygame.KEYDOWN:
					for i in range(10):
						for j in range(10):
							status_arr[i][j]=(0)
		if master_flag==1:
			break


		pygame.display.update()



if __name__=="__main__":
	STAT_FONT = pygame.font.SysFont("comicsans",50)

	train_image=[]
	train_label=[]
	counter=0
	while True:
		counter+=1
		status_arr=[]
		gameDisplay = pygame.display.set_mode((400,400))
		for _ in range(10):
			status_arr.append([])
		for i in range(10):
			for j in range(10):
				status_arr[i].append(0)
		if counter<30:
			print("training x")
		else:
			print("training o")
		draw_grid()

		train_image.append(status_arr)
		if counter<=30:
			
			train_label.append(0)
		else:
			
			train_label.append(1)

		if counter==60:
			break

	# gameDisplay = pygame.display.set_mode((400,400))
	# draw_grid()
	np.save("image_data",train_image,allow_pickle=True,fix_imports=True)
	np.save("labels",train_label,allow_pickle=True,fix_imports=True)


	


	


