import random

comp = random.choice([1,2,3])
mydict = {"rock":1,"paper":2,"scissor":3}
reversedict = {1:"rock",2:"paper",3:"scissor"}
you = input("enter your choice(rock,paper,scissor):")
yourstr = mydict[you]

print("computer chosen",reversedict[comp])
print("you chosen",you)


if comp == yourstr:
    print("the match is tie!")
else:
    if comp == 1 and yourstr == 2:
        print("you win!!")
    elif comp == 1 and yourstr == 3:
        print("you lose!!")
    elif comp == 2 and yourstr == 1:
        print("you lose!!")
    elif comp == 2 and yourstr == 3:
        print("you win!!")
    elif comp == 3 and yourstr == 1:
        print("you win!")
    elif comp == 3 and yourstr == 2:
        print("you lose!")
    