import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
boston_housing=tf.keras.datasets.boston_housing
(train_x,train_y),(_,_)=boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT","MEDV"]
plt.figure(figsize=(12,12))
for i in range(13):
  plt.subplot(4,4,(i+1))
  plt.scatter(train_x[:,i],train_y)

  plt.xlabel(titles[i])
  plt.ylabel("Price($1000's)")
  plt.title(str(i+1)+"."+titles[i]+"- Price")

for num in range(13):
    print(str(num+1)+" -- "+titles[num])
i=int(input("请选择属性："))

plt.figure(figsize=(5,5))
plt.scatter(train_x[:,i],train_y)
plt.xlabel(titles[i])
plt.ylabel("price($1000's)")
plt.title(titles[i]+" - Price")



plt.tight_layout()
plt.suptitle("各个属性与房价的关系",x=0.5,y=1.02,fontsize=20)
plt.show()