#guess a number between 1 to 9.
num=4
while True:
    guess=int(input("guess the number between 1-9"))
    if guess>0 and guess==4 and guess<10:
        print("well,guessed")
        break
    else:
        print("enter again")
        continue