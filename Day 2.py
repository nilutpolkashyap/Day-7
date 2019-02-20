# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:29:02 2019

@author: Nilutpol
"""
#Largest Number is List

l=[]
s=int(input("Enter Size of List "))

for i in range(s):
    x=int(input("Enter list item "))
    l.append(x)
n=l[0]
for i in range(s):
    if l[i]>n:
        n=l[i]
        
print("Largest Number in list is",n)




#Second Largest Number is List
l=[]
s=int(input("Enter Size of List "))

for i in range(s):
    x=int(input("Enter list item "))
    l.append(x)
    
l.sort()
del(l[-1])

print("Second Largest Number in List is",l[-1])




#Separating Even and Odd Items in a List
l=[]
l1=[]
l2=[]
s=int(input("Enter Size of List "))

for i in range(s):
    x=int(input("Enter list item "))
    l.append(x)
    
for i in range(s):
    if(l[i]%2==0):
        l1.append(l[i])
    else:
        l2.append(l[i])
        
print("Even list=",l1)
print("Odd list=",l2)


####


a=int(input("enter first no."))
b=int(input("enter second no."))
c=int(input("enter third no."))

if(a>b):
    if(a>c):
        print("a is lar.")
    else:
        print("c is lar.")
else:
    if(b>c):
        print("b is lar.")
    else:
        print("c is lar.")
        



        