import math
import pygame

pygame.init()
width=900
height=600
gameDisplay=pygame.display.set_mode((width,height))
wave=[]
white=(255,255,255)
red=(255,0,0)


def Fourier_transform(signalX):

	Transform=[]

	for i in range(len(signalX)):

		Re=0
		Im=0
		for j in range(len(signalX)):
			theta=(2*math.pi*i*j)/len(signalX)

			Re+=signalX[j]*math.cos(theta)
			Im-=signalX[j]*math.sin(theta)
		Re/=len(signalX)
		Im/=len(signalX)

		arg=(Re**2+Im**2)**0.5
		angle=math.atan2(Im,Re)

		Transform.append([i,arg,angle])

	return Transform



	
	
time=0

def drawepicycles(signal):

	global time
	signalX=[]
	signalY=[]

	for s in signal:
		signalX.append(s[0])
		signalY.append(s[1])

	transform=Fourier_transform(signalX)
	transformY=Fourier_transform(signalY)
	freq,angle,arg=[],[],[]

	for t in transform:
		freq.append(t[0])
		angle.append(t[2])
		arg.append(t[1])

	x=400
	y=400

	for i in range(len(transform)):
		x_pos=int(x)
		y_pos=int(y) 
		radius=int(arg[i])
		radius2=int(transformY[i][1])
		angle2=int(transformY[i][2])
		freq2=int(transformY[i][0])
		try:
			pygame.draw.circle(gameDisplay,white,(x_pos,y_pos),radius,1)
		except:
			pass
		x=x_pos+radius*math.cos(2*math.pi*freq[i]*time+angle[i])
		# y=y_pos+radius*math.sin(2*math.pi*freq[i]*time+angle[i])
		y=y_pos+radius*math.sin(2*math.pi*freq2*time+angle2)

	time+=0.001

	global wave
	x,y=int(x),int(y)

	wave.append((x_pos,y_pos))
	w1=wave[0]
	for w in range(1,len(wave)):
		# gameDisplay.set_at(wave[w],red)
		pygame.draw.line(gameDisplay,red,w1,wave[w])
		w1=wave[w]

def create_signal():
	# signal=[[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400],[100,400],[100,400],[100,400],[100,400],[-100,400],[-100,400],[-100,400],[-100,400]]
	signal=[]
	for i in range(10,20):
		signal.append([i**2,400])

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




