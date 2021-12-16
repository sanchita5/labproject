#write a program to print absolute value of a number entered by user.
# E.g.- INPUT: 1   OUTPUT:1
#INPUT: -1         OUTPUT:1
a=input("enter an integer:")
for i in a:
    if i=="-":
        continue
    print(i, end="")