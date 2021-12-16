#check weather 5 is in the list of first 5 number or not.
#list =>[1,2,3,4,5]
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=int(input("enter the fourth number"))
e=int(input("enter the fifth number"))
list ={a,b,c,d,e}
for i in list:
    print("includes umber 5")
    break 
if i==e:
    print("does not include 5")