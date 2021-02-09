import time 
import random

def IntroFunction():

    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guessnumber a word letter by letter, a hanging an will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    print( text )
    time.sleep(0.2)
    print("\nSo, lets start with some basic game things.\nWhat's your name ?")
    time.sleep(0.3)

    global name
    name = input()

    time.sleep(0.2)
    print("Bonito Nombre niño ")

def Settingsfunction():
    

IntroFunction()
