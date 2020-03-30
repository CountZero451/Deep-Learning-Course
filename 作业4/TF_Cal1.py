import numpy as np
import tensorflow as tf
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
w=0
b=0

x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,166.03]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
t_x=tf.constant(x,dtype=tf.float64)
t_y=tf.constant(y,dtype=tf.float64)
tf.constant(w,dtype=tf.float64)
tf.constant(b,dtype=tf.float64)
n=tf.size(x)

for index in range(tf.size(x)):
    
    sum1+=(t_x[index]*t_y[index])
    sum2+=(t_x[index])**2
    sum3+=t_x[index]
    sum4+=t_y[index]

w=(n*sum1-sum1)/(n*sum2)-((sum3)**2)
b=(sum4-w*sum3)/n
print("w=%f,b=%f"%(w,b))