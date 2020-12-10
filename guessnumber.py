import random

numberofattempts = 0
print("Choose your difficulty")

print("Hello, player What's your name")
name = input()
print("nice to meet you " + name)

guessnumber = random.randint(1, 60)

print("Well, " + name + " I was thinking a no. between 1 to 60")
print("Can you Guess the number????")

winlose = False

for numberofattempts in range(1, 9):
    number = input()
    number = int(number)
    
    if(number > guessnumber):
        print("Well you went to high.")

    elif(number < guessnumber):
        print("Well you went to Low.")
    elif(number == guessnumber):
        winlose = True
        break

if(winlose == False):
    print("You lose,booooooooooooooooooooooooooooooooooo!")
    print("press any key to exit")
    roxit = input()
elif(winlose == True):
    print("Good Job!, you guessed the number in " + str(numberofattempts) + " attempts.")
    print("press enter key to exit")
    toxit = input()
