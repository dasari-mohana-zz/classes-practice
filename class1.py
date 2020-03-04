print("hello world")

print("c")

#casting int,float,string
#int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#string
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
#convertion of int,float,complex
x = 1 # int
y = 2.8 # float
z = 1j # complex
#convert int to float
a = float(x)
type(a)
#convert from float to int:
b = int(y)
type(b)
#convert from int to complex:
c = complex(x)
type(c)
#types and Id's
b=66
type(b)
a=2.9
type(a)
id(b)
c=a+b
type(c)
id(c)

#listing
l=(1,2,3)
l1=list((1,2,3))
l2=list({1,2,3})
l3=list(1,2,3)
#bool
a=1
bool(a)
b=0
bool(b)
c=101
bool(c)
d=10.0
bool(d)
e="a"
bool(e)
#strings
a='dasari'
type(a)
a = '''Lorem ipsum dolor sit amet,
con'''
print(a)
#divison
a=11/2
b=11//2
c=-11/2
d=-11//2
e=-22//3
f=-22/3
#boolen true & false
#true statements
bool(1)
bool("abc")
bool(True)
bool(123)
bool(["apple", "cherry", "banana"])
print(10 > 9)

#false statements
bool()
bool(None)
bool(False)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(11<5)

x = "Hello"
y = 15

print(bool(x))
print(bool(y))




