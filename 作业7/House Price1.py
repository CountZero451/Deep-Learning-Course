import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
TRAIN_URL="http://download.tensorflow.org/data/iris_training.csv"
train_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)
# df =pd.read_csv("C:\\Users\\OnlyS\\Desktop\\神经网络作业\\作业7\\data\\boston.csv",header=0)
#print(df.describe())
#x=tf.placeholder(tf.float32,[None,12],name="X")
#y=tf.placeholder(tf.float32,[None,1],name="Y")
# def model(x,w,b):
#     return tf.matmul(x,w)+b

# W=tf.Variable(tf.random.normal([12,1],mean=0.0,stddev=1.0,dtype=tf.float32))
# B=tf.Variable(tf.zeros(1),dtyoe=tf.float32)
# print(W)
# print(B)

#训练
# training_epochs=50
#学习率
# learning_rate=0.01
# batch_size=10

# def loss(x,y,w,b):
#    err=model(x,w,b)-y
#    squared_err=tf.square(err)
#    return tf.reduce_mean(squared_err)

# def grad(x,y,w,b):
#     with tf.GradientTape() as tape:
#         loss_=loss(x,y,w,b)
#     return tape.gradient(loss_,[w,b]) 

# optimizer=tf.keras.optimizers.SGD(learning_rate)
COLUMN_NAMES=['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']
df_iris=pd.read_csv(train_path,names=COLUMN_NAMES,header=0)

iris=np.array(df_iris)

fig=plt.figure('Iris Data',figsize=(15,15))

fig.suptitle("Anderson's Iris Data Set\n(Blue->Setosa | Red->Versicolor | Green->Virginica)")
for i in range(4):
    for j in range(4):
        plt.subplot(4,4,4*i+(j+1))
        if(i==j):
            plt.hist(iris[:,j], align= 'mid', color='blue',edgecolor='green')
        else:
            plt.scatter(iris[:,j],iris[:,i],c=iris[:,4],cmap='brg')
        if(i==0):
            plt.title(COLUMN_NAMES[j])
        if(j==0):
            plt.ylabel(COLUMN_NAMES[i])
plt.tight_layout(rect=[0,0,1,0.93])

plt.show()
