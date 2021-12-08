#give the number of student in each class,print the smallest possible number of desk 
#when a desk is used for two students.
a=int(input("enter the number of student in class A"))
b=int(input("enter the number of the student in class B"))
C= int(input("enter the number of student in class C"))
deskInA=a//2
deskInB=b//2
deskInc=C//2
if a % 2!=0:
    deskInA +=1
if b % 2!=0:
    deskInB +=1
if C % 2!=0:
    deskInc +=1
total=deskInA=deskInB+deskInc
print(f"the total number of desks required is {total}")