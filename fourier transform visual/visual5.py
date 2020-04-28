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

			angle=2*math.pi*k*n/N
			real+=signal[n][0]*math.cos(angle)
			img-=signal[n][1]*math.sin(angle)

		real/=N
		img/=N
		# print(str(real)+"  "+str(img))

		freq=k
		arg=(real*real+img*img)**0.5
		angle=math.atan2(img,real)

		transform.append([arg,freq,angle])


	# transform.sort()
	



	# for i in range(len(transform)):
	# 	print(transform[i][0])
	# exit()

	return transform


def draw_epicycles(signal):

	global time,wave

	transform=fourirer_transform(signal)
	# print(transform)
	N=len(transform)
	#finding COM
	sumX=0
	sumY=0
	for s in signal:
		sumX+=s[0]
		sumY+=s[1]

	x=sumX/len(signal)
	y=sumY/len(signal)
	#0=freq 1=arg 2=angle
	for i in range(1,N):

		x_pos=int(x)
		y_pos=int(y)
		radius=int(transform[i][0])
	
		try:
			pygame.draw.circle(gameDisplay,white,(x_pos,y_pos),radius)
		except:
			
			pass

		x=x_pos+radius*math.cos(2*math.pi*transform[i][1]*time+transform[i][2])
		y=y_pos+radius*math.sin(2*math.pi*transform[i][1]*time+transform[i][2])
		
	time+=2*math.pi/N
	
	wave.append((x_pos,y_pos))
	w1=wave[0]

	for w in range(1,len(wave)):
		pygame.draw.line(gameDisplay,red,w1,wave[w])
		w1=wave[w]

	if len(wave)>2000:
		wave.pop()

def create_signal():
	signal=[]
	for i in range(200,400):
		signal.append([i,200])
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
	print(fourirer_transform(signal))
	# # -----------------------------
	while run:
		gameDisplay.fill(0)

		draw_epicycles(signal)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False


		pygame.display.update()










