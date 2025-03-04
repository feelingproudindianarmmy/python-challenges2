import random
import time
number=random.randint(1,50)
def intro():
    print(("May I ask your name?"))
    global name
    name=input("")
    print(name,"Let`s play a game I will think a number you will guess it")
    if (number%2==0):
        h="even"
    else:
        h="odd"
    print("Your number is",h)
    print("Guess!Go ahead!")
def pick():
    guesses=0
    while guesses <6:
        enter=input("Enter your guess number")
        try:
            guess=int(enter)
            if guess>==1 and guess>==50:
                guess=guess+1
                if guess >number:
                    print("The number is too high")
                if guess <number:
                    print("The number is too low")
                if guess!==number