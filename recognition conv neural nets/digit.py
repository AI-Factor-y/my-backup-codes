import pygame
import time
import os

pygame.init()
gameDisplay = pygame.display.set_mode((400,400))

clock = pygame.time.Clock()


#global convolution search strategic matrices 

x_mat1=[[-1,1,-1],
		[-1,1,-1],
		[-1,1,-1]]

x_mat2=[[-1,1,-1],
		[-1,1,-1],
		[-1,1,-1]]

x_mat3=[[-1,1,-1],
		[-1,1,-1],
		[-1,1,-1]]
x_mat4=[[-1,1,-1],
		[-1,1,-1],
		[-1,1,-1]]

y_mat1=[[1,1,1],
		[-1,-1,-1],
		[-1,-1,-1]]
y_mat2=[[-1,-1,-1],
		[-1,-1,-1],
		[1,1,1]]

y_mat3=[[-1,-1,1],
		[-1,1,-1],
		[1,-1,-1]]
y_mat4=[[-1,-1,-1],
		[-1,-1,-1],
		[1,1,1]]


z_mat1=[[1,1,1],
		[-1,-1,-1],
		[-1,-1,-1]]
z_mat2=[[-1,-1,1],
		[-1,-1,1],
		[-1,-1,1]]

z_mat3=[[-1,-1,-1],
		[-1,-1,-1],
		[1,1,1]]
z_mat4=[[-1,-1,-1],
		[1,1,1],
		[-1,-1,-1]]






white=(255,255,255)
black=(0,0,0)
draw_arr=[]

status_arr=[]
for _ in range(10):
	status_arr.append([])
for i in range(10):
	for j in range(10):
		status_arr[i].append(-1)



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
					pygame.quit()
					master_flag=1
					break
				if master_flag==1:
					break
				if event.type==pygame.KEYDOWN:
					for i in range(10):
						for j in range(10):
							status_arr[i][j]=(-1)
		if master_flag==1:
			break


		pygame.display.update()

def convolution(mat):
	
	global status_arr
	convolute=[]
	for i in range(10):
		for j in range(10):
			sum=0
			for x in range(3):
				for y in range(3):
					try:
						sum+=status_arr[i+x][j+y]*mat[x][y]
					except:
						pass
			convolute.append(sum/9)
	modified_cov=[]
	for i in range(10):
		modified_cov.append([])
	k=0
	for i in range(10):
		for j in range(10):
			modified_cov[i].append(convolute[k])
			k+=1


	return modified_cov

def relu(con_mat):
	for i in range(10):
		for j in range(10):
			if con_mat[i][j]<0:
				con_mat[i][j]=0
	return con_mat


def pooling(rel_mat):
	pool_arr=[]
	for i in range(0,10,2):
		for j in range(0,10,2):

			maxi_arr=[]
			for x in range(2):
				for y in range(2):
					try:
						maxi_arr.append(rel_mat[i+x][j+y])
					except:
						pass
			pool_arr.append(max(maxi_arr))
	temp=[]
	for i in range(5):
		temp.append([])
	k=0
	for i in range(5):
		for j in range(5):
			temp[i].append(pool_arr[k])
			k+=1
	pool_arr=temp
	return pool_arr


if __name__=="__main__":
	
	
	draw_grid()
	conv_1=[pooling(relu(convolution(x_mat1))),pooling(relu(convolution(x_mat2))),pooling(relu(convolution(x_mat3))),pooling(relu(convolution(x_mat4)))]
	conv_2=[pooling(relu(convolution(y_mat1))),pooling(relu(convolution(y_mat2))),pooling(relu(convolution(y_mat3))),pooling(relu(convolution(y_mat4)))]
	conv_3=[pooling(relu(convolution(z_mat1))),pooling(relu(convolution(z_mat2))),pooling(relu(convolution(z_mat3))),pooling(relu(convolution(z_mat4)))]
	summer_x=0
	summer_y=0
	summer_z=0
	for i in range(3):
		for j in range(5):
			summer_x+=sum(conv_1[i][j])

	for i in range(4):
		for j in range(5):
			summer_y+=sum(conv_2[i][j])
	for i in range(4):
		for j in range(5):
			summer_z+=sum(conv_3[i][j])

	prob=[summer_x/100,summer_y/100,summer_z/100]
	
	if prob.index(max(prob))==0:
		print("it is 1")
	elif prob.index(max(prob))==1:
		print("it is 2")
	elif prob.index(max(prob))==2:
		print("it is 3")



	


	


