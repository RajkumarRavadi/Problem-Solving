"""
To find the ASCII value of the given character.
A-65
Z-90

a-97
z-122

0-48
9-57

"""

#take input

x=input("Enter a character: ")
l=len(x)
if l==1:
    print("ASCII of {} is {}".format(x,ord(x)))






