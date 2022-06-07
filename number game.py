import random as rd
import math as M
lower = int(input("Enter the first number: "))
upper= int(input("Enter the second number: "))
x=rd.randint(lower,upper)
print("you have ",round(M.log(upper -lower+1,2)),"chances to guess the integer \n")
c=0
while c < M.log(upper-lower+1,2):
    c+=1
    guess=int(input("Enter the Number: "))
    if(x==guess):
        print("Congratutations you got the correct guess in ",c,"tries")
        break
    elif x>guess:
        print("you guessed lower then the original number.")
    else:
        print("you guessed upper then the original number.")
if c >= M.log(upper-lower+1,2):
    print("The number is ",x)
    print("\n Better Luck Next Time")