# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:57:56 2020

@author: MOHANA D
"""

#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.



class IOString():
    def __init__(self):
        self.str1 = "oh god"

    def get_String(self):
        self.str1 = "oh god"

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()