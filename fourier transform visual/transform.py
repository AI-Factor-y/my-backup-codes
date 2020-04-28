import pygame
import math

pygame.init()
width=1000
height=600
gameDisplay=pygame.display.set_mode((width,height))
white=(255,255,255)


#global varibales
time=0
x_cord=0
y_cord=0
speed=0.005
g_radius=100

signal=[]
def fourier(f):

	transformed=[]

	for i in range(1,len(f)):
		Real=0
		Img=0

		for j in range(1,len(f)):
			x=(2*math.pi*i*j)/(len(f))

			Real+=f[j]*math.cos(x)
			Img-=f[j]*math.sin(x)

		Real/=len(f)
		Img/=len(f)
		freq=i
		amp=(Real**2+Img**2)**0.5
		
		phase=math.atan2(Img,Real)
		transformed.append((Real,Img,freq,amp,phase))


	return transformed
def show_series(ori_depth,c_x,c_y):

	global time,speed,g_radius
	f=[100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,100,100,100,-100,-100,-100]
	
	transformed=fourier(f)
	x_cord=300
	y_cord=400
		# print(radius)
	for trans in transformed:

		prevx=x_cord
		prevy=y_cord
		radius=trans[3]
		freq=trans[2]
		phase=trans[4]

		# c_cord=(int(c_x),int(c_y))
		print(radius)
		# pygame.draw.circle(gameDisplay,white,c_cord,int(radius),1)
		
		x_cord+=radius*math.cos(freq*time+phase)
		y_cord+=radius*math.sin(freq*time+phase)

		cord=(int(x_cord),int(y_cord))
		c_x,c_y=x_cord,y_cord


		pygame.draw.circle(gameDisplay,white,(int(prevx),int(prevy)),int(radius),1)

		#drawing line
		# pygame.draw.line(gameDisplay,white,c_cord,cord)

		

	# pygame.draw.line(gameDisplay,white,(x_cord,y_cord),(450,y_cord))
	signal.insert(0,y_cord)
	k=0
	for i in range(len(signal)):
		gameDisplay.set_at((int(signal[i]),450+int(k)),white)
		k+=0.1
	
	if len(signal)>2000:
		signal.pop()


	dt=2*math.pi/len(f)
	time+=dt
	offset=500
	








if __name__=="__main__":
	run=True
	clock=pygame.time.Clock()
	
	while run:
		clock.tick(20)


		gameDisplay.fill(0)

		show_series(5,200,400)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()

		pygame.display.update()



