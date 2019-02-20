# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:35:31 2019

@author: nilutpol
"""

#To merge two lists and sort it

l1=[]
l2=[]
l3=[]
l4=[]

n1=int(input("No of elements in list 1: "))

print("\nList 1")
for i in range(n1):
    x=int(input("Enter list item "))
    l1.append(x)
    
n2=int(input("No of elements in list 2: "))
print("\nList 2")
for i in range(n2):
    x=int(input("Enter List item "))
    l2.append(x)
    
l3=l1+l2
j=0
while j in range(len(l3)):
    mini=l3[0]
    s=len(l3)
    for i in range(s):
        if l3[i]<mini:
            mini=l3[i]
            
    l4.append(mini)
    l3.remove(mini)

print("New Sorted List: ",l4)

#Create list of even numbers using list comprehension

l=[]
even=[]

n=int(input("Enter no of elements in list: "))

print("\nEnter List")
for i in range(n):
    x=int(input("Enter list item: "))
    l.append(x)
    
even=[i for i in l if i%2==0]
print(even)


#To count upper and lower characters in a list

a=input("Enter list")
cu=0
cl=0
for i in a:
    if(i.isupper()):
        cu=cu+1
    elif(i.islower()):
        cl=cl+1
        
print("Upper Case count: ",cu)
print("Lower Case count: ",cl)
