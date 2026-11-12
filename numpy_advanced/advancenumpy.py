#difference beetween python list and numpy array

#speed memory
import time
a=[i for i in range(100)]
b=[i for i in range(100,200)]
c=[]
start=time.time()
for i in range(len(a)):
	c.append(a[i]+b[i])

print(time.time()-start)
import numpy as np
t=np.arange(100,dtype=np.int16)
d=np.arange(100,200,dtype=np.int16)
start=time.time()
e=t+d
print(time.time()-start)

f=3.0040/1.4305
print(f)

#memory
import sys
print(sys.getsizeof(c))
print(sys.getsizeof(e))

#Advanced indexing
#1. fancy indexing
#2. boolean indexing
a1=np.arange(9).reshape(3,3)
print(a1[[0,1]])

print("the array is :",a1[a1>5])

q=np.random.randint(1,10,5)
print(q)

#working with mathematical formulas

#sigmoid  mean square error
def sigmoid(array):
	return 1/(1+np.exp(-array))

c1=sigmoid(a1)
print(c1)

actual=np.random.randint(1,15,10)
expected=np.random.randint(1,15,10)

def mse(actual,expected):
	return np.mean((actual-expected)**2)
print(mse(actual,expected))

#working with missing value

a=[1,2,3,np.nan,6]
arr=np.array(a)
v=arr[~np.isnan(arr)]
print(v)

#graph plotting

import matplotlib.pyplot as plt
x=np.linspace(-10,10,50)
y=x**2
plt.plot(x,y)
plt.show()
