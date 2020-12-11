
import random

numberofattempts = 0

print("Welcome player")
print("Let me introduce you to the game.")
print("This is a Guess the Number type game, so the machine will randomly generate a number,")
print("you have a limited number of chances to guess the number,the game will give you hints")
print("on your every guess, I hope you have understood the game, so go enjoy....")
print("Oh! I forgot to ask your name.")
name = input()
print("Nice to meet you " + str(name))
print("Ready to start the game??")
print("Press enter to continue")
start = input()
print("How many attempts do you want?")

number = input()
number = int(number)

print("How much range do you want?")
print("please enter only Smallest number of range")

smallrange = input()
smallrange = int(smallrange)

print("please enter only Highest number of range")
highrange = input()
highrange = int(highrange)

guessnumber = random.randint(int(smallrange),int(highrange))

print("Your game starts now, Good Luck ;)")

for numberofattempts in range(1,int(number)):
    guess = input()
    guess = int(guess)

    if(guess > guessnumber):
        print("You went too High")

    elif(guess < guessnumber):
        print("You went too Low")

    elif(guess == guessnumber):
        print("Good Job, you guessed the number in " + str(numberofattempts) + " attempts")
