import random

numberofattempts = 0

print("Hello, player What's your name")
name = input()
print("nice to meet you " + name)

guessnumber = random.randint(1, 60)

print("Well, " + name + " I was thinking a no. between 1 to 60")
print("Can you Guess the number????")

winlose = False

for numberofattempts in range(1, 7):
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
elif(winlose == True):
    print("Good Job!, you guessed the number in " + str(numberofattempts) + " attempts")
    print("press enter key to exit")
    toxit = input()
