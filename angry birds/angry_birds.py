import pygame
import os
import math
pygame.init()

STAT_FONT = pygame.font.SysFont("comicsans",30)
disp_width=1100
disp_height=500
gameDisplay = pygame.display.set_mode((disp_width,disp_height))

clock = pygame.time.Clock()
clock.tick(400)
#global variables
gravity=9.8
#global variables for the thickness of reflectors
x_bound=5
y_bound=5
score=0
tries=-1

#global obstacle array
obstacles=[]
#global pigs array
piggs=[]

#images initialisation
bird_img=pygame.image.load("bird.png")
wood_img=pygame.image.load("wood.png")
pig_img=pygame.image.load("pig.png")
catapult=pygame.image.load("catapult.png")
# square_wood=pygame.image.load("square_wood.png")
background_img=pygame.image.load("background.jpeg")

def draw_background():
	global background_img
	background_img=pygame.transform.scale(background_img,(disp_width,disp_height+20))
	gameDisplay.blit(background_img,(0,0))



class bird:
	global bird_img
	global gravity

	def __init__(self,x,y,theta):
		self.bird_x_initial=x
		

		self.bird_y_initial=y
		self.bird_x=x
		self.bird_y=y
		self.velocity=150
		self.theta=-theta
		self.vx=0
		self.vy=0
		self.direction_x=1
		self.direction_y=1
		self.time=0
		self.score=0

	def draw_bird(self):
		global bird_img
		# pygame.draw.circle(gameDisplay,(255,0,0),(int(self.bird_x),int(self.bird_y)),10)
		bird_img=pygame.transform.scale(bird_img,(40,40))
		gameDisplay.blit(bird_img,(int(self.bird_x),int(self.bird_y)))
	def mover(self):
		self.vx=self.direction_x*self.velocity*math.cos(math.radians(self.theta))
		self.vy=self.direction_y*self.velocity*math.sin(math.radians(self.theta))+gravity*(self.time)

		self.bird_x=self.bird_x_initial+(self.vx*self.time)*self.direction_x
		self.bird_y=self.bird_y_initial+(self.vy*self.time)*self.direction_y
		self.draw_bird()
		self.time+=0.1
		

		
class obstacle:
	global wood_img
	global x_bound,y_bound
	def __init__(self,x,y,width_w,height_h):
		self.flag_x=0
		self.flag_y=0
		self.x_reflec=x
		self.y_reflec=y
		self.h=height_h
		self.w=width_w

	

	def reflector_x(self,angry):
		if(angry.bird_x-10>=self.x_reflec and angry.bird_x-10<=(self.x_reflec+x_bound) and angry.bird_y+20>=self.y_reflec and angry.bird_y+20<=self.y_reflec+self.h) and self.flag_x!=1:
			angry.bird_x_initial=angry.bird_x
			angry.bird_y_initial=angry.bird_y
			angry.theta=180-math.degrees(math.tanh(angry.vy/angry.vx))
			angry.direction_x=-(1/2.5)
			angry.direction_y=(1/2)
			angry.time=0
			self.flag_x=1

	def reflector_y(self,angry):
		if(angry.bird_y+20>=self.y_reflec and angry.bird_y+20<=(self.y_reflec+y_bound) and angry.bird_x-10>=self.x_reflec and angry.bird_x-10<=self.x_reflec+self.w) and self.flag_y!=1:
			angry.bird_x_initial=angry.bird_x
			angry.bird_y_initial=angry.bird_y
			angry.theta=270-math.degrees(math.tanh(angry.vy/angry.vx))
			angry.direction_x=(1/2)
			angry.direction_y=(1/2)
			angry.time=0
			self.flag_y=1

	def draw_obs(self):
		global wood_img
		# pygame.draw.rect(gameDisplay,(204,145,44),(self.x_reflec,self.y_reflec,self.w,self.h))
		wood_img=pygame.transform.scale(wood_img,(self.w,self.h))
		gameDisplay.blit(wood_img,(int(self.x_reflec),int(self.y_reflec)))

class pigs:
	global pig_img
	def __init__(self,x,y,width_w,height_h):
		self.x=x
		self.y=y
		self.h=height_h
		self.w=width_w

	def drawpigs(self):
		global pig_img
		# pygame.draw.rect(gameDisplay,(64,217,53),(self.x,self.y,self.w,self.h))
		pig_img=pygame.transform.scale(pig_img,(self.w,self.h))
		gameDisplay.blit(pig_img,(int(self.x),int(self.y)))

	def collide(self,b):
		global score
		if b.bird_x>=self.x and b.bird_x<=self.x+self.w:
			if b.bird_y>=self.y and b.bird_y<=self.y+self.h:
				score+=1
				return 1
			else:
				return 0
		else:
			return 0








def aim_mechanics(angry_b,x,y,aim_radius,obst,pigy):
	angle=160
	aim_over=False
	global catapult
	while aim_over==False:
		# gameDisplay.fill((0,0,0))
		draw_background()
		catapult=pygame.transform.scale(catapult,(40,70))
		gameDisplay.blit(catapult,(x+50,y-20))
		
		for o in obst:
			o.draw_obs()
		for p in pigy:
			p.drawpigs()
			

		keys = pygame.key.get_pressed()
		if angle<179:
			if  keys[pygame.K_i]:
				angle+=1
		if keys[pygame.K_m]:
			angle-=1
		if keys[pygame.K_l]:
			aim_over=True
			return angle
		global score,tries
		text = STAT_FONT.render("angle : "+str(angle),1, (255,255,255))
		gameDisplay.blit(text, (10,450))
		text = STAT_FONT.render("score : "+str(score),1, (255,255,255))
		gameDisplay.blit(text, (10,20))
		textx = STAT_FONT.render("Tries : "+str(tries),1, (255,255,255))
		gameDisplay.blit(textx, (150,20))

		#line drawing

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					pygame.quit()

					quit()
				


		# pygame.draw.circle(gameDisplay,(0,255,0),(int(x),int(y)),5)
		angry_x=x+aim_radius*math.cos(math.radians(angle))
		angry_y=y+aim_radius*math.sin(math.radians(angle))
		# pygame.draw.circle(gameDisplay,(255,0,0),(int(angry_x),int(angry_y)),10)
		global bird_img
		bird_img=pygame.transform.scale(bird_img,(40,40))
		gameDisplay.blit(bird_img,(int(angry_x),int(angry_y)))
		pygame.draw.line(gameDisplay,(0,0,0),(angry_x+7,angry_y+27),(x+80,y-5),10)
		pygame.draw.line(gameDisplay,(0,0,0),(angry_x+7,angry_y+27),(x+62,y-7),10)

		pygame.display.update()
		




def creating_obstacles():
	global obstacles
	# obstacles.append(obstacle(720,300,100,20))
	obstacles.append(obstacle(1000,-300,10,1000))
	obstacles.append(obstacle(550,100,30,1000))
	obstacles.append(obstacle(600,200,30,1000))
	#ground
	obstacles.append(obstacle(650,250,30,1000))
	obstacles.append(obstacle(0,490,1700,50))
	obstacles.append(obstacle(685,300,400,20))
	obstacles.append(obstacle(550,250,30,900))
	obstacles.append(obstacle(720,400,310,20))
	obstacles.append(obstacle(800,400,40,100))
	obstacles.append(obstacle(830,153,20,150))
	obstacles.append(obstacle(720,153,350,20))
	obstacles.append(obstacle(900,100,100,60))


def creating_pigs():
	global piggs
	piggs.append(pigs(600,270,40,40))
	piggs.append(pigs(653,315,40,40))
	piggs.append(pigs(820,115,40,40))
	piggs.append(pigs(930,65,40,40))
	piggs.append(pigs(960,460,40,40))
	piggs.append(pigs(860,363,40,40))
	piggs.append(pigs(750,460,40,40))



def gameplay():
	global score,tries
	global tries
	global obstacles
	global piggs
	global catapult
	gameLOOP=True
	gameON=False
	creating_pigs()
	
	while gameLOOP:
		tries+=1
		
		# gameDisplay.fill((0,0,0))
		draw_background()
		aimer_x=100
		aimer_y=400
		aim_radius=50
		time=0
		b=bird(100,300,60)
		
		creating_obstacles()
		

		
		o2=obstacle(0,480,1000,20)
		o4=obstacle(0,0,1000,10)
		o3=obstacle(500,200,1000,20)

		aim_angle=aim_mechanics(b,100,400,50,obstacles,piggs)
		if aim_angle<=90 and aim_angle>0:
			b.theta=-aim_angle
		elif aim_angle>=180:
			b.theta=-(270+aim_angle)
		elif aim_angle<=200:
			b.theta=180+aim_angle
		else:
			b.theta=-(180-aim_angle)
		# print(aim_angle)

		b.bird_x_initial=aimer_x+aim_radius*math.cos(math.radians(aim_angle))
		b.bird_y_initial=aimer_y+aim_radius*math.sin(math.radians(aim_angle))
		gameON=True
		while gameON:
			
			# gameDisplay.fill((0,0,0))
			draw_background()
			catapult=pygame.transform.scale(catapult,(40,70))
			gameDisplay.blit(catapult,(100+50,400-20))
			text = STAT_FONT.render("score : "+str(score),1, (255,255,255))
			gameDisplay.blit(text, (10,20))
			textx = STAT_FONT.render("Tries : "+str(tries),1, (255,255,255))
			gameDisplay.blit(textx, (150,20))
			# text = STAT_FONT.render("Gen: "+str(gen),1, (255,255,255))
			# gameDisplay.blit(text, (10,620))

			
			# if b.bird_y>400:
			# 	b.bird_y=b.bird_y_initial
			# 	b.bird_x=b.bird_x_initial
			# 	time=0
			b.mover()
			
			# o3.reflector_y(b)
			for o in obstacles:
				o.draw_obs()
				o.reflector_y(b)
				o.reflector_x(b)
			for x,pig in enumerate(piggs):
				pig.drawpigs()
				if pig.collide(b)==1:
					piggs.pop(x)
					
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					pygame.quit()
					quit()
			pygame.display.update()
			if(b.bird_y>600 or b.bird_x>1300):
				gameON=False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()


gameplay()







