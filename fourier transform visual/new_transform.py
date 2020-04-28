import math
import pygame

pygame.init()
width=900
height=600
gameDisplay=pygame.display.set_mode((width,height))
wave=[]
white=(255,255,255)
red=(255,0,0)

def Fourier_transform(signalX,signalY):
	n=50

	Transform=[]
	for xwave in signalX:

		for f in range(n):
			Re=0
			Im=0

			for ywave in signalY:
				theta=2*math.pi*f*xwave

				Re+=ywave*math.cos(theta)
				Im-=ywave*math.sin(theta)

			Re/=len(signalY)
			Im/=len(signalY)

			arg=(Re**2+Im**2)**0.5
			angle=math.atan2(Im,Re)

			Transform.append([f,arg,angle])

	return Transform


def drawepicycles(signal):
	signalX=[]
	signalY=[]

	for s in signal:
		signalX.append(s[0])
		signalY.append(s[1])

	transform=Fourier_transform(signalX,signalY)
	freq,angle,arg=[],[],[]

	for t in transform:
		freq.append(t[0])
		angle.append(t[2])
		arg.append(t[1])

	x=sum(signalX)//len(signalX)
	y=sum(signalY)//len(signalY)

	for i in range(len(transform)):
		x_pos=int(x)
		y_pos=int(y) 
		radius=int((arg[i])*freq[i]*math.pi)

		pygame.draw.circle(gameDisplay,white,(x_pos,y_pos),radius)
		x+=radius*math.cos(angle[i])
		y+=radius*math.sin(angle[i])

	global wave
	x,y=int(x),int(y)

	wave.append((x,y))

	for w in wave:
		gameDisplay.set_at(w,red)

def create_signal():
	signal=[]
	for i in range(300,400):
		signal.append([i,400])

	return signal 


if __name__=="__main__":

	sig=create_signal()
	run=True
	while run:
		gameDisplay.fill(0)

		drawepicycles(sig)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False


		pygame.display.update()




