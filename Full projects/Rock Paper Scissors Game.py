import time
import random
import string

def slowprint(text):
    for char in text:
        sec = "0.000" + str(random.randrange( 1, 3))
        sec = float(sec)
        print(char,end=''),time.sleep(sec)    

def introductoryFunction():
    slowprint("""Hey! welcome to another game, 
    So, this is a Rock-Paper_scissor game. So I don't need to explain this to you.\n If you Don't know the how to play Rock-Paper_scissor than just die in the hell.""")

    slowprint("""\nChoose between
    1. Rock
    2. Paper
    3. Scissors
    
    Note :- Please enter the index number of the your option.\n""")

def rockPaperScissorsGame():

    putthat = "user turn: "
    rootthat = "enter valid input: "

    user_choice = int(input(putthat))

    while user_choice < 1 and user_choice > 3:
        user_choice = int(input(rootthat))

    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else:
        user_choice_name = 'Scissors'

    slowprint("\nUser's choice is: " + user_choice_name)

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    slowprint("\nComputer's choice is: " + comp_choice_name)

    if user_choice == comp_choice:
        slowprint('\nOh! looks like a tie.')

    if user_choice == 1:
        if comp_choice == 2:
            winner = 'Computer'
        else:
            winner = 'User'

    elif user_choice == 2:
        if comp_choice == 3:
            winner = 'Computer'
        else:
            winner = 'User'

    elif user_choice == 3:
        if comp_choice == 1:
            winner = 'Computer'
        else:
            winner = 'User'

    slowprint('\n' + winner + ' wins!')

    loopfunction()
    
def loopfunction():

    slowprint("\n\nDo you wanna play again! (Y/N)\n")
    user_response = input()

    if user_response == 'Y':
        slowprint('Ok! then\n\n\n')
        rockPaperScissorsGame()

    elif user_response == 'N':
        slowprint('Ba Bye! hope to see you again.')
        exit

    while user_response != 'Y' and user_response != 'N':
        user_response = input('enter valid input: ')



introductoryFunction()
rockPaperScissorsGame()
