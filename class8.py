# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:48:34 2020

@author: MOHANA D
"""

"""Numpy"""

"""NumPy is a python library used for working with arrays.
   It also has functions for working in domain of linear algebra, fourier transform, and matrices
   NumPy was created in 2005 by Travis Oliphant. NumPy stands for Numerical Python.
##################################################################################################
## Why Use NumPy ?

(1)In Python we have lists that serve the purpose of arrays, but they are slow to process.

(2)NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

(3)The array object in NumPy is called ndarray,it provides a lot of supporting functions 
   that make working with ndarray very easy.

(4)Arrays are very frequently used in data science, where speed and resources are very important.
#################################################################################################
##Why is NumPy Faster Than Lists?

(1)NumPy arrays are stored at one continuous place in memory unlike lists, 
   so processes can access and manipulate them very efficiently.

(2)This behavior is called locality of reference in computer science.

(3)This is the main reason why NumPy is faster than lists. 
   Also it is optimized to work with latest CPU architectures.
################################################################################################
"""
import numpy
arr=numpy.array([1,2,3,5,6,8,7])
print(arr)

"""NumPy is usually imported under the np alias(as)."""
import numpy as np
arr1=np.array([5,7,2,6,36,8])
arr1
type(arr1)
#The version string is stored under __version__ attribute.
import numpy as np
print(np.__version__)

import numpy as np
arr2=np.array((1,7,3,4,16,8))
arr2
type(arr2)

"""Initilize the numpy"""
import numpy as np
aa=np.zeros((3,2))
#np.zeros(rows,colums)
print(aa)

"""Intervals in arrays"""
bb=np.arange(1,50,5)
#np.arange(rows,cloumns,interval)
print(bb)

range(0,10,0.5)  # range - float doesnt work
np.array([x/2 for x in range(0,30)]) #till 29/2 and it does not calculate 30/2
np.array([x/2 for x in range(10,20,2)])
#range(a,b,interval)

"""linspace() in arrays"""
cc=np.linspace(4,5,10)
print(cc)
cc.dtype
"""full() in numpy"""
dd=np.full((4,5),7)
#np.full((rows,colums),number to fill)
print(dd)

"""random() in numpy"""
import numpy as np
ee=np.random.random((5,3))
print(ee)

"""to convert from array to list"""
a=np.arange(0,10,3).tolist()  #use .tolist()
a
a.tolist

"""Dimensions in arrays"""
#A dimension in arrays is one level of array depth (nested arrays).
"""0-D arrays"""
#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
import numpy as np
arr3=np.array(34)
arr3
"""1-D arrays"""
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
import numpy as np
arr4=np.array([2,4,6,8])
arr4
"""2-D arrays"""
#An array that has 1-D arrays as its elements is called a 2-D array.
#These are often used to represent matrix or 2nd order tensors.
import numpy as np
arr5= np.array([[1, 2, 3], [4, 5, 6]])
print(arr5)
"""3-D arrays"""
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
import numpy as np
arr6= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr6)

#NumPy Arrays provides the ".ndim" attribute that returns 
#an integer that tells us how many dimensions the array have.
import numpy as np
arr3=np.array(34)
arr4=np.array([2,4,6,8])
arr5= np.array([[1, 2, 3], [4, 5, 6]])
arr6= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr3.ndim
arr4.ndim
arr5.ndim
arr6.ndim

"""Higher Dimensional Arrays"""
#An array can have any number of dimensions.

#When the array is created, you can define the number of dimensions by using the ndmin argument.
import numpy as np
arr7=np.array([3,5,7,2,6,4,7],ndmin=7)
arr7
arr7.ndim

"""Changing elements in arrays"""
import numpy as np
a=np.array([1,2,3])
a[1]=4
print(a)

"""numpy arrayu inspection"""
"""Shape of an array"""
#returns a tuple consisting of array dimensions. can also be used to resize an array
import numpy as np
b=np.array([[1,2,3],[4,5,6]])
b.shape  #output gives no.of rows and columns

#we can also change the rows and columns in shape
b.shape=(3,2)
b
#we can also access the values in the array
b.shape[0]
#output is 2

"""size of array"""
import numpy as np
c=np.arange(12)
c
c.size
c.dtype

"""Numpy Operations""""
#Addition #subtraction
import numpy as np
add1=np.sum([3,2])
add1

import numpy as np
x=np.array([6,7])
y=np.array([2,4])
aa=np.sum([x,y])     #give [] for addition
aa
bb=np.subtract(x,y)  #give () for subtraction
bb
bb=np.array([1,3])
#axis
cc=np.sum([aa,bb],axis=0)
cc
dd=np.sum([aa,bb],axis=1)#######
dd

ee=np.sum([[3,6],[7,5]],axis=0)  #column wise addition
ee
ff=np.sum([[4,2],[8,7]],axis=1)  #row wise addition
ff

gg=np.divide([7,9],[5,8])
gg

hh=np.divide(aa,bb)

ii=np.multiply([7,9],[5,8])
jj=np.multiply(aa,bb)

"""Other Operations"""
np.exp(aa)
np.sin(bb)
np.cos(cc)
np.sqrt(dd)
np.log(ee)

"""Aggregate Function"""
rr=[23,45,67]
np.min(rr)
np.max(rr)
np.std(rr)  #standard deviation 
np.mean(rr)
np.median(rr) 
np.average(rr)
np.corrcoef(rr)  #correlation coeffiect of array


"""Numpy Broadcasting"""
a=np.array([[1,2,3],[4,5,6]])
b=np.array([8,9,10])
np.sum([a,b])
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)

"""To plot a gragh"""
import matplotlib.pyplot as plt
x=np.arange(0,20,2)
f=np.sin(x)
f=np.cos(x)
f=np.exp(x)
plt.plot(x,f)

# Don't use this statement "import pi from numpy"
#always use this statement to imort from
from numpy import pi
y=np.linspace(0,2*pi,20)
y
f=np.sin(y)
f=np.log(y)
f=np.exp(y)

plt.plot(y,f)

"""Reshape"""
i=np.arange(1000)
i
ii=i.reshape(100,10) 
ii
ii.shape
iii=i.reshape(-10,100)
iii.shape
iii=i.reshape(-25,10)
iii.shape

iii=i.reshape(100,-10)
iii.shape