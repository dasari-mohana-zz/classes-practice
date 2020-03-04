print("hello world")

print("c")


a=6
if a>5:
    print("5 is big")
    
x = 5
y = "Hello, World!"
x = ["apple", "banana", "cherry"]
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

b = "Hello, World!"
print(b[-8:-2])

txt = "The rain in Spain stays mainly in the plain"
x = "b" not in txt
print(x) 

a = "Hello"
b = "World"
c = a + b
print(c)

age = 36 
txt = "My name is John, and I am {}"
print(txt.format(age))

"""Lists"""
#lisiting
#List is a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
print(thislist)
 
#to print required word in the list from first
thislist = ["apple", "banana", "cherry"] #strats with 0,1,2,3....
print(thislist[1]) #positive indexing
#to print rquired word from last
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #negative indexing

#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #2 is included but 5 is not included
#This example returns the items from the beginning to "orange"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0:4]) #or [:4]
#This example returns the items from "cherry" and to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #or [2:7]
#This example returns the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #-4 is included but -1 is not included

#to change the value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#loop through the list items by using a "for" loop
#Print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist: #for loop is uesd with "in" and closed by ":" and we have to use a variable x
  print(x)
#Check if Item Exists
#To determine if a specified item is present in a list use the "in" keyword
thislist=["apple","banana","cherry"]
if "apple" in thislist: #close the statement by ":"
    print("apple is in thislist")
#List Length
#To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Add iteams
#To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#To add an item at the specified index, use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"orange")
print(thislist)

#Remove Item ; There are several methods to remove items from a list
#The remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index, (or the last item if index is not specified)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#The del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[2] #the del function should mention first and give the specific index to remove
print(thislist)
#The del keyword can also delete the list completely
thislist=["apple", "banana", "cherry", "orange"]
del thislist[0:2] #deletes 0 position but not 2 position / from 0 to 1
print (thislist)
#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Copy the list
#one way is to use the built-in List method copy()
#Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist=list(thislist)
print(mylist)

#Join Two Lists
#One of the easiest ways are by using the + operator.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#Use the extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #to get list2 in 1 position use list2.extend(list1)
print(list1)

"""TUPLE"""
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets()
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Change tuple values
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
#add item in tuple , remember we cannot add iteam in tuple directly. we change into list and back to tuple
x = ("apple", "banana", "cherry")    
y=list(x)
y.append("orange")
x=tuple(y)
print(x)
#create one item tuple
#To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
thistuple = ("apple",)
print(type(thistuple))
#we cannoft remove iteams from tuple but del whole tuple
x = ("apple","banana")
del x
print(x)
#Count in tuple
x=(1,2,3,4,4,5,6,7,7,7)
y=x.count(4) #couple(value)in brackets use any value to search in the tuple
print(y)
#index() in tuple
x=(1,6,9,3,5,8,6,7,2,0)
y=x.index(6) #index is used to find which position the value is presented in the tuple
print(y) #here output is 1 because 6 presented in 2 position in tuple as counting starts from 0,1,2,3....

"""SETS"""
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.{}
set = {"apple", "banana", "cherry"}
print(set)
#using for loop
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)
#to check in set   
set = {"apple", "banana", "cherry"}
print("apple" in set)
#to add items in set
set = {"apple", "banana", "cherry"}
set.add("mango")
print(set)
#to add multipe iteams in set
set = {"apple", "banana", "cherry"}
set.update(("orange","mango","strawberry")) #close with double brackets ([]) or (())
print(set)
#to remove any item use remove() or discard()-don't raise the error
set = {"apple", "banana", "cherry"}
set.discard("mango") #dicard() will execute even if the item did not present in the set
print(set)
#The clear() method empties the set
set = {"apple", "banana", "cherry"}
set.clear()
print(set)
#to delete the entire set
set = {"apple", "banana", "cherry"}
del set
print(set)
#to add two sets use union()
set1 = {"apple", "banana", "cherry"}
set2={"orange","mango","strawberry"}
set3=set1.union(set2) #use only this format for sets
print(set3)

"""Dictionary"""
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets{}, and they have keys and values.
x = {               #dictionaries is opened with flower brackets and use ":" step by step
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(x) #output is {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
y=x["brand"] #to know specific item by calling refering name
print(y) #output is Ford
#There is also a method called get() that will give you the same result:
z=x.get("year")
#change the value of a specific item by referring to its key name
x["brand"]=benz

#to get specific iteam we use
y=x["quantity"]
z=x.get("fruit")
#to change any value in dictionary
x["price"]= 150 
print(x)

x={
   "fruit":"mango", #use commas
   "quantity": "2kg",
   "price":100 #no need of commas in last line
   }
for y in x: #the for loop is used to return the values of only keys of the dictionry
    print(y)
for y in x.keys(): #we can also use this to reututn the keys values
    print (y)
    
x={
   "fruit":"mango", #use commas
   "quantity": "2kg",
   "price":100 #no need of commas in last line
   }
for z in x: 
    print(x[z])    #for loop is used to return the values of the dictionaries use z in square brackets of x or dictionary
for z in x.values(): #we can also use this method to return values
    print(z)
    
#to get both keys and values we use items() fuction
for y,z in x.items():
    print(y,z)
#to remove any item in dictionary use pop() fuction     
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.pop("quantity") #always use keyword
print(x)
#we can use pop.item() function  to remove last item in the dictionary
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.popitem()
print(x)
#The del keyword removes the item with the specified key name
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
del x["quantity"] #don't use ":" in del 
print(x)
#The clear() keyword empties the dictionary
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.clear()
print(x)
