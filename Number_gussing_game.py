import random as r
 
s=r.randint(1,100)
k=10
while k:
    n=int(input("Enter Your Number:"))
    if n==s:
        print("Congratulation!...You Won.")
        break
    elif n>100 or n<0:
        print("Silly Goose! That number isn't in the range!")
        print("Please enter a number between 1 and 100")
    elif s>n:
        print("The guess of the number that you have entered is too low")
    elif s<n:
        print("The guess of the number that you have entered is too high")
    k-=1
print("Game Over")
print("Computer gen",s)