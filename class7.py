# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:49:55 2020

@author: MOHANA D
"""
"""Zip"""
#The purpose of zip() is to map the similar index of multiple containers 
#so that they can be used just using as single entity.
name = [ "mohana", "krishna", "dasari", "nani" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ]
x=zip(name,roll_no,marks)
y=list(x)  #the zip value should be listed
print(y)

for i in y: #this for loop is used for line by line output
    print(i)
##############################################################################   
"""Unzip"""
name = [ "mohana", "krishna", "dasari", "nani" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ]
x=zip(name,roll_no,marks)
y=list(x)  #the zip value should be listed
print(y)
#unzipping
namz,roll_noz,marksz=zip(*y) #we are unzipping the zipped values of "y" which is listed

print(namz)
print(roll_noz)
print(marksz)

#example of zip() with for loop
students=("a","b","c","d")
marks=(85,96,74,56)
for stu,mar in  zip(students,marks):
    print("student: %s marks:%s"%(stu,mar))
    #print(stu,mar)
#####################################################################################    
"""Enumerate"""
'''A lot of times when dealing with iterators, 
we also get a need to keep a count of iterations. 
Python eases the programmers’ task by providing a built-in function enumerate() for this task.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
'''
name = [ "mohana", "krishna", "dasari", "nani" ]
x=enumerate(name)
y=list(x) #convert enumerate into list
print(y)

name = [ "mohana", "krishna", "dasari", "nani" ]
x=enumerate(name,4) #the number is given to change the default counter & the indexing starts from given number
y=list(x) #convert enumerate into list
print(y)

name = [ "mohana", "krishna", "dasari", "nani" ]
x=enumerate(name,-2) #the number is given to change the default counter & the indexing starts from given number
y=list(x) #convert enumerate into list
print(y)

# Looping Over an Enumerate
for i in enumerate(name):
    print(i)
    
for a,i in enumerate(name):
    print(a,i)
    
for a,i in enumerate(name,3):
    print(a,i)
    
 #############################################################################   
"""Lexical closures"""

def f(x):
    def g(y):
        return x+y
    return g

f(x=3)(y=2)
#==================
def f(x):
    def g(y):
        return x+y
    return x+y #this shows error as y is not defined in f(x) function
f(x=3)(y=2)