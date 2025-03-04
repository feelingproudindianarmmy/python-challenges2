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
                    time.sleep(.5)
                    print("Try again!")
                if guess==number:
                    break
            if guess>100 or guess<1:
                print("Silly goose!The number is out of range")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except:
            print("I don`t think that"+enter+"is a number.Sorry!")
    if guess == number:
        guesses= str(guesses)
        print("Good job {} you gusses my number in {} guesses!".format(name,guesses))
    if guess != number:
        print("Nope!The number I was thinking is" + str(number))
playagain="yes"
while playagain=="yes" or playagain=="Yes" or playagain="y":
intro()
pick()
print("Do you want play again")
playagain=input()