import time
import random
import string

def winnerorlosercheckfunction():
    global winlose
    if (winlose == True):
        text = """\n\n\nThe Game is complete. You have Guessed the letter and the HANGMAN isn't still completed.\
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
             ===========\n"""
        slowprint(text)      

    elif (winlose == False):
        texty = "Oh! Looks like the Hangman has been completed.😞😞 Better Luck Next Time."    
        slowprint(texty)

hangman_ascii = ['''
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

def slowprint(text):
    for char in text:
        sec = float("0.00" + str(random.randrange( 1, 3, 1)))
        print(char,end=''),time.sleep(sec)

def introfunction():
    # This Function will let the player know that what program even is this. 
    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guess a word letter by letter, a hanging man will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    
    slowprint(text)

    speech = ("""\nSo, lets start with some basic game things.
    What's your name ?:-""")
    # you will see it after every "string" variable.
    slowprint(speech)  

    global name
    name = input()
    
    string = "Choose your language:-"
    slowprint(string)
    inputlanguage = input()
    troll =  "Just kidding\nI only know English "
    slowprint(troll)

def settingsfunction():
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write full name of difficulty.\n"""
    print(text)

    global answer
    answer = input(str)
    answer = answer.lower()
    print(answer)
    
    while answer != 'easy' and answer != 'intermediate' and answer != 'hard' and answer != 'pro' and answer != 'master':
        settingsfunction()

def OBJfunction():

    global answer

    easy_wordslist = ['cap','ant','fun','run','man','rub','fur','two','one','gun','pig','cow','sit','fit','lit','kit','hot','mop','lot','war','top','don','cod','net','wet','rat','mop']
    intermediate_wordslist = ['ajay','nonu','read','home','lame','rate','same','evil','hack','mice','gell','ride','fill','gill','mill','rice','seed','meet','code','mode','mood','keep','else','leak','rome','zone','foul','doll','worn','warn','shop','alto','json','tool','rule','fool','dome','boom','door','four','five','nine','kill','ammo','stun','girl','luck','next','look','time','best','been','hill','hung','ring','wing','wind','roar','lion','bomb','tear']
    hard_wordslist = ['stalk','child','never','jelly','house','comma','print','empty','tiger','basic','thing','wrong','debug','pause','serve','sauce','study','space','sharp','local','watch','globe','model','seema','break','shift','enter','stack','point','first','alive','alone','night','brave','tobay','world','least','where','apart','album','earth','venus','cause','ready']
    pro_wordslist = ["Friend","twelve","eleven","common","visual","studio","letter","source","winner","number","output","abroad","access","eagles","broken","bureau","advise","belief","gender","golden","guilty","powers","german","france","joseph","handle","yellow","walker","kadyan","inaaya","versus","unless","travel","potter","ronald","useful","exceed","extent","fright","crisis","gaming","defend"]
    master_wordslist = ['acquire','absence','scissor','billion','million','privacy','private','command','windows','control','silence','smoking','butcher','poacher','someone','welcome','waiting','victory','venture','problem','console','station','outline','setting','editors','unsaved','silicon','phoenix','product','nursing','network','obvious','killing','kitchen','illegal','warrior','exactly','consent','crystal','chicken','chronic','balance','bedroom','already','outpost','masters','classes','captain','compete','economy','diamond','palette']

    if (answer == 'easy'):
        selectedword = (random.choice(easy_wordslist))
        emptystring = "***"

    if (answer == 'intermediate'):
        selectedword = (random.choice(intermediate_wordslist))
        emptystring = "****"
 
    elif (answer == 'hard'):
        selectedword = (random.choice(hard_wordslist))
        emptystring = "*****"

    elif (answer == 'pro'):
        selectedword = (random.choice(pro_wordslist))
        emptystring = "******"

    elif (answer == 'master'):
        selectedword = (random.choice(master_wordslist))
        emptystring = "*******"

    text = "So, let's start your game."
    slowprint(text)
    print('Debug Only' + selectedword)
    print('\n\n')
    slowprint(emptystring)
    printstatement = "\n\n\nGuess a letter\n "
    slowprint(printstatement)             

    numberofguesses = 0
    numberofwrongguesses = 0
    global winlose
    winlose = False
    
    for numberofguesses in range(1, 1024):
        guess = input(str)
        guess = guess.lower()

        inspector = selectedword.find(guess)
        inspector = int(inspector)
        if inspector == int(-1):
            wronganswerlist = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers "]
            wronganswervariable = (random.choice(wronganswerlist)),
            slowprint(wronganswervariable)
            hangman_printer = ((hangman_ascii[numberofwrongguesses]) + '\n')
            slowprint(hangman_printer)
            numberofwrongguesses = numberofwrongguesses + 1

            assert(numberofwrongguesses < len(hangman_ascii))

            if numberofwrongguesses == len(hangman_ascii):
                winlose = False
                break

        else:
            correctanswertext = "That' a Correct one\n"
            slowprint(correctanswertext)

            templist = list(emptystring)
            templist[inspector] = guess
            emptystring = "".join(templist)
            printabletext = emptystring   
            tempList = list(printabletext)
            tempList[inspector] = '*'
            printabletext = "".join(tempList)
            emptystring = printabletext 

            slowprint(emptystring)

        if emptystring == selectedword:
            winlose = True
            break   

    winnerorlosercheckfunction()

def mainfunction():
    settingsfunction()
    OBJfunction()
    loopFunction()

def loopFunction():

    text = "Do you wanna play it again?\nNote : Only 'yes' or 'no'."
    slowprint(text)
    canihavetheanswer = input(str)
    canihavetheanswer = canihavetheanswer.lower()

    if canihavetheanswer == 'yes':
        printvariable = "Ok then"
        slowprint(printvariable)
        mainfunction()

    else:
        exit()    

settingsfunction()
OBJfunction()
loopFunction()

