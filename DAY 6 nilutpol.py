#Program to create a dictionary at runtime

s=int(input("Enter number of keys: "))
d={}
for i in range(s):
    key=input("Enter key: ")
    value=int(input("Enter Value: "))
    d.update({key:value})
print("Updated Dictionary is: ",d)


#

s=int(input("Enter number of keys: "))
d={}
for i in range(s):
    key=input("Enter key: ")
    value=[]
    for i in key:
        if i in "aeiouAEIOU":
            value.append(i)
    d.update({key:value})
print("Updated Dictionary is: ",d)