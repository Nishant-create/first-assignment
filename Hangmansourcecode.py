import random
import sys
import time

def Delaybetweencharacters():
    from random import randrange

    global text
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 5, 1))
        seconds = float(seconds)
        time.sleep(seconds)

def IntroFunction():
    global text
    text = ("""Hey! its game time.
    today we have planned to play a game known as HANGMAN. Its a bit high level game from our Guessnumber Game.
    So,get ready. In this game you have to guess a word letter by letter. \nNow the interesting thing starts, the word is randomly generated and if you can't guess he word until the hanging man is completely drawn.
    \nDon't worry you can select difficulty on easy there will be Four to three letter words\nOn intermediate the words change to Five to Six words \nAnd on Hard these will change to Seven letter words.\n\n\nGooD LucK    """)

    print("\nSo, let's start with some basic so called game things\n")  
    global name
    name = input()



IntroFunction() 
Delaybetweencharacters()
