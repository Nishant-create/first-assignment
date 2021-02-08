
import random 

numberofattempts = 0

def intro():
    print("Welcome player")
    print("Let me introduce you to the game.")
    print("This is a Guess the Number type game, so the machine will randomly generate a number,")
    print("you have a limited number of chances to guess the number,the game will give you hints")
    print("on your every guess, I hope you have understood the game, so go enjoy....")
    print("Oh! I forgot to ask your name.")
    print("What's your name???")

    name = input()

    print("Nice to meet you " + str(name))
    print("Ready to start the game??")
    print("Press enter to continue")
    start = input()

def game():

    print("How many attempts do you want?")

    number = input()
    number = int(number)

    print("Please enter lowest number of range")

    smallrange = input()
    smallrange = int(smallrange)

    print("please enter highest number of range")

    highrange = input()
    highrange = int(highrange)

    guessnumber = random.randint(int(smallrange),int(highrange))

    winlose = False

    while(highrange < number):
        print("Caught you, cheeky little thing.")
        print("Only one more chance play honestly.")
        print("Enter your attempts again")
        number = input()
        number = int(number)
        

    print("Your game starts now, Good Luck ;)")

    for numberofattempts in range(1,int(number)):
        guess = input()
        guess = int(guess)

        if(guess > guessnumber):
            print("You went too High")

        elif(guess < guessnumber):
            print("You went too Low")

        elif(guess == guessnumber):
            winlose = True
            break
    if(winlose==True):
        print("Good Job, you guessed the number in " + str(numberofattempts) + " attempts")
        print("Press enter to exit...")
        roxit = input()
    else:
        print("Better luck next time")
        print("press enter to exit...")
        toxit = input()

intro()

game()



