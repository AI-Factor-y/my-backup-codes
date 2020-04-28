import cv2
import numpy as np



class convolution:

	def __init__(self):

		self.identity=[[0,0,0],
					   [0,1,0],
					   [0,0,0]]

		self.edge1=[[1,0,-1],
					[0,0,0],
					[-1,0,1]]

		self.edge2=[[0,1,0],
					[1,-4,1],
					[0,1,0]]

		self.edge3=[[-1,-1,-1],
					[-1,-8,-1],
					[-1,-1,-1]]

		

		#converting to numpy array
		self.identity=np.array(self.identity)
		self.edge1=np.array(self.edge1)
		self.edge2=np.array(self.edge2)
		self.edge3=np.array(self.edge3)


	def im_convertor(self,image,detect_methode):
		if detect_methode=="identity":
			arr=self.identity
		elif detect_methode=="edge1":
			arr=self.edge1
		elif detect_methode=="edge2":
			arr=self.edge2
		elif detect_methode=="edge3":
			arr=self.edge3

		conv_img=np.zeros(image.shape)

		for i in range(0,image.shape[0],3):
			for j in range(0,image.shape[1],3):

				for x in range(arr.shape[0]):
					for y in range(arr.shape[1]):
						# try for boundary
						try:
							conv_img[i+x][j+y]=image[i+x][j+y]*arr[x][y]
						except:
							pass

		return conv_img


c=convolution()
img=cv2.imread("im.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image",img_gray)
# cv2.waitKey(0)

image=c.im_convertor(img_gray,"edge3")

cv2.imshow("cvt_img",image)
 
cv2.waitKey(0)





