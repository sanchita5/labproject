#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character 
# are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
#  Expected Result : 2 
list=['abc','xyz','abc','1221']
c=0
for i in list:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            c+=1
print(c)