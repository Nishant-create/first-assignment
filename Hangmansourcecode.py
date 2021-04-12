import time 
import random
import secrets
import string


global Hangman_ascii
Hangman_ascii = ['''\  
+=========+
         |
         |
         |
         |
         |
         |
         |
         |
         |
         |
       _===_\n''','''\
+=========+
O        |
         |
         |
         |
         |
         |
         |
         |
         |
       _===_\n''','''\
       +========+
       O       |
      /        |
               |
               |
               |
               |
               |
               |
               |
             _===_\n''','''
       +========+
       O       |
      / \      |
               |
               |
               |
               |
               |
               |
               |
             _===_\n''','''\
             +========+
             O       |
            /|\      |
                     |
                     |
                     |
                     |
                     |
                     |
                     |
                     |
                   _===_\n''','''\
                   +==========+
                   O         |
                  /|\        |
                  /          |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                           _===_\n''','''
                   +==========+
                   O         |
                  /|\        |
                  / \        |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                           _===_\n''',]

def slowPrint(text):
    for c in text:
        sec = float("0.0" + str(random.randrange( 1, 5, 1)))
        print(c,end=''),time.sleep(sec)                           

def IntroFunction():
    # This Function will let the player know that what program even is this. 
    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guess a word letter by letter, a hanging man will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    # this thing or you can say FOR loop will make the text appear like anyone is typing it superfast.
    slowPrint(text)

    pri = ("""\nSo, lets start with some basic game things.
    What's your name ?:-""")
    # you will see it after every "string" variable.
    slowPrint(pri)  

    global name
    name = input()
    #  You can't understand it because its written in Spanish.
    Text = ("Bonito Nombre niño ")
    slowPrint(Text)

def SettingsFunction():
    # This Function will let the player choose his difficulty. 
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write full name of difficulty, and don't toggle the case of letters.\n"""
    slowPrint(text)

    global answer
    answer = input()
    if (answer == 'easy') or (answer == 'Easy') or (answer == 'EASY'):
        EasyFunction()
    elif (answer == 'intermediate') or (answer == 'Intermediate') or (answer == 'INTERMEDIATE'):
        print('done')
    elif (answer == 'hard') or (answer == 'Hard') or (answer == 'HARD'):
        print('done')
    elif (answer == 'pro') or (answer == 'Pro') or (answer == 'PRO'):
        print('done')
    elif (answer == 'master') or (answer == 'Master') or (answer == 'MASTER'):
        print('done')

    elif (answer != 'easy') or (answer != 'Easy') or (answer != 'EASY') or (answer != 'intermediate') or (answer != 'Intermediate') or (answer != 'INTERMEDIATE') or (answer != 'hard') or (answer != 'Hard') or (answer != 'HARD') or (answer != 'pro') or (answer != 'Pro') or (answer != 'PRO') or (answer != 'master') or (answer != 'Master') or (answer != 'MASTER'):
        prit = "((Error)Invalid input) please read the note written with the question."
        slowPrint(prit)
        LoopFunction()

def LoopFunction():

    global answer

    while (answer != 'easy') and (answer != 'Easy') and (answer != 'EASY') and (answer != 'intermediate') and (answer != 'Intermediate') and (answer != 'INTERMEDIATE') and (answer != 'hard') and (answer != 'Hard') and (answer != 'HARD') and (answer != 'pro') and (answer != 'Pro') and (answer != 'PRO') and (answer != "master") and (answer != 'Master') and (answer != 'MASTER'):
        SettingsFunction() 

def EasyFunction():

    global answer
    
    text = "So, let's start your game."
    slowPrint(text)
  
    wordslist = ['cap','ant','fun','run','man','rub','fur','two','one','gun','pig','cow','sit','fit','lit','kit','hot','mop','lot','war','top','don','cod','net','wet','rat','mop']
    selectedword = (secrets.choice(wordslist))
    print("\n\n")
    emptyString =  "***"
    print('Debug Only\n' + selectedword)
    slowPrint(emptyString)
     
    printstatement = "\n\n\nGuess a letter\n "
    slowPrint(printstatement)             

    Wrong = 0

    numberofguesses = 0

    winlose = False

    for numberofguesses in range(0,10):

        Guess = input()
        Guess = str(Guess)
        Guess = Guess.lower()

        finder = selectedword.find(Guess)                                              
        
        if  (finder == int(-1)):

            global WrongAnswerList


            WrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers "]
            WrongAnswerVariable = print(random.choice(WrongAnswerList)),range(0, 1)
            print(Hangman_ascii[Wrong])
            Wrong = numberofguesses
            
        else:
            CorrectAnswerText = "That' a Correct one"
            slowPrint(CorrectAnswerText)

            templist = list(emptyString)
            templist[find] = Guess
            emptyString = "".join(templist)
            print(emptyString)

        if(numberofguesses == 10):
            winlose = False
            break   

        elif(emptyString == selectedword):
            

EasyFunction()

















