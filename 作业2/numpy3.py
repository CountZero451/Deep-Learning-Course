import numpy as np
import copy as cp

x0=np.zeros(10)
x1=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,166.03]
x2=[2,3,4,2,3,4,2,4,1,3]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
X=np.mat([x0,x1,x2],dtype=float)
Y=np.mat(y)
X=X.T
Y=Y.T
W=X.I*X.T.I*X.T*Y
print(type(W))
print(X)
print(Y)
print(W)