# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:20:21 2020

@author: MOHANA D
"""

"""Numpy Manupulation in array"""

"""Concatenate"""
#Concatenate on same dimension
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.concatenate([a,b],axis=0)
np.concatenate([a,b],axis=1)

"""Stacking"""  #only for  1-D array
a=np.array([1,2,3])
b=np.array([7,8,9])
np.stack([a,b],axis=0)
np.stack([a,b],axis=1)

"""V stack""" #column wise
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.vstack([a,b])

"""H stack""" #row wise
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.hstack([a,b])

"""Column stack"""
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.column_stack([a,b])

"""Splitting arrays"""
# np.split(array,index,axis)
# array= numpy array
# indx= int/list
# axis= 0/1
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.split(a,2,axis=0)
np.split(a,3,axis=1)
np.split(b,1,axis=0)
np.split(b,1,axis=1)
np.split(b,2,axis=0)
np.split(b,3,axis=1)

np.split(a,[1,2],axis=0) # row wise split
#the split works in this way
a[:1,]
a[1:2,]
a[2:,]

np.split(a,[1,2],axis=1) # column wise spilt
#the split works in this way
a[:,:1]
a[:,1:2]
a[:,2:]