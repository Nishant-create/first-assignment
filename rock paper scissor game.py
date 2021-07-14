import time
import random
import string

def slowprint(text):
    for char in text:
        sec = "0.000" + str(random.randrange( 1, 3))
        sec = float(sec)
        print(char,end=''),time.sleep(sec)    

def rockPaperScissorsGame():
    text = """Hey! welcome to another game, 
    So, this is a Rock-Paper_scissor game. So I don't need to explain this to you.\n If you Don't know the how to play Rock-Paper_scissor than just die in the hell."""

    slowprint(text)

    while True:
        Text = """\nChoose between
        1. Rock
        2. Paper
        3. Scissors
        
        Note :- Please enter the index number of the your option.\n"""

        slowprint(Text)
        putthat = "user turn:"
        rootthat = "enter valid input:"

        user_choice = int(input(putthat))

        while user_choice > 3 or user_choice < 1:
            user_choice = int(input(rootthat))

        if user_choice == (1):
            user_choice_name  = "Rock"
        elif user_choice == (2):
            user_choice_name = "Paper"
        else:
            user_choice_name = "Scissors"

        printtext = ("\nUser's choice is: " + user_choice_name)

        slowprint(printtext)

        comp_choice = random.randint(1,3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        printstatement = ("\n\nComputer's choice is: " + comp_choice_name + "\n")

        slowprint(printstatement)
        
        if user_choice == 1 and comp_choice == 2:
            won = comp_choice
            if won == comp_choice:
                winner = 'Computer'
            text02 = winner + " wins"  
            slowprint(text02)

        if user_choice == 2 and comp_choice == 3:
            won = comp_choice
            if won == comp_choice:
                winner = 'Computer'
            text03 = winner + " wins"   
            slowprint(text03)

        if user_choice == 3 and comp_choice == 1:
            won = comp_choice
            if won == comp_choice:
                winner = 'Computer'
            text04 = winner + " wins"
            slowprint(text04)

        elif user_choice == 1 and comp_choice == 3:
            won = comp_choice
            if won == comp_choice:
                winner = 'User'
            text05 = winner + " wins"
            slowprint(text05)

        elif user_choice == 2 and comp_choice == 1:
            won = comp_choice
            if won == comp_choice:
                winner = 'User'
            text06 = winner + " wins"
            slowprint(text06)

        elif user_choice == 3 and comp_choice == 2:
            won = comp_choice
            if won == comp_choice:
                winner = 'User'
            text07 = winner + " wins"
            slowprint(text07)
        elif user_choice == comp_choice:
            text08 = "Oh! looks like a draw"
            slowprint(text08)

        break

def loopfunction():
    text09 = "\n\nDo you wanna play again (Y/N)\n"
    slowprint(text09)
    user_response = input()
    
    while user_response != 'y' and 'n':
        text11 = 'Invalid response plz try again.'
        slowprint(text11)
        user_response = input()

    user_response = user_response.lower

    if user_response == 'y':
        rockPaperScissorsGame()

    elif user_response == 'n':
        text10 = "Ba Bye! hope to see you again."
        slowprint(text10)
        exit()

rockPaperScissorsGame()
loopfunction()