# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:05:38 2019

@author: Nilutpol
"""

#Day 1

print("CALCULATOR")
x=float(input("Enter First Number"))
y=float(input("Enter Second Number"))

Sum=x+y
Diff=x-y
Prod=x*y
Divi=x/y
Mod=x%y

print("Enter your choice")
print("1.Addition /n 2.Subtraction /n 3.Product /n 4.Division /n 5.Modulus")

ch=int(input())

if(ch==1):
    print(Sum)
elif(ch==2):
    print(Diff)
elif(ch==3):
    print(Prod)
elif(ch==4):
    print(Divi)
elif(ch==5):
    print(Mod)
else:

    print("Invalid Input")
    
    
#FOR GRADES CALCULATION

print("Grading System")

print("Enter Marks of Student")

print("Subject")
m=int(input())

if(m>90 and m<=100):
    print("Grade A")
elif(m>80 and m<=90):
    print("Grade B")
elif(m>70 and m<=80):
    print("Grade C")
elif(m>60 and m<=70):
    print("Grade D")
elif(m>50 and m<= 60):
    print("Grade E")
elif(m>=0 and m<=50):
    print("FAIL")
else:
    print("INVALID INPUT")



