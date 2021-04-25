import time
import random
import string

def hangman():
    global hangman_ascii
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
    
    slowPrint(text)

    speech = ("""\nSo, lets start with some basic game things.
    What's your name ?:-""")
    # you will see it after every "string" variable.
    slowPrint(speech)  

    global name
    name = input()
    
    string = "Choose your language:-"
    slowprint(string)
    time.sleep(1)
    troll =  "Just kidding\nI only know English "
    slowprint(troll)

def settingsfunction():
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write full name of difficulty.\n"""
    slowPrint(text)

    global answer
    answer = input()

    answer = str(answer.lower)

def loopFunction():
    global answer
    while answer != 'easy' and answer != 'intermediate' and answer != 'hard' and answer != 'pro' and answer != 'master':
        settingsfunction()

def mainfunction():
    global hangman_acsii
    global answer

    easy_wordslist = ['cap','ant','fun','run','man','rub','fur','two','one','gun','pig','cow','sit','fit','lit','kit','hot','mop','lot','war','top','don','cod','net','wet','rat','mop']
    intermediate_wordslist = ['ajay','nonu','read','home','lame','rate','same','evil','hack','mice','gell','ride','fill','gill','mill','rice','seed','meet','code','mode','mood','keep','else','leak','rome','zone','foul','doll','worn','warn','shop','alto','json','tool','rule','fool','dome','boom','door','four','five','nine','kill','ammo','stun','girl','luck','next','look','time','best','been','hill','hung','ring','wing','wind','roar','lion','bomb','tear']
    hard_wordslist = ['stalk','child','never','jelly','house','comma','print','empty','tiger','basic','thing','wrong','debug','pause','serve','sauce','study','space','sharp','local','watch','globe','model','seema','break','shift','enter','stack','point','first','alive','alone','night','brave','tobay','world','least','where','apart','album','earth','venus','cause','ready']
    pro_wordslist = ["Friend","twelve","eleven","common","visual","studio","letter","source","winner","number","output","abroad","access","eagles","broken","bureau","advise","belief","gender","golden","guilty","powers","german","france","joseph","handle","yellow","walker","kadyan","inaaya","versus","unless","travel","potter","ronald","useful","exceed","extent","fright","crisis","gaming","defend"]
    master_wordslist = ['acquire','absence','scissor','billion','million','privacy','private','command','windows','control','silence','smoking','butcher','poacher','someone','welcome','waiting','victory','venture','problem','console','station','outline','setting','editors','unsaved','silicon','phoenix','product','nursing','network','obvious','killing','kitchen','illegal','warrior','exactly','consent','crystal','chicken','chronic','balance','bedroom','already','outpost','masters','classes','captain','compete','economy','diamond','palette']

    if answer = 'easy':
        selectedword = (random.choice(easy_wordslist))
        emptystring = "***"

    if answer = 'intermediate':
        selectedword = (random.choice(intermediate_wordslist))
        emptystring = "****"
 
    elif answer = 'hard':
        selectedword = (random.choice(hard_wordslist))
        emptystring = "*****"

    elif answer = 'pro':
        selectedword = (random.choice(pro_wordslist))
        emptystring = "******"

    elif answer = 'master':
        selectedword = (random.choice(master_wordslist))
        emptystring = "*******"

    text = "So, let's start your game."
    slowPrint(text)
    slowprint()
