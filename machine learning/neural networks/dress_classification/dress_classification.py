import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import matplotlib.pyplot as plt 
import os
data=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=data.load_data()

class_names=["T-shirt","trousers","pullovers","dress","coat","sandal","shirt","sneaker","bag","ankle boot"]

# plt.imshow(train_images[0],cmap=plt.cm.binary)
# plt.show()
#shrinking the data
test_images=test_images/250
train_images=train_images/250

#creating the model
model=keras.models.load_model("model.h5")
# model=keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
# 						keras.layers.Dense(128,activation="relu"),
# 						keras.layers.Dense(10,activation="softmax")

# 						])		

# model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])


# model.fit(train_images,train_labels,epochs=5)
# model.save("model.h5")
test_loss,test_acc=model.evaluate(test_images,test_labels)
print("test accuracy : ",test_acc)
prediction=model.predict(test_images)
for i in range(5):
	plt.grid(False)
	plt.imshow(test_images[i],cmap=plt.cm.binary)
	plt.xlabel("actual :" + class_names[test_labels[i]])
	plt.title("predicted : "+class_names[np.argmax(prediction[i])])
	plt.show()
