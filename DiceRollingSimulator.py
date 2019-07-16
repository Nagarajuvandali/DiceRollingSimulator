import random

def dice():
    print ("Dice is rolling and the number is : ",end="")
    print (random.choice([1, 2, 3, 4, 5, 6]))

a=1
while a==1:
    dice()
    a = int(input("Do you want to roll again?if you want to roll again click 1 for yes else 2 for no"))