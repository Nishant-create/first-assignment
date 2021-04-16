import time 
import random
import secrets
import string


global Hangman_ascii
Hangman_ascii = ['''
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
       _===_\n''','''
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
       _===_\n''','''
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
             _===_\n''','''
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
                   _===_\n''','''
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
    # this thing or you can say FOR loop will make the text appear like anyone is typing it superfast.
    for c in text:
        sec = float("0.0" + str(random.randrange( 1, 5, 1)))
        print(c,end=''),time.sleep(sec)                           

def introFunction():
    # This Function will let the player know that what program even is this. 
    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guess a word letter by letter, a hanging man will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    
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

def settingsFunction():
    # This Function will let the player choose his difficulty. 
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write full name of difficulty, and don't toggle the case of letters.\n"""
    slowPrint(text)

    global answer
    answer = input()
    if (answer == 'easy') or (answer == 'Easy') or (answer == 'EASY'):
        easyFunction()
    elif (answer == 'intermediate') or (answer == 'Intermediate') or (answer == 'INTERMEDIATE'):
        intermediateFunction()
    elif (answer == 'hard') or (answer == 'Hard') or (answer == 'HARD'):
        ()
    elif (answer == 'pro') or (answer == 'Pro') or (answer == 'PRO'):
        print('done')
    elif (answer == 'master') or (answer == 'Master') or (answer == 'MASTER'):
        print('done')

    elif (answer != 'easy') or (answer != 'Easy') or (answer != 'EASY') or (answer != 'intermediate') or (answer != 'Intermediate') or (answer != 'INTERMEDIATE') or (answer != 'hard') or (answer != 'Hard') or (answer != 'HARD') or (answer != 'pro') or (answer != 'Pro') or (answer != 'PRO') or (answer != 'master') or (answer != 'Master') or (answer != 'MASTER'):
        prit = "((Error)Invalid input) please read the note written with the question."
        slowPrint(prit)
        loopFunction()

def loopFunction():

    global answer

    while (answer != 'easy') and (answer != 'Easy') and (answer != 'EASY') and (answer != 'intermediate') and (answer != 'Intermediate') and (answer != 'INTERMEDIATE') and (answer != 'hard') and (answer != 'Hard') and (answer != 'HARD') and (answer != 'pro') and (answer != 'Pro') and (answer != 'PRO') and (answer != "master") and (answer != 'Master') and (answer != 'MASTER'):
        settingsFunction() 

def easyFunction():

    global answer
    
    text = "So, let's start your game."
    slowPrint(text)
  
    wordslist = ['cap','ant','fun','run','man','rub','fur','two','one','gun','pig','cow','sit','fit','lit','kit','hot','mop','lot','war','top','don','cod','net','wet','rat','mop',]
    selectedword = (secrets.choice(wordslist))
    print("\n\n")
    emptyString =  "***"
    slowPrint(emptyString)
     
    printstatement = "\n\n\nGuess a letter\n "
    slowPrint(printstatement)             

    Wrong = 0

    numberofguesses = 0
    global winlose
    winlose = False

    for numberofguesses in range(0,1024):

        guess = input()
        guess = str(guess)
        guess = guess.lower()

        finder = selectedword.find(guess)                                              
        
        if  (finder == int(-1)):

            global wrongAnswerList


            wrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers "]
            wrongAnswerVariable = (random.choice(wrongAnswerList)),
            slowPrint(wrongAnswerVariable)
            hangman_printer = ((Hangman_ascii[Wrong]) + '\n')
            slowPrint(hangman_printer)
            Wrong = numberofguesses

            if (Wrong == 7):
                winlose = False
                break 
                
            
        else:
            correctAnswerText = "That' a Correct one\n"
            slowPrint(correctAnswerText)

            templist = list(emptyString)
            templist[finder] = guess
            emptyString = "".join(templist)
            print(emptyString)   

        if(emptyString == selectedword):
            winlose = True 
            break
            
def intermediateFunction():
    global answer

    text = "So, let's start your game."
    slowPrint(text)

    wordslist = ['ajay','nonu','read','home','lame','rate','same','evil','hack','mice','gell','ride','fill','gill','mill','rice','seed','meet','code','mode','mood','keep','else','leak','rome','zone','foul','doll','worn','warn','shop','alto','json','tool','rule','fool','dome','boom','door','four','five','nine','kill','ammo','stun','girl','luck','next','look','time','best','been','hill','hung','ring','wing','wind','roar','lion','bomb','tear']
    selectedword = (secrets.choice(wordslist))
    print("\n\n")
    emptyString =  "****"
    slowPrint(emptyString)

    printstatement = "\n\n\nGuess a letter\n "
    slowPrint(printstatement)             

    Wrong = 0

    numberofguesses = 0
    global winlose
    winlose = False
   
    for numberofguesses in range(0,1024):

        guess = input()
        guess = str(guess)
        guess = guess.lower()

        finder = selectedword.find(guess)                                              
        
        if  (finder == int(-1)):

            global wrongAnswerList


            wrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers "]
            wrongAnswerVariable = (random.choice(wrongAnswerList)),
            slowPrint(wrongAnswerVariable)
            hangman_printer = ((Hangman_ascii[Wrong]) + '\n')
            slowPrint(hangman_printer)
            Wrong = numberofguesses

            if (Wrong == 7):
                winlose = False
                break 
                
        else:
            correctAnswerText = "That' a Correct one\n"
            slowPrint(correctAnswerText)

            templist = list(emptyString)
            templist[finder] = guess
            emptyString = "".join(templist)
            printableString = emptyString   

            slowPrint(printableString)

        if(emptyString == selectedword):
            winlose = True 
            break

def hardFunction():
    global answer

    text = "So, let's start your game."
    slowPrint(text)

    wordslist = ['stalk','child','never','jelly','house','comma','print','empty','tiger','basic','thing','wrong','debug','pause','serve','sauce','study','space','sharp','local','watch','globe','model','seema','break','shift','enter','stack','point','first','alive','alone','night','brave','tobay','world','least','where','apart','album','earth','venus','cause','ready']
    selectedword = (secrets.choice(wordslist))
    print("\n\n")
    emptyString =  "*****"
    slowPrint(emptyString)

    printstatement = "\n\n\nGuess a letter\n "
    slowPrint(printstatement)             

    Wrong = 0

    numberofguesses = 0
    global winlose
    winlose = False
   
    for numberofguesses in range(0,1024):

        guess = input()
        guess = str(guess)
        guess = guess.lower()

        finder = selectedword.find(guess)                                              
        
        if  (finder == int(-1)):

            global wrongAnswerList


            wrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers "]
            wrongAnswerVariable = (random.choice(wrongAnswerList)),
            slowPrint(wrongAnswerVariable)
            hangman_printer = ((Hangman_ascii[Wrong]) + '\n')
            slowPrint(hangman_printer)
            Wrong = numberofguesses

            if (Wrong == 7):
                winlose = False
                break 
                
        else:
            correctAnswerText = "That' a Correct one\n"
            slowPrint(correctAnswerText)

            templist = list(emptyString)
            templist[finder] = guess
            emptyString = "".join(templist)
            printableString = emptyString   

            slowPrint(printableString)

        if(emptyString == selectedword):
            winlose = True 
            break

def     

def winnerOrLoserCheckFunction():
    global winlose
    if (winlose == True):
        text = """The Game is complete. You have Guessed the letter and the HANGMAN isn't still completed.\
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              =========\n"""
        slowPrint(text)      

    elif (winlose == False):
        text = "Oh! Looks like the Hangman has been completed.😞😞 Better Luck Next Time."    
        slowPrint(text)

# printStatement = "Do you wanna play it again\n  Only 'yes' or 'no'"
# slowPrint(printStatement)
# loopvariable = input(str)
# 
# loopvariable = loopvariable.lower
# if loopvariable == yes:
introFunction()
settingsFunction()
winnerOrLoserCheckFunction()


















