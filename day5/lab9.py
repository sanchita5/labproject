# program to find the factorial of a number. 
num=int(input('enter the number'))
factorial = 1
if num <0:
    print("factorial of negative number doesnot exist.")
elif num ==0:
    print(f"factorial of 0 is{factorial}")
else:
      for x in range(1,num +1):
        factorial = x*factorial
        print(f"factorial of{num} is {factorial}")