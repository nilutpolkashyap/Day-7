# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:33:41 2019

@author: nilutpol
"""

#Program to count frequency of words appearing in a string using dictionary

s=input("Enter String: ")
l=(s.lower()).split()
d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
    
#Program to find factorial of a number using functions

num=int(input("Enter number to find factorial: "))
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ", num, " is ", fact(num))
    