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
def show_series(ori_depth,c_x,c_y):

	global time,speed,g_radius

	
		
		
		# print(radius)
	for depth in range(1,ori_depth+1,2):
		radius=int(g_radius*(4/(depth*math.pi)))
		c_cord=(int(c_x),int(c_y))
		pygame.draw.circle(gameDisplay,white,c_cord,radius,1)
		
		x_cord=c_x+radius*math.cos(depth*time)
		y_cord=c_y+radius*math.sin(depth*time)

		cord=(int(x_cord),int(y_cord))
		c_x,c_y=x_cord,y_cord


		pygame.draw.circle(gameDisplay,white,cord,2)

		#drawing line
		pygame.draw.line(gameDisplay,white,c_cord,cord)

		

	pygame.draw.line(gameDisplay,white,(x_cord,y_cord),(450,y_cord))
	signal.insert(0,y_cord)
	k=0
	for i in range(len(signal)):
		gameDisplay.set_at((450+int(k),int(signal[i])),white)
		k+=0.1
	
	if len(signal)>2000:
		signal.pop()



	time-=speed
	offset=500
	








if __name__=="__main__":
	run=True
	while run:

		gameDisplay.fill(0)

		show_series(5,200,400)

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit()

		pygame.display.update()