# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:29:12 2019

@author: nilutpol
"""

#Program to check if a string is pangram or not.(1)
s=input("Enter string: ")
s=s.lower()
l1=[]
for i in s:
    if i.isalpha():
        l1.append(i)
l2=set(l1)
if len(l2)==26:
    print("Pangram")
else:
    print("Not pangram")
    
#Program to check if a string is pangram or not.(2)   
s=input("Enter string: ")
a=set("abcdefghijklmnopqrstuvwxyz")
s=s.lower()
s1=set(s)
c=0
for i in s1:
    if i in a:
        c+=1
if c==26:
    print("Pangram")
else:
    print("Not pangram")



#Program to map two lists into a dictionary
l1=[]
l2=[]
n=int(input("Enter no of keys in dictionary: "))

for i in range(n):
    x=input("Enter Key: ")
    l1.append(x)
    y=int(input("Enter value: "))
    l2.append(y)
    
d=dict(zip(l1,l2))
print("Dictionary: ",d)

#Program to count the no of vowels appearing in a string using sets
s=input("Enter a string: ")
c=0
v=set("aeiouAEIOU")
for i in s:
    if i in v:
        c+=1
        
print("No of vowels in string: ",c)