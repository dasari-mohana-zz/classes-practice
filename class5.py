# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:42:26 2020

@author: MOHANA D
"""
"""Funtions"""
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
def my_function():
  print("Hello from a function")
my_function() #calling the function using ()

"""Arguments"""
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses.
#we can add as many arguments as we want, just separate them with a comma ','.
#The following example has a function with one argument (fname). 
#When the function is called, we pass along a first name, which is used inside the function to print the full name:
def function(fname):
    print(fname)
function("dasari")
#we can also add other functions
def function(fname):
    print(fname+" dasari")
function("mohana") #output:mohana dasari
function("krishna") #output:krishna dasari
#Arguments are often shortened to args in Python documentations.
#The terms parameter and argument can be used for the same thing: information that are passed into a function
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that are sent to the function when it is called.
#a function must be called with the correct number of arguments. 
#Meaning that if our function expects 2 argmts,we have to call the function with 2 argmts,not more,and not less.
def function(fname1,fname2):
    print(fname1+" "+fname2) #" " used for space
function("mohana","krishna")
"""Arbitrary Arguments, *args"""
#If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition.
#this way the function will receive a tuple of arguments, and can access the items accordingly:
def function(*kids):
    print("my son name is ",kids[2])
function("sakhi","nani","kalki") #output: my son name is kalki
#we can also send arguments with the key = value syntax.
def function(fname1,fname2,fname3):
    print("my son name is "+fname3)
function("sakhi","kalki","nani")

#If the number of keyword arguments is unknown, add a double ** before the parameter name
def function(**kids):
    print("my son name is ",kids["fname2"])
function(fname1="sakhi",fname2="nani",fname3="kalki")

#Default Parameter Value
def function(country = "india"):
  print("I am from " + country)
function()  #executes even the function is called without argument
function("italy")

#Passing a List as an Argument
#we can send any data types of argument to a function (string, number, list, dictionary etc) 
#and it will be treated as the same data type inside the function.
def function(food):
    for i in food:
        print(i)
fruits=["apple","mango","orange"] 
function(fruits)       

#Return value
def function(x):
    return 2*x
print(function(3))
print(function(4))
print(function(5))

"""Recursion"""
#Recursion is a common mathematical and programming concept.It means that a function calls itself. 
#This has the benefit of meaning that you can loop through data to reach a result.
def try_recursion(i):
    if(i>0):
        x=i+try_recursion(i-1)
        print(x)  #it takes as factorial form calculation
    else:
        x=0
    return x

print("\n\nRecursion Example Results")
try_recursion(3)
try_recursion(5)
try_recursion(6)

"""Lambda function"""
#A lambda function is a small anonymous function.
#lambda function can take any number of arguments, but can only have one expression.
x=lambda a: a*2
print(x(1))
print(x(5))
print(x(7))

y=lambda b: b+5
print(y(2))
print(y(3))

#A lambda function that multiplies argument a with argument b and print the result
x=lambda a,b: a+b
print(x(3,4))
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Use that function definition to make a function that always doubles the number you send in
def function(n):
    return lambda a:a/n
doubler=function(4)
print(doubler(2))
#use the same function definition to make a function that always triples the number you send in
def function(n):
    return lambda a:a*n
tripler=function(4)
print(tripler(11))

"""Arrays"""#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#An array is a special variable, which can hold more than one value at a time.
#Arrays are used to store multiple values in one single variable

cars=["audi","benz","ford"]
for x in cars:
    print(x)
#length of an array
print(len(cars))
#value of an array
print(cars[1])