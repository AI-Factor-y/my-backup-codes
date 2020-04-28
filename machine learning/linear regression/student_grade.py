import pandas as pd 
import numpy as np 
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data=pd.read_csv("student-mat.csv",sep=";")
# data=data[["G1","G2","G3","studytime","failures","absences"]]
dat=data[["romantic"]]

# print(data.head())
data=data[["G1","G2","G3","studytime","failures","absences"]]

# print(data)

predict="G3"

x=np.array(data.drop([predict],1))
y=np.array(data[predict])


best=0
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.1)
# for _ in range(1000):
# 	x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.1)
# 	linear=linear_model.LinearRegression()
# 	linear.fit(x_train,y_train)
# 	acc=linear.score(x_test,y_test)
# 	print(acc)
# 	if acc>best:
# 		best=acc
# 		with open("student.pickle","wb") as f:
# 			pickle.dump(linear,f)
print("best accuracy :",best)
pickle_in=open("student.pickle","rb")
linear=pickle.load(pickle_in)
# print("coeficient :",linear.coef_)			#slope of a n dimentional space
# print("intercept: ",linear.intercept_)	# y intercept of the line in n diamentional space
acc=linear.score(x_test,y_test)
print("accuracy",acc)
predictions=linear.predict(x_test)

for x in range(len(predictions)):
	print(predictions[x],x_test[x],y_test[x])

#ploting data
# p='G1'
# style.use("ggplot")
# pyplot.scatter(data[p],data["G3"])
# pyplot.xlabel(p)
# pyplot.ylabel("final grade")
# pyplot.show()