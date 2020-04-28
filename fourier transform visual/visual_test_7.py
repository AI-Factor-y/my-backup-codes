import pygame
import math
import operator
pygame.init()
width=900
height=600
gameDisplay=pygame.display.set_mode((width,height))

def fourier(x):
	transform=[]

	N=len(x)

	for k in range(N):
		real=0
		img=0

		for n in range(N):

			theta=2*math.pi*k*n/N

			real+=x[n]*math.cos(theta)
			img-=x[n]*math.sin(theta)

		real/=N
		img/=N

		freq=k
		amp=math.sqrt(real*real+img*img)

		phase=math.atan2(img,real)

		transform.append([freq,amp,phase])

	return transform


time=0
x=[]
y=[]
path=[]

def draw_epicycles(x,y,rotation,fourier):

	for i in range(len(fourier)):

		prevx=x
		prevy=y

		freq=fourier[i][0]
		radius=fourier[i][1]
		phase=fourier[i][2]

		x+=radius*math.cos(freq*time+phase+rotation)
		y+=radius*math.sin(freq*time+phase+rotation)

		try:
			pygame.draw.circle(gameDisplay,white,(int(prevx),int(prevy)),int(radius),1)
		except:
			pass

		pygame.draw.line(gameDisplay,white,(int(prevx),int(prevy)),(int(x),int(y)))

	return (x,y)


def get_draw_cord():
	white=(255,255,255)
	draw_Run=True
	x=[]
	y=[]
	while draw_Run:
		gameDisplay.fill(0)

		if pygame.mouse.get_pressed()[0]:
			x.append(pygame.mouse.get_pos()[0]-width/2)
			y.append(pygame.mouse.get_pos()[1]-height/2)

		for i in range(len(x)):
			pygame.draw.circle(gameDisplay,white,(int(x[i]+width/2),int(y[i]+height/2)),5)
		

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				draw_Run=False


		pygame.display.update()

	return x,y

x,y=get_draw_cord()

x_center=sum(x)/len(x)
y_center=sum(x)/len(x)

fourierX=fourier(x)
fourierY=fourier(y)

fourier_3d=fourierX+fourierY
fourierX=sorted(fourierX,key=operator.itemgetter(1),reverse=True)
fourierY=sorted(fourierY,key=operator.itemgetter(1),reverse=True)



white=(255,255,255)
red=(255,0,0)


run=True
#-----------------------------
while run:
	gameDisplay.fill(0)

	vx=draw_epicycles(width/2+50,height/2,0,fourierX)
	vy=draw_epicycles(vx[0],vx[1],math.pi/2,fourierY)
	v=(vy[0],vy[1])
	
	path.insert(0,v)
	pygame.draw.line(gameDisplay,white,(vx[0],vx[1]),(v[0],v[1]))
	pygame.draw.line(gameDisplay,white,(vy[0],vy[1]),(v[0],v[1]))
	
	prevx=path[0][0]
	prevy=path[0][1]

	for i in range(len(path)):
		# gameDisplay.set_at((int(path[i][0]),int(path[i][1])),white)

		pygame.draw.line(gameDisplay,red,(int(prevx),int(prevy)),(int(path[i][0]),int(path[i][1])))
		prevx=path[i][0]
		prevy=path[i][1]
		
	dt=2*math.pi/len(fourierX)
	time+=dt

	if time>2*math.pi:
		time=0
		path=[]

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False


	pygame.display.update()


