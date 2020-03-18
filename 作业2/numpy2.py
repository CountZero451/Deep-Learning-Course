import numpy as np
sum1=0
sum2=0
w=0
b=0
x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,166.03]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]


for index in range(10):
    sum1+=(x[index]-np.mean(x))*(y[index]-np.mean(y))
    sum2+=(x[index]-np.mean(x))**2

w=sum1/sum2
b=np.mean(y)-w*np.mean(x)

print("w=%f,b=%f"%(w,b))
