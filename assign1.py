"""Dasari Mohan Krishna--Assignment1-- 19/02/2020"""

#Write a program to perform input/output of aall basic data types
x=3 #x is int
y=4.8 #y is float
z="dasari" #z is string
a=7j #a is complex
b=["tv","phone","laptop"] #b is list
c=("tv","phone","laptop") #c is tuple
d={"tv","phone","laptop"} #d is set
e=range(5) #e is range
f=bool(2) #f is boolen
print(x,y,z,a,b,c,d,e,f)
print(type(x),type(y),type(z),type(a),type(b),type(c),type(d),type(e),type(f))

#write a program to enter two numbers and their sum
x=4
y=8
z=x+y #used '+' operator
print(z)

#write a program to enter two numbers and perform all arithemetic operations
x=5
y=3
a=x+y #addition
b=x-y #subtraction
c=x*y #Multiplication
d=x/y #Division
e=x//y#Floor division
f=x%y #modulus
g=x**y #power
print(a,b,c,d,e,f,g)

#write a program to enter length and breadth of rectangle and find its perimeter
l=float(input("enter length value:"))#l=length
b=float(input("enter breath value:"))#b=breadth
p=(2*l)+(2*b) #p is perimeter
print(p)

#write a program to enter length and breadth of rectangle and find its area
l=float(input("enter length value:")) #l=length
b=float(input("enter breath value:")) #b=breadth
a=l*b #a is area
print(a)

#write a program to enter radius of circle and find its diameter,circumference,and area
r=float(input("enter radius of the circle:")) #r=radius
d=2*r #d is diameter
c=2*3.14*r #c is circumference
a=3.14*(r**2) #a is area
print(d)
print(c)
print(a)

#wite a program to length in centimeter and convert into meter and kilometer
cm=float(input("enter value:")) #cm is centimeter
m=cm/100                        #m is meter
km=cm/(1000*100)                #km is kilometer
print(m)
print(km)

#write a program to enter temperature in celcius and convert into fahrenheit
c=float(input("enter temperature in celcius:")) #c is celcius
f=(c*1.8)+32 #f is farenheit
print(f)

#write a program to enter temperature in fahrenheit and convert into celcius
f=float(input("enter temperature in fahrenheit:")) #f is farenheit
c=(f-32)/1.8 #c is celcius
print(c)

#write a program to convert days into years, weeks and days
d=float(input("enter no.of days:")) #days
y=d/365 #y=years
w=d/7 #w=weeks
print(y)
print("years=",y,"weeks=",w,"days=",d)

#write a program to find power of any number
x= float(input("enter base number:")) #base number
y=float(input("enter power:")) #power number
z=x**y
print(z)

#write a program to enter any number and calcute its square root
x=float(input("enter number:"))
y=x**0.5
print("squre root of number is",y)

#write a program to enter two angles of triangle and find third angle
a=float(input("enter first angle value:"))
b=float(input("enter second angle value:"))
c=180-(a+b)
print("thrid angle is:",c)

#write a program to enter base and height of atraingle and find its area
h=float(input("enter height value:"))
b=float(input("enter base value:"))
a=(b*h)/2
print("area:",a)

#write a program to calculate area of an equilateral triangle
import math
x=float(input("enter side value:"))
y=(math.sqrt(3)/4)*(x**2)
print("area of equilateral triangle:",y)

#write a program to enter marks of five subjects and calculate total,average and percentage
a=float(input("enter english marks:"))
b=float(input("enter physics marks:"))
c=float(input("enter biology marks:"))
d=float(input("enter maths marks:"))
e=float(input("enter social marks:"))
t=a+b+c+d+e
avg=t/5
per=(t/500)*100
print("total:",t,"average",avg,"percentage%:",per)

#write a program to P,T,R and calculate simple interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
SI=(p*t*r)/100 #simple interest=(P*T*R)/100
print("simple interest:",SI)

#write a program to P,T,R and calculate compound interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
CI=p*(1+r/100)**t #compound interest=P(1+1/r)^t
print("compound interest:",CI)