
import pygame




from copy import deepcopy

import random



pygame.init()
import time
STAT_FONT = pygame.font.SysFont("comicsans",50)
disp_width=900
disp_height=800
gameDisplay = pygame.display.set_mode((disp_width,disp_height))
clock = pygame.time.Clock()

blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)
orange=(251,128,13)
yellow=(255,242,0)
red=(255,0,0)

size=3



bot=[]
b=[]
f=[]
l=[]
r=[]
top=[]
for _ in range(size):
	bot.append([])
	b.append([])
	f.append([])
	l.append([])
	r.append([])
	top.append([])


for i in range(size):
		
	for _ in range(size):	
		bot[i].append('w')
		b[i].append('y')
		f[i].append('b')
		l[i].append('r')
		r[i].append('g')
		top[i].append('o')

names=['w','y','b','r','g','o']
colors=[orange,yellow,white,blue,green,red]



def fill_sides():
	global bot,b,f,l,r,top,size


	bot=[]
	b=[]
	f=[]
	l=[]
	r=[]
	top=[]
	for _ in range(size):
		bot.append([])
		b.append([])
		f.append([])
		l.append([])
		r.append([])
		top.append([])


	for i in range(size):
		
		for _ in range(size):	
			bot[i].append('w')
			b[i].append('y')
			f[i].append('b')
			l[i].append('r')
			r[i].append('g')
			top[i].append('o')

def normalizer():
	global bot,b,f,l,r,top,size
	for i in range(size):
		for j in range(size):
			for k in names:
				if k==bot[i][j]:
					bot[i][j]=names.index(k)/5
				if k==b[i][j]:
					b[i][j]=names.index(k)/5
				if k==f[i][j]:
					f[i][j]=names.index(k)/5
				if k==l[i][j]:
					l[i][j]=names.index(k)/5
				if k==r[i][j]:
					r[i][j]=names.index(k)/5
				if k==top[i][j]:
					top[i][j]=names.index(k)/5
def convert_cube(cube):

	global bot,b,f,l,r,top,size,cube_ar
	
	

	for k in range(int(size**2)):
		# bot[i][j]=names[cube[0][k]]
		# b[i][j]=names[cube[1][k]*5]
		# f[i][j]=names[cube[2][k]*5]
		# l[i][j]=names[cube[3][k]*5]
		# r[i][j]=names[cube[4][k]*5]
		# top[i][j]=names[cube[5][k]*5]
		
		cube[0][k]=cube[0][k]*5
		cube[1][k]=cube[1][k]*5
		cube[2][k]=cube[2][k]*5
		cube[3][k]=cube[3][k]*5
		cube[4][k]=cube[4][k]*5
		cube[5][k]=cube[5][k]*5
	cube_ar=cube
	return cube
def convert_back_cube(cube):
	global bot,b,f,l,r,top,size,cube_ar
	
	

	for k in range(int(size**2)):
		# bot[i][j]=names[cube[0][k]]
		# b[i][j]=names[cube[1][k]*5]
		# f[i][j]=names[cube[2][k]*5]
		# l[i][j]=names[cube[3][k]*5]
		# r[i][j]=names[cube[4][k]*5]
		# top[i][j]=names[cube[5][k]*5]
		
		cube[0][k]=cube[0][k]/5
		cube[1][k]=cube[1][k]/5
		cube[2][k]=cube[2][k]/5
		cube[3][k]=cube[3][k]/5
		cube[4][k]=cube[4][k]/5
		cube[5][k]=cube[5][k]/5
	cube_ar=cube


def restore_cube_state(cube):
	global bot,b,f,l,r,top,size,cube_ar
	
	

	for k in range(int(size**2)):
		# bot[i][j]=names[cube[0][k]]
		# b[i][j]=names[cube[1][k]*5]
		# f[i][j]=names[cube[2][k]*5]
		# l[i][j]=names[cube[3][k]*5]
		# r[i][j]=names[cube[4][k]*5]
		# top[i][j]=names[cube[5][k]*5]
		
		cube[0][k]=cube[0][k]/5
		cube[1][k]=cube[1][k]/5
		cube[2][k]=cube[2][k]/5
		cube[3][k]=cube[3][k]/5
		cube[4][k]=cube[4][k]/5
		cube[5][k]=cube[5][k]/5
	cube_ar=cube


def shuf_gen(n):
	global size
	shuffle=[]
	# for i in range(random.randint(1,n)):

	# 		shuffle.append(random.choice(['t','s'])+random.choice(['1',str(size)])+random.choice(['a','c']))
	# return shuffle
	for i in range(n):

			shuffle.append(random.choice(['t','s','f'])+random.choice(['1',str(size)])+random.choice(['a','c']))
	return shuffle
def shuffle_cube(shuffle):
	for mov in shuffle:
		if mov[0]=='t':
			if mov[1]=='1':
				if mov[2]=='a':
					top_swap(1,'a')
				if mov[2]=='c':
					top_swap(1,'c')
			if mov[1]==str(size):
				if mov[2]=='a':
					top_swap(size,'a')
				if mov[2]=='c':
					top_swap(size,'c')
		if mov[0]=='s':
			if mov[1]=='1':
				if mov[2]=='a':

					side_swap(1,'a')
				if mov[2]=='c':
					side_swap(1,'c')
			if mov[1]==str(size):
				if mov[2]=='a':
					side_swap(size,'a')
				if mov[2]=='c':
					side_swap(size,'c')
		if mov[0]=='f':
			if mov[1]=='1':   #top face
				if mov[2]=='c':
					topface_rot('c')
				if mov[2]=='a':
					topface_rot('a')

			if mov[1]=='3': #3 corresponds to bottom face
				if mov[2]=='c':
					botface_rot('c')
				if mov[2]=='a':
					botface_rot('a')


def draw_cube(cube):
	hgt=50
	wid=50
	sep=3
	dis=10
	for i in range(6):

		if i==0:
			x_cord1=x_cord2=x_cord3=350
			y_cord1=y_cord2=y_cord3=400
			for j in range(size**2):
				if j<=(size-1):
					# print(i,j)
					# print(cube)
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep
		if i==1:
			x_cord1=x_cord2=x_cord3=350
			y_cord1=y_cord2=y_cord3=240-dis
			for j in range(size**2):
				if j<=(size-1):
				
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep
		if i==2:
			x_cord1=x_cord2=x_cord3=350
			y_cord1=y_cord2=y_cord3=560+dis
			for j in range(size**2):
				if j<=(size-1):
				
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep
		if i==3:
			x_cord1=x_cord2=x_cord3=190-dis
			y_cord1=y_cord2=y_cord3=400
			for j in range(size**2):
				if j<=(size-1):
				
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep
		if i==4:
			x_cord1=x_cord2=x_cord3=510+dis

			y_cord1=y_cord2=y_cord3=400
			for j in range(size**2):
				if j<=(size-1):
				
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep
		if i==5:
			x_cord1=x_cord2=x_cord3=670+dis+10
			y_cord1=y_cord2=y_cord3=400
			for j in range(size**2):
				if j<=(size-1):
				
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord1,y_cord1,wid,hgt))
					x_cord1+=wid+sep

				if j>=size and j<=(size+2):
					y_cord2=y_cord1+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord2,y_cord2,wid,hgt))
					x_cord2+=wid+sep

				if j>(size+2) and j<=(size**2-1):

					y_cord3=y_cord2+hgt+sep
					pygame.draw.rect(gameDisplay,colors[int(cube[i][j])],(x_cord3,y_cord3,wid,hgt))
					x_cord3+=wid+sep


def face_rot(face,rotation):
	size=3
	temp_face=deepcopy(face)
	if rotation=='a':
		temp1,temp2,temp3=face[0][0],face[0][1],face[0][2]
		for i in range(size):
			temp_face[0][i]=face[i][size-1]
		for i in range(size):
			temp_face[i][size-1]=face[size-1][size-1-i]
		for i in range(size):
			temp_face[size-1][i]=face[i][0]
		temp_face[0][0],temp_face[1][0],temp_face[2][0]=temp3,temp2,temp1

	if rotation=='c':
		temp1,temp2,temp3=face[0][0],face[1][0],face[2][0]

		for i in range(size):
			temp_face[i][0]=face[size-1][i]
		for i in range(size):
			temp_face[size-1][i]=temp_face[size-1-i][size-1]
		for i in range(size):
			temp_face[i][size-1]=face[0][i]

		temp_face[0][0],temp_face[0][1],temp_face[0][2]=temp3,temp2,temp1

	return temp_face

def topface_rot(rot):
	global top,l,r,b,bot,f
	if rot=='a':
		l1=deepcopy(l)
		f1=deepcopy(f)
		r1=deepcopy(r)
		b1=deepcopy(b)
		for j in range(size):
			temp_l=l1[0][j]
			temp_f=f1[0][j]
			temp_r=r1[0][j]
			temp_b=b1[2][2-j]

			f[0][j]=temp_l
			r[0][j]=temp_f
			b[2][2-j]=temp_r
			l[0][j]=temp_b

		top=face_rot(top,'a')
	
	if rot=='c':
		l1=deepcopy(l)
		f1=deepcopy(f)
		r1=deepcopy(r)
		b1=deepcopy(b)
		
		for j in range(size):
			temp_l=l1[0][j]
			temp_f=f1[0][j]
			temp_r=r1[0][j]
			temp_b=b1[2][2-j]

			f[0][j]=temp_r
			r[0][j]=temp_b
			b[2][2-j]=temp_l
			l[0][j]=temp_f
		top=face_rot(top,'c')
			

def botface_rot(rot):
	global top,l,r,b,bot,f
	if rot=='a':
		l1=deepcopy(l)
		f1=deepcopy(f)
		r1=deepcopy(r)
		b1=deepcopy(b)
		
		for j in range(size):
			temp_l=l1[2][j]
			temp_f=f1[2][j]
			temp_r=r1[2][j]
			temp_b=b1[0][2-j]

			f[2][j]=temp_l
			r[2][j]=temp_f
			b[0][2-j]=temp_r
			l[2][j]=temp_b

		bot=face_rot(bot,'c')
	
	if rot=='c':
		l1=deepcopy(l)
		f1=deepcopy(f)
		r1=deepcopy(r)
		b1=deepcopy(b)
		
		for j in range(size):
			temp_l=l1[2][j]
			temp_f=f1[2][j]
			temp_r=r1[2][j]
			temp_b=b1[0][2-j]

			f[2][j]=temp_r
			r[2][j]=temp_b
			b[0][2-j]=temp_l
			l[2][j]=temp_f
		bot=face_rot(bot,'a')

def side_swap(side,rotation):
	global size,top,bot,l,r,f,b
	if (rotation=='a'):
  
		i=side-1 
		l1=deepcopy(l)
		bot1=deepcopy(bot)
		r1=deepcopy(r)   
		top1=deepcopy(top)
		for j in range(size):
	    
			temp_l=l1[size-1-j][i]
			temp_bot=bot1[3-side][j]
			
			temp_r=r1[j][3-side]
			temp_top=top1[i][j]
			bot[3-side][size-1-j]=temp_l
			r[2-j][3-side]=temp_bot
			top[i][j]=temp_r

			l[2-j][i]=temp_top
			
			
		if i==0:
			b=face_rot(b,'c')
		if i==2:
			f=face_rot(f,'a')

	if (rotation=='c'):
		i=side-1 
		l1=deepcopy(l)
		bot1=deepcopy(bot)
		r1=deepcopy(r)   
		top1=deepcopy(top)
		for j in range(size):
	    
			temp_l=l1[size-1-j][i]
			temp_bot=bot1[3-side][j]
			
			temp_r=r1[j][3-side]
			temp_top=top1[i][j]
			bot[3-side][size-1-j]=temp_r
			r[j][3-side]=temp_top
			top[i][j]=temp_l

			l[j][i]=temp_bot
			

		if i==0:
			b=face_rot(b,'a')
		if i==2:
			f=face_rot(f,'c')

def top_swap(side,rotation):
	global size,top,bot,l,r,f,b
	if (rotation=='c'):
		j=side-1
		f1=deepcopy(f)
		top1=deepcopy(top)
		b1=deepcopy(b)
		bot1=deepcopy(bot)
		for i in range(size):
			temp_f=f1[i][j]
			temp_top=top1[i][j]
			temp_b=b1[i][j]
			temp_bot=bot1[i][j]
			top[i][j]=temp_f
			b[i][j]=temp_top
			bot[i][j]=temp_b
			f[i][j]=temp_bot
		if j==0:
			l=face_rot(l,'a')
		if j==2:
			r=face_rot(r,'c')



    
  
	if (rotation =='a'):
  
		j=side-1;
		j=side-1
		f1=deepcopy(f)
		top1=deepcopy(top)
		b1=deepcopy(b)
		bot1=deepcopy(bot)
    
		for i in range(size):

			temp_f=f1[i][j]
			temp_top=top1[i][j]
			temp_b=b1[i][j]
			temp_bot=bot1[i][j]
			top[i][j]=temp_b
			b[i][j]=temp_bot
			bot[i][j]=temp_f
			f[i][j]=temp_top
		if j==0:
			l=face_rot(l,'c')
		if j==2:
			r=face_rot(r,'a')

def cube_state():
		
	total_cube=[]
	for _ in range(6):
		total_cube.append([])

	for i in range(6):
		for j in range(size):
			for k in range(size):
				if i==0:
					total_cube[i].append(bot[j][k])
				if i==1:
					total_cube[i].append(b[j][k])
				if i==2:
					total_cube[i].append(f[j][k])
				if i==3:
					total_cube[i].append(l[j][k])
				if i==4:
					total_cube[i].append(r[j][k])
				if i==5:
					total_cube[i].append(top[j][k])

	return total_cube
def changer():
	global cube_ar,bot,b,f,top,r,l,size
	k=0
	for i in range(size):
		for j in range(size):

			
			
			bot[i][j]=cube_ar[0][k]
			b[i][j]=cube_ar[1][k]
			f[i][j]=cube_ar[2][k]
			l[i][j]=cube_ar[3][k]
			r[i][j]=cube_ar[4][k]
			top[i][j]=cube_ar[5][k]
			
			k+=1
def change_back():
	global cube_ar,bot,b,f,top,r,l,size
	k=0
	for i in range(size):
		for j in range(size):
			
			cube_ar[0][k]=bot[i][j]
			cube_ar[1][k]=b[i][j]
			cube_ar[2][k]=f[i][j]
			cube_ar[3][k]=l[i][j]
			cube_ar[4][k]=r[i][j]
			cube_ar[5][k]=top[i][j]
			
			
			k+=1










def solve_cube(mov):
	global cube_ar,bot,b,f,l,r,top
	changer()
	if mov==1:
			
		top_swap(1,'c')
			
		
	if mov==0:
		
		top_swap(1,'a')
		
		
	if mov==3:
		
			
		top_swap(size,'c')
		
		

	if mov==2:
		
		top_swap(size,'a')
		
		
	if mov==5:
		
	
		side_swap(1,'c')
		
		
	if mov==4:
		
		side_swap(1,'a')
		
		

	if mov==7:
		
			
		side_swap(size,'c')
		
		
	if mov==6:
		
		side_swap(size,'a')
	
	if mov==8:
		
		topface_rot('a')

	if mov==9:

		topface_rot('c')
		

	if mov==10:

		botface_rot('a')


	if mov==11:

		botface_rot('c')

		

def denormalize():
	global bot,b,f,l,r,top,size
	for i in range(size):
		for j in range(size):
			bot[i][j]=names[int(bot[i][j])]
			b[i][j]=names[int(b[i][j])]
			f[i][j]=names[int(f[i][j])]
			l[i][j]=names[int(l[i][j])]
			r[i][j]=names[int(r[i][j])]
			top[i][j]=names[int(top[i][j])]
		
def solve_daisy():
	global bot,b,f,r,top,b,cube_ar,moves,solving
	delay=0.3
	top_daisy=0
	left_daisy=0
	right_daisy=0
	bot_daisy=0
	def check_daisy():
		if top[1][0]==0:
			left_daisy=1
		if top[1][2]==0:
			right_daisy=1
		if top[0][1]==0:
			top_daisy=1
		if top[2][1]==0:
			bot_daisy=1

	# names=['w','r','o','b','g','y']  lookup for color schemes
	check_daisy()
	
	# print(f)
	# print(l)
	# print(b)
	# print(r)
	draw_cube(cube_ar)
	time.sleep(delay)
	pygame.display.update()
	if f[1][0]==0:
		solving.append(move.index('t1c'))
		# solve_cube(move.index('t1c'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)
	if l[1][0]==0:
		solving.append(move.index('s1c'))
		# solve_cube(move.index('s1c'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)
	if b[1][2]==0:
		solving.append(move.index('t3a'))
		# solve_cube(move.index('t3a'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)
	if r[1][0]==0:
		solving.append(move.index('s3a'))
		# solve_cube(move.index('s3a'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)

	if f[1][2]==0:
		solving.append(move.index('t3c'))
		# solve_cube(move.index('t3c'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)
	if l[1][2]==0:
		solving.append(move.index('s3c'))
		# solve_cube(move.index('s3c'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)

	if b[1][0]==0:
		
		solving.append(move.index('t1a'))
		# solve_cube(move.index('t1a'))

		draw_cube(cube_ar)
		pygame.display.update()
		
		
		time.sleep(delay)
	if r[1][2]==0:
		solving.append(move.index('s1a'))
		# solve_cube(move.index('s1a'))
		pygame.display.update()
		draw_cube(cube_ar)
		
		time.sleep(delay)

	 

	check_daisy()
	print(left_daisy,right_daisy,top_daisy,bot_daisy)
	print(solving)
	

			
	




if __name__=="__main__":
	no_of_shuffles=10
	solving=[]
	move=['t1a','t1c','t3a','t3c','s1a','s1c','s3a','s3c','f1a','f1c','f3a','f3c']

	#call in the trained model
	
	solved_arr=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0], [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]]
	solved_arr2=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6], [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8], [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

	failsafe=[]
	count=0
	turns_not_over=True
	shuffle_not_over=True
	

	if shuffle_not_over:
		fill_sides()
		normalizer()
		# shuffle=shuf_gen(no_of_shuffles)
		shuffle=['t3c','s1c','f1a','s3a','t1a']
		# print(shuffle)
		shuffle_cube(shuffle)
		print("shuffle used to shuffle the cube:")
		print(shuffle)
		# print_mat()
		# print(cube_state())
		cube_ar=cube_state()
		shuffle_not_over=False
	
	
	
	diasy=True
	
	
	
		


	gameDisplay.fill((0,0,0))
	
	cube_ar=convert_cube(cube_ar)

	
	

	changer()

	
	solve_daisy()



	
	
	# print("movement taken :"+str(move[solution]))
	change_back()
	convert_back_cube(cube_ar)
	cube_ar=convert_cube(cube_ar)
	# draw_cube(cube_ar)
	
	
	count+=1

	if cube_ar==solved_arr:

		turns_not_over=False



	restore_cube_state(cube_ar)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			pygame.quit()
			quit()
	time.sleep(0.5)
	pygame.display.update()

	
	if cube_ar==solved_arr2:
		# print("solllevvvd")
		text = STAT_FONT.render("CUBE SOLVED",3, (255,255,255))
		gameDisplay.blit(text, (330,160))

		text = STAT_FONT.render("TOTAL MOVES :"+str(count),3, (255,255,255))
		gameDisplay.blit(text, (550,260))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			pygame.quit()
			quit()
			
	pygame.display.update()


	



