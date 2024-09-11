import random

n = random.randint(1,100)
a = int(input("enter the no that you guess: "))
for i in range(1,100):
    
     if(a>n):
        print(f"{i}.your number is more than that of n")
        a=na = int(input("enter the no that you guess: "))
     elif(a<n):
        print(f"{i}.your number is less than that you think")
        a=na = int(input("enter the no that you guess: "))        
if(a==n):
    print('congratulation! you did it')
print(f"the value of n = {n}")

