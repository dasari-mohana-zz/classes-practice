"""if... else"""
a=45
b=32
if a>b:                   #if statment close by":"
    print("a is greater") #we should give atleast one space for print statement 
else:                     #else statment close by":"
    print("b is greater")    

a=5
b=6
if a==b:
    print("a and b are equal")
else:
    print("a and b are not equal")
    
"""if..elif..else""" 
a=float(input("give 'a' value:"))
b=float(input("give 'b' value:"))
if a>b:
    print("a is greater")
elif a==b:  #The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
    print("a and b are equal")
else :      #else should not give any condition
    print("b is greater")
    
"""one line code for if else"""
a=45
b=78
print("a is greater") if a>b else print("b is greater")

"""multiple else statements on the same line"""
a=float(input("give 'a' value:"))
b=float(input("give 'b' value:"))
print("a is greater") if a>b else print("a equals b") if a==b else print("b is greater")

"""using "and in if statements"""
a=50
b=34
c=99
if a>b and c>a:
    print("both conditions are true")
    
"""using 'or' in if statements"""
a=45
b=56
c=23
if a>b or a>c:
    print("any one is true")

"""Nested If"""
a=float(input("enter 'a' value:"))
if a>10:          #this is main if
    print("a is above 10")
    if a>30:        #this is nested if
        print("a is also above 30")
    if a<100:       #this is nested if
        print("a is below 100")
    else:           #this is nested else 
        print("a is below 30")
else:            #this is main else which related to main if
    print("a is below 10")
"""While Loop"""
#With the while loop we can execute a set of statements as long as a condition is true.
i=0 #intilization
while i<10: #condition
    i=i+1   #increment or decrement (output: 1 to 10)
    print(i) 
    
i=0 #intilization
while i<10: #condition
    print(i)
    i=i+1   #increment or decrement (output: 0 to 9)

"""Break statement"""
#With the break statement we can stop the loop even if the while condition is true
i=0 #intilization
while i<10: #condition
    i=i+1 #increment or decrement 
    if i==7:
        break
    print(i) #(output: 1 to 6)
    
i=0 #intilization
while i<10: #condition
     
    if i==7:
        break
    print(i)
    i=i+1 #increment or decrement   #(output: 0 to 6)

"""Continue statement"""
i=0 #intilization
while i<10: #condition
    i=i+1 #increment or decrement 
    if i==7: #only 7 will not be shown in output
        continue
    print(i)      #output : it gives from 1to 6 and 7 will break and continue from 8 to 10
    
i=0 #intilization
while i<10: #condition 
    if i==7:
        continue
    print(i)
    i=i+1 ##increment or decrement #output: 0 to 6
    
"""else Statement"""
#With the else statement we can run a block of code once when the condition no longer is true
i=0 #intilization
while i<10: #condition
    print(i) 
    i=i+1  #increment or decrement
else:
    print("i is no longer less than 10")