# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 20:58:10 2017

@author: nandu
"""

#%%
def first():
    print("Hello World")



#%%
def areaTriangle(base,height):
    area = (1/2)*base*height
    print("The area of triangle of base",base,"and height",height,"is:",area) 

#%%
def fahrenheit(celcius):
    f = 1.8 * celcius +32
    print(celcius,"degree celcius \in '\\'fahrenheit is:",f)



#%%
fahrenheit(0)
fahrenheit(50)
fahrenheit(100)



#%%
def capturePerson():
    fname = input("Enter your first Name: ")
    lname = input("Enter your last name: ")
    
    fullName = fname + " " + lname
    print("Your Name is: " + fullName)
    
#%%

def calculateArea(value):
    if(value == 0):
        absValue = value
    elif(value>0):
        absValue = value
    elif(value<0):
        absValue = -1* value
        
    print("Absolute Value is:",absValue)
    

    




#%%