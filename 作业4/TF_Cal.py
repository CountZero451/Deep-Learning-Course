import numpy as np
import tensorflow as tf
sum1=0
sum2=0
w=0
b=0
x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,166.03]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
t_x=tf.constant(x,dtype=tf.float32)
t_y=tf.constant(y,dtype=tf.float32)


for index in range(tf.size(x)):
    sum1+= (t_x[index]-tf.reduce_mean(t_x))*(t_y[index]-tf.reduce_mean(t_y))
    sum2+=(t_x[index]-tf.reduce_mean(t_x))**2
    
w=tf.divide(sum1,sum2)
b=tf.reduce_mean(t_y)-tf.multiply(w,tf.reduce_mean(t_x))
print("w=%f,b=%f"%(w,b))
