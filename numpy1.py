
import numpy.matlib
import numpy as np
x=int(input("请随机输入1到100的整数"))

np.random.seed(612)
random2=np.linspace(x,1000,int(1000/x))
random1 = np.random.rand(int( 1000/x))
print("序号  索引值    随机数")
for i in range(int (1000/x)):
  print(i,end=" ")
  print(random2[i:i+1],end=" ")
  print(random1[i:i+1],end=" ")
  print(" ")
  




