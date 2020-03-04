# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:00:13 2020

@author: MOHANA D
"""

"""Functions"""
def f1():
    print("orange")
def f2(arg1,arg2): #<function __main__.f2(arg1, arg2)>
    print("mango")
    
f3(1,2)   #only if we give the argugments then only the function will perform
def f3(arg1,arg2):
    c=arg1*arg2
    print(c)   #output: 2 and white
    print("white")
  
re=f3(1,2) #cannot assign the function
print(re) #output will be none

def f3(arg1,arg2):
    c=arg1*arg2
    print(c)  
    print("white")
    return(c) #return() is used to get the under function value outside and return the value
re=f3(1,2)
print(re)

def f3(arg1,arg2):
    c=arg1*arg2
    d=arg1/arg2
    print(c)
    print(d)
    return(c)
    return(d) #the output of d is not shown since the function runs till return(c) 
re=f3(1,2)
print(re)

def f3(arg1,arg2):
    c=arg1*arg2
    d=arg1/arg2
    print(c)
    print(d)
    return(c,d) #the output gives both c and d since we gave the return(c,d)    
re=f3(1,2)
print(re)
type(re) #tuple
"""using if else statements"""
def f3(arg1,arg2):
    c=arg1*arg2
    d=arg1/arg2
    if arg1==1:
        return(c)
    else:
        return(d,c)
        print("white")
re=f3(2,2)

def f3(arg1,arg2):
    c=arg1*arg2
    d=arg1/arg2
    if arg1==1:
        return(c)
    else:
        return(list((d,c)))
        print("white")
re=f3(2,2)
type(re)
"""using add() function"""
def add(i,j,k):
    return(i+j+k)
add(2,3,4) #the corresponding values will be added

def add(i,j,k):
    return(i+j+k)
add(i=2,j=3,k=4)

def add(i,j,k):
    return(i+j+k)
add(i=2,j=3,8)  #positional argument follows keyword argument #errror will occur , either give i,j,k values or don't specify the i,j,k  
    
def add(i,j,k):
    return(i+j+k)
add(i=1,k=2,3) #position error

def add(j,k,i): #it follows the j,k,i order
    print(i) #i=6
    print(j) #j=3
    print(k) #k=5
    return(i+j+k)
add(3,5,6)
    