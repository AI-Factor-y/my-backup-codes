import pygame
import winsound
width=1400
height=600
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
pygame.display.set_caption("pi emulator")
gameDisplay=pygame.display.set_mode((width,height))
STAT_FONT = pygame.font.SysFont("comicsans",50)
class box:

	def __init__(self,mass,size,x,y,v):
		self.length=size
		self.mass=mass
		self.x=x
		self.y=y-size
		self.vel=v

	def draw_box(self,color):

		pygame.draw.rect(gameDisplay,color,(self.x,self.y,self.length,self.length))

	def move_box(self):
		self.x+=(self.vel)



def collitions():
	global s,b,col,k

	if b.x<=(s.x+s.length):
		#v1=(m1-m2)*u1/(m1+m2)+(2*m2)*u2/(m1+m2)
		#v2=2*m1*u1/(m1+m2)+(m2-m1)*u2/(m1+m2)
		u1=s.vel
		u2=b.vel

		s.vel=((s.mass-b.mass)*u1+(2*b.mass)*u2)/(s.mass+b.mass)
		b.vel=((2*s.mass*u1)+(b.mass-s.mass)*u2)/(s.mass+b.mass)
		k=b.vel
		col+=1
		winsound.Beep(2600,1)
		
	if s.x<=100:
		s.vel*=-1
		col+=1
		winsound.Beep(2600,1)
	# if b.x<=100:
	# 	b.vel*=-1







	
	



if __name__=="__main__":
	#box(mass,size,x,y,vel)
	exit=False
	
	s=box(1,50,600,400,0)
	b=box(100**2,150,700,400,-0.5)
	col=0
	k=0
	clock=pygame.time.Clock()
	run=True
	while run:
		
		gameDisplay.fill(white)
		text = STAT_FONT.render("Number of collitions : "+str(col),1, (255,0,0))
		gameDisplay.blit(text, (400,height-100))
		text2 = STAT_FONT.render("mass of small block : "+str(s.mass),1, (0,0,255))
		gameDisplay.blit(text2, (500,50))
		text3 = STAT_FONT.render("mass of big block   : "+str(b.mass),1, (0,0,255))
		gameDisplay.blit(text3, (500,100))

		pygame.draw.line(gameDisplay,black,(0,410),(width,410),20)
		for i in range(0,width,10):
			pygame.draw.line(gameDisplay,black,(i,430-10),(i-15,445-10),2)
		pygame.draw.line(gameDisplay,black,(50,0),(50,420),101)

		s.draw_box((100,100,100))
		b.draw_box((50,50,50))
		b.move_box()
		s.move_box()
		collitions()
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
				exit=True

		pygame.display.update()

