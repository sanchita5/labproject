#WAP which acceps marks of four subjects and display total marks , percentange and grade.
#hint:more 70%-> distinction, more than 60% -> first, more than 40% ->pass, less than 40%-> fail
subjectA=int(input("enter the marks of math"))
subjectB=int(input("enter the marks of physics"))
subjectC=int(input("enter the marks of chemistry"))
subjectD=int(input("enter the marks of computing"))
total=subjectA+subjectB+subjectC+subjectD
percentage=total/4
if percentage>=70:
    division="distinction"
elif percentage>=60:
    division="first"
elif percentage>=40:
    division="pass"
else:
    division="fail"
print(f"math: {subjectA}")
print(f"physics:{subjectB}")
print(f"chemistry: {subjectC}")
print(f"computing: {subjectD}")
print(f"totalMarks: {total}")
print(f"percentage: {percentage}")
print(f"division: {division}")