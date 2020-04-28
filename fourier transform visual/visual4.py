import pygame
import math

pygame.init()
width=900
height=600
gameDisplay=pygame.display.set_mode((width,height))

def fourirer_transform(signal):

	N=len(signal)
	transform=[]

	for k in range(N):
		real=0
		img=0

		for n in range(N):

			angle=-2*math.pi*k*n/N
			real+=(signal[n][0]*math.cos(angle)+signal[n][1]*math.sin(angle))
			img+=(signal[n][1]*math.cos(angle)-signal[n][1]*math.sin(angle))

		real/=N
		img/=N

		freq=k
		arg=(real**2+img**2)**0.5
		angle=math.atan2(img,real)

		transform.append([freq,arg,angle])

	return transform


def draw_epicycles(signal):

	global time,wave

	transform=fourirer_transform(signal)
	# print(transform)
	N=len(transform)
	#finding COM
	sumX=0
	sumY=0
	for trans in transform:
		sumX+=trans[0]
		sumY+=trans[1]

	x=sumX/N
	y=sumY/N
	#0=freq 1=arg 2=angle
	for i in range(1,N):

		x_pos=int(x)
		y_pos=int(y)
		radius=int(transform[i][1]*100)
	
		try:
			pygame.draw.circle(gameDisplay,white,(x_pos,y_pos),radius,1)
		except:
			
			pass

		x=x_pos+radius*math.cos(2*math.pi*transform[i][0]*time+transform[i][2])
		y=y_pos+radius*math.sin(2*math.pi*transform[i][0]*time+transform[i][2])
		
	time+=1/N
	
	wave.append((x_pos,y_pos))
	w1=wave[0]

	for w in range(1,len(wave)):
		pygame.draw.line(gameDisplay,red,w1,wave[w])
		w1=wave[w]

	if len(wave)>2000:
		wave.pop()

def create_signal():
	signal=[]
	for i in range(400,800):
		signal.append([i,400])
	return signal

if __name__=="__main__":
	signal=create_signal()
	#global variables
	#----------------------------
	white=(255,255,255)
	red=(255,0,0)
	time=0
	wave=[]
	run=True
	#-----------------------------
	while run:
		gameDisplay.fill(0)

		draw_epicycles(signal)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False


		pygame.display.update()










