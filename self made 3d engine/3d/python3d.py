
import pygame
import random
import numpy as np 
import math




class p3d:


	def __init__(self,width,height,gameDisplay):

		self.rotateX=0
		self.rotateY=0
		self.rotateZ=0
		self.width=width
		self.height=height
		self.key_x_rot=0
		self.key_y_rot=0
		self.key_z_rot=0
		self.prevx=0
		self.rotator=0
		self.scale=1
		self.gameDisplay=gameDisplay
	def translate(self,point,pos):
		x,y,z=pos
		np_point=np.array(point)
		new_point=np.zeros(np_point.shape)
		for i,p in enumerate(point):

			
			new_point[i][0]=p[0]+x 
			new_point[i][1]=p[1]+y 
			new_point[i][2]=p[2]+z

		return new_point





	def Create_Rot_Mat(self,alpha,beta,gamma):

		rotX=[[1,0,0],
			  [0,math.cos(alpha),-math.sin(alpha)],
			  [0,math.sin(alpha),math.cos(alpha)]]

		rotY=[[math.cos(beta),0,math.sin(beta)],
			  [0,1,0],
			  [-math.sin(beta),0,math.cos(beta)]]

		rotZ=[[math.cos(gamma),-math.sin(gamma),0],
			  [math.sin(gamma),math.cos(gamma),0],
			  [0,0,1]]

		rotX=np.array(rotX)

		rotY=np.array(rotY)

		rotZ=np.array(rotZ)

		RotationMat=np.matmul(rotX,np.matmul(rotY,rotZ))

		return RotationMat



	def Point_Rotation(self,point,alpha,beta,gamma):
		
		point_array=np.array([
			                  [point[0]],
							  [point[1]],
							  [point[2]]
								])
							  

		RotMat=self.Create_Rot_Mat(alpha,beta,gamma)
		
		result =np.matmul(RotMat,point_array)

		return [result[0][0],result[1][0],result[2][0]]


	def rotate_axis(self,totalpoints,speed_in_direction):

		for i,point in enumerate(totalpoints):

			alpha=speed_in_direction[0]
			beta=speed_in_direction[1]
			gamma=speed_in_direction[2]

			totalpoints[i]=self.Point_Rotation(point,alpha,beta,gamma)


		return totalpoints


	def draw_poly(self,points,color,fill_colors=(0,0,0),fill=False):
		first_point=points[0]
		last_point=points[0]
		if fill:
			fill_points=self.eliminate_diamention(points)
			fill_points=tuple(map(tuple,fill_points))
			pygame.draw.polygon(self.gameDisplay,fill_colors,fill_points)

		for i in range(1,len(points)):
			pygame.draw.line(self.gameDisplay,color,(first_point[0],first_point[1]),(points[i][0],points[i][1]))
			first_point=points[i]

		pygame.draw.line(self.gameDisplay,color,(first_point[0],first_point[1]),(last_point[0],last_point[1]))




	def eliminate_diamention(self,arr):
		new_arr=np.zeros((np.array(arr).shape[0],np.array(arr).shape[1]-1))
		for i in range(len(arr)):
			new_arr[i][0]=arr[i][0]
			new_arr[i][1]=arr[i][1]

		return new_arr

	def cube(self,size,pos,color,axis=(0,0,0),rotspeed=(0,0,0),fill=False,color_arr=[],auto_rotate=False):
		

		point=[(pos[0]-size/2,pos[1]-size/2,pos[2]+size/2),(pos[0]+size/2,pos[1]-size/2,pos[2]+size/2),
			   (pos[0]+size/2,pos[1]+size/2,pos[2]+size/2),(pos[0]-size/2,pos[1]+size/2,pos[2]+size/2),
			   (pos[0]-size/2,pos[1]-size/2,pos[2]+size/2),

			   (pos[0]-size/2,pos[1]-size/2,pos[2]-size/2),(pos[0]+size/2,pos[1]-size/2,pos[2]-size/2),
			   (pos[0]+size/2,pos[1]-size/2,pos[2]+size/2),(pos[0]+size/2,pos[1]+size/2,pos[2]+size/2),
			   (pos[0]+size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]+size/2,pos[1]-size/2,pos[2]-size/2),
			   (pos[0]-size/2,pos[1]-size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]+size/2,pos[2]-size/2),
			   (pos[0]+size/2,pos[1]+size/2,pos[2]-size/2),

			   (pos[0]-size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]+size/2,pos[2]+size/2)]

		face5=[(pos[0]-size/2,pos[1]-size/2,pos[2]+size/2),(pos[0]+size/2,pos[1]-size/2,pos[2]+size/2),
		       (pos[0]+size/2,pos[1]-size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]-size/2,pos[2]-size/2),
		       (pos[0]-size/2,pos[1]-size/2,pos[2]+size/2)]
		face2=[(pos[0]+size/2,pos[1]-size/2,pos[2]+size/2),(pos[0]+size/2,pos[1]+size/2,pos[2]+size/2),
				(pos[0]+size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]+size/2,pos[1]-size/2,pos[2]-size/2),
				(pos[0]+size/2,pos[1]-size/2,pos[2]+size/2)]

		face3=[(pos[0]+size/2,pos[1]-size/2,pos[2]-size/2),(pos[0]+size/2,pos[1]+size/2,pos[2]-size/2),
				(pos[0]-size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]-size/2,pos[2]-size/2),
				(pos[0]+size/2,pos[1]-size/2,pos[2]-size/2)]

		face4=[(pos[0]-size/2,pos[1]-size/2,pos[2]+size/2),(pos[0]-size/2,pos[1]-size/2,pos[2]-size/2),
				(pos[0]-size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]+size/2,pos[2]+size/2),
				(pos[0]-size/2,pos[1]-size/2,pos[2]+size/2)]

		face6=[(pos[0]-size/2,pos[1]+size/2,pos[2]+size/2),(pos[0]+size/2,pos[1]+size/2,pos[2]+size/2),
				(pos[0]+size/2,pos[1]+size/2,pos[2]-size/2),(pos[0]-size/2,pos[1]+size/2,pos[2]-size/2),
				(pos[0]-size/2,pos[1]+size/2,pos[2]+size/2)]
		point=list(map(list,point))
		
		if auto_rotate:
			point=self.rotate_axis(point,(self.rotateX,self.rotateY,self.rotateZ))
		else:
			point=self.rotate(point,(rotspeed[0],rotspeed[1],rotspeed[2]))
		point=self.translate(point,axis)

		if fill:
			# =====================================================================
			if auto_rotate:
				face5=self.rotate_axis(face5,(self.rotateX,self.rotateY,self.rotateZ))
			else:
				face5=self.rotate(face5,(rotspeed[0],rotspeed[1],rotspeed[2]))
			face5=self.translate(face5,axis)

			if auto_rotate:
				face2=self.rotate_axis(face2,(self.rotateX,self.rotateY,self.rotateZ))
			else:
				face2=self.rotate(face2,(rotspeed[0],rotspeed[1],rotspeed[2]))

			face2=self.translate(face2,axis)

			if auto_rotate:
				face3=self.rotate_axis(face3,(self.rotateX,self.rotateY,self.rotateZ))
			else:
				face3=self.rotate(face3,(rotspeed[0],rotspeed[1],rotspeed[2]))
			face3=self.translate(face3,axis)

			if auto_rotate:
				face4=self.rotate_axis(face4,(self.rotateX,self.rotateY,self.rotateZ))
			else:
				face4=self.rotate(face4,(rotspeed[0],rotspeed[1],rotspeed[2]))
			face4=self.translate(face4,axis)

			if auto_rotate:
				face6=self.rotate_axis(face6,(self.rotateX,self.rotateY,self.rotateZ))
			else:
				face6=self.rotate(face6,(rotspeed[0],rotspeed[1],rotspeed[2]))
			face6=self.translate(face6,axis)
			# ======================================================================
			face1=self.eliminate_diamention(point[0:5])
			face1=tuple(map(tuple,face1))
			#////////////////////////////////////////////////////
			face5=self.eliminate_diamention(face5)
			face5=tuple(map(tuple,face5))

			face2=self.eliminate_diamention(face2)
			face2=tuple(map(tuple,face2))

			face3=self.eliminate_diamention(face3)
			face3=tuple(map(tuple,face3))

			face4=self.eliminate_diamention(face4)
			face4=tuple(map(tuple,face4))

			face6=self.eliminate_diamention(face6)
			face6=tuple(map(tuple,face6))

		#////////////////////////////////////////////////////
		if fill:
			
			pygame.draw.polygon(self.gameDisplay,color_arr[1],face2)
			pygame.draw.polygon(self.gameDisplay,color_arr[2],face3)
			pygame.draw.polygon(self.gameDisplay,color_arr[3],face4)
			pygame.draw.polygon(self.gameDisplay,color_arr[4],face5)
			pygame.draw.polygon(self.gameDisplay,color_arr[5],face6)
			pygame.draw.polygon(self.gameDisplay,color_arr[0],face1)

		#////////////////////////////////////////////////////

		self.draw_poly(point,color)

		self.rotateX+=rotspeed[0]
		self.rotateY+=rotspeed[1]
		self.rotateZ+=rotspeed[2]

	def cuboid(self,size,pos,color,axis,rotspeed=(0,0,0),auto_rotate=False):
		point=[(pos[0]-size[0]/2,pos[1]-size[1]/2,pos[2]+size[2]/2),(pos[0]+size[0]/2,pos[1]-size[1]/2,pos[2]+size[2]/2),
			   (pos[0]+size[0]/2,pos[1]+size[1]/2,pos[2]+size[2]/2),(pos[0]-size[0]/2,pos[1]+size[1]/2,pos[2]+size[2]/2),
			   (pos[0]-size[0]/2,pos[1]-size[1]/2,pos[2]+size[2]/2),

			   (pos[0]-size[0]/2,pos[1]-size[1]/2,pos[2]-size[2]/2),(pos[0]+size[0]/2,pos[1]-size[1]/2,pos[2]-size[2]/2),
			   (pos[0]+size[0]/2,pos[1]-size[1]/2,pos[2]+size[2]/2),(pos[0]+size[0]/2,pos[1]+size[1]/2,pos[2]+size[2]/2),
			   (pos[0]+size[0]/2,pos[1]+size[1]/2,pos[2]-size[2]/2),(pos[0]+size[0]/2,pos[1]-size[1]/2,pos[2]-size[2]/2),
			   (pos[0]-size[0]/2,pos[1]-size[1]/2,pos[2]-size[2]/2),(pos[0]-size[0]/2,pos[1]+size[1]/2,pos[2]-size[2]/2),
			   (pos[0]+size[0]/2,pos[1]+size[1]/2,pos[2]-size[2]/2),

			   (pos[0]-size[0]/2,pos[1]+size[1]/2,pos[2]-size[2]/2),(pos[0]-size[0]/2,pos[1]+size[1]/2,pos[2]+size[2]/2)]

		point=list(map(list,point))
		if auto_rotate:
			point=self.rotate_axis(point,(self.rotateX,self.rotateY,self.rotateZ))
		else:
			point=self.rotate(point,(rotspeed[0],rotspeed[1],rotspeed[2]))
		point=self.translate(point,axis)

		self.draw_poly(point,color)

		self.rotateX+=rotspeed[0]
		self.rotateY+=rotspeed[1]
		self.rotateZ+=rotspeed[2]

	def flipY(points):
		new_points=np.zeros(np.array(points).shape)
		for i in range(new_points.shape[0]):
			new_points[i][1]=-points[i][1]



		return new_points
	def flipX(points):
		new_points=np.zeros(np.array(points).shape)
		for i in range(new_points.shape[0]):
			new_points[i][0]=-points[i][0]



		return new_points
	def flipZ(points):
		new_points=np.zeros(np.array(points).shape)
		for i in range(new_points.shape[0]):
			new_points[i][2]=-points[i][2]



		return new_points

	def trans_rotate(self,points,rotation,axis):
		test_point=self.rotate_axis(points,rotation)
		test_point=self.translate(test_point,axis)
		return test_point
	def top_scale(self,points):


		np_point=np.array(point)
		new_points=np.zeros(np_point.shape)
		
			
		new_points=points
		

		return new_points 

	def scale(self,points,scales):
		x_scale,y_scale,z_scale=scales
		np_point=np.array(point)
		new_points=np.zeros(np_point.shape)
		
			
		new_points=points
		for i in range(new_points.shape[0]):
			new_points[i][0]*=x_scale
			new_points[i][1]*=y_scale
			new_points[i][2]*=z_scale

		

		return new_points 



	def create_space(self,surfaces,colors=[(255,255,255)],keys=[pygame.K_RIGHT,pygame.K_UP,pygame.K_a,pygame.K_LEFT,pygame.K_DOWN,pygame.K_s],z_extrema=2000,fill_colors=[(0,0,0)],rotation=(0,0,0),axis=(0,0,0),space_translate=(100,100,0)):
		
		m_pos_x,m_pos_y=pygame.mouse.get_pos()
		m_pos_x,m_pos_y=m_pos_x-self.width/2,m_pos_y-self.height/2
		moving=False
		if self.prevx!=m_pos_x:
			moving=True
			self.prevx=m_pos_x



		for x,points in enumerate(surfaces):
			
			points=np.array(points,dtype="float64")
			points*=self.scale
			points=self.key_translate(keys,points,translate_from=(space_translate[0],space_translate[1],space_translate[2]))
			
			points=self.rotate(points,(-(m_pos_y/self.height)*math.pi,-(m_pos_x/self.width)*math.pi,0))
			draw=True
			for p in points:
				if p[2]>z_extrema:
					draw=False
					break
			if draw:
				self.draw_poly(points,colors[x],fill_colors=fill_colors[x],fill=True)


	def rotate(self,points,rotation):
		totalpoints=np.zeros(np.array(points).shape)
		for i,point in enumerate(points):

			alpha=rotation[0]
			beta=rotation[1]
			gamma=rotation[2]

			totalpoints[i]=self.Point_Rotation(point,alpha,beta,gamma)


		return totalpoints

	def key_translate(self,keys,points,translate_from=(0,0,0),speed=(0.5,0.5,0.1)):

		pressed_key=pygame.key.get_pressed()
	
		if pressed_key[keys[0]]:
			
			self.key_x_rot+=speed[0]
		if pressed_key[keys[1]]:
			
			self.key_y_rot+=speed[1]
		if pressed_key[keys[2]]:
			
			self.key_z_rot+=speed[2]
			self.scale+=0.01
			

		if pressed_key[keys[3]]:
			
			self.key_x_rot-=speed[0]
		if pressed_key[keys[4]]:
			
			self.key_y_rot-=speed[1]
		if pressed_key[keys[5]]:
			
			self.key_z_rot-=speed[2]
			self.scale-=0.01
		
		points=self.translate(points,(translate_from[0]+self.key_x_rot,translate_from[1]+self.key_y_rot,translate_from[2]+self.key_z_rot))
		


		return points

	def image(self,image_obj,pos,width,height,corner_depth=(0,0,0),rotation=(0,0,0)):
		d=corner_depth
		points=self.rotate([pos,[pos[0]+width,pos[1],d[0]],[pos[0]+width,pos[1]+height,d[1]],[pos[0],pos[1]+height,d[2]]],(rotation[0],rotation[1],rotation[2]))
		pos=points[0]
		width=abs(points[1][0]-points[0][0])
		height=abs(points[2][1]-points[0][1])

		image_obj=pygame.transform.scale(image_obj,(int(width),int(height)))
		self.gameDisplay.blit(image_obj,(int(pos[0]),int(pos[1])))

	
	def image_space(self,images,positions,keys=[pygame.K_RIGHT,pygame.K_UP,pygame.K_a,pygame.K_LEFT,pygame.K_DOWN,pygame.K_s],z_extrema=2000,rotation=(0,0,0),axis=(0,0,0),space_translate=(100,100,0)):

		m_pos_x,m_pos_y=pygame.mouse.get_pos()
		m_pos_x,m_pos_y=m_pos_x-self.width/2,m_pos_y-self.height/2
		


		for x,points in enumerate(positions):
			
			points=np.array(points,dtype="float64")
			points*=self.scale
			points=self.key_translate(keys,points,translate_from=(space_translate[0],space_translate[1],space_translate[2]))
			
			points=self.rotate(points,(-(m_pos_y/self.height)*math.pi,-(m_pos_x/self.width)*math.pi,0))
			draw=True
			for p in points:
				if p[2]>z_extrema:
					draw=False
					break
			if draw:
				
				width=int(abs(points[1][0]-points[0][0]))
				height=int(abs(points[2][1]-points[1][1]))
				image=pygame.transform.scale(images[x],(width,height))
				self.gameDisplay.blit(image,(points[0][0],points[0][1]))
	
