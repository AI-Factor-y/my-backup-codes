import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np

data=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=data.load_data()

x_test=tf.keras.utils.normalize(x_test,axis=1)
x_train=tf.keras.utils.normalize(x_train,axis=1)

model=tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer="adam",
		loss="sparse_categorical_crossentropy",
		metrics=['accuracy'])

model.fit(x_train,y_train,epochs=3)
# ---------------------------------------------------------------------------------

# #  save a model
# model.save('epic.model')
# new_model=tf.keras.models.load_model('epic.model')
# _____________________________________________________________-__
# ------------------------------------------------------------------


val_loss,val_acc=model.evaluate(x_test,y_test)
print(val_loss,val_acc)
prediction=model.predict(x_test)
for i in range(5):
	plt.grid(False)
	plt.imshow(x_test[i],cmap=plt.cm.binary)
	plt.xlabel("actual :" + str(y_test[i]))
	plt.title("predicted : "+str(np.argmax(prediction[i])))
	plt.show()
