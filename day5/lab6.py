#count the number of even and odd numbers from a series of numbers 
even=0
odd=0
num=int(input("enter the number"))
for i in range(0,num+1):
    if i%2==0:
        even+=1
    
    else:
        odd+=1
        print(f"there are {even} number and {odd} odd numvers from 0to {num}")
