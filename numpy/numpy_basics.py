#creation of numpy array


import numpy as np

d1=np.array([1,2,3,4,5,6,7,8,9,2],dtype=float)     #1D
d2=np.array([[1,2],[2,3]])    #2D
d3=np.array([[[1,2],[2,3]],[[4,5],[6,7]]])   #3D

a1=np.arange(10)
a2=np.arange(9).reshape(3,3)
a3=np.arange(27).reshape(3,3,3)
a4=np.arange(1,11,2)

c1=np.ones((3,3))
c2=np.zeros((3,3))
c3=np.random.random((3,3))
c4=np.identity(3)
c5=np.linspace(-10,10,10)

"""print(d1)
print(d2)
print(d3)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

print(a1)
print(a2)
print(a3)
print(a4)"""

#array atributes

print(a1.ndim)
print(a2.ndim)      #It will show the dimensions
print(a3.ndim)

print(a1.size)
print(a2.size)      #It will give the size of array basically product of no of row and column
print(a3.size)

print(a1.itemsize)
print(a2.itemsize)  #It will give how much datatype takes memory in bytes
print(a3.itemsize)


print(a1.shape)
print(a2.shape)    #It will give no of rows and no of col
print(a3.shape)

print(a1.dtype)
print(a2.dtype)    #It will show dtype
print(a3.dtype)


#changing datatype

data=a3.astype(np.int32)
print(data.dtype)

#scaler operations

print(a1+d1)
print(a1*d1)
print(a1/d1)
print(a1**d1)
print(a1%d1)
print(a1>5)
print(a1==d1)
print(a1*2)

#array functions

print(np.round(a1*10))
print(np.floor(d1*10))
print(np.ceil(d1*10))

print(np.mean(a1))
print(np.mean(d1))
print(np.median(d1))
print(np.std(d1))
print(np.var(d1))
print(np.max(d1))

print(np.min(a2,axis=1))

e1=np.array([[2,4],[3,6]])
e2=np.array([[7,2],[4,2]])

print(np.dot(e1,e2))
print(np.log(e1))
print(np.exp(e1))

#indexing and slicing

print(a1[0])
print(a2[1,2])
print(a3[2,2,2])

print(a1[2:5])
print(a2[::2,::2])
print(a2[0,:])
print(a2[:,2])


#iteration

for i in a1:
        print(i)

for i in a2:
        print(i)

for i in a3:
        print(i)

for i in np.nditer(a2):
        print(i)

#reshaping

print(np.transpose(a2))
print(np.ravel(a2))

#stacking

print(np.hstack(a2))
print(np.hstack(a2))
print(np.vstack(a2))

#splitting

print(np.hsplit(a2,3))
print(np.vsplit(a2,3))


