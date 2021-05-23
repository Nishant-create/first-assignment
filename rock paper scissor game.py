import random
import os
import time
import string

def slowPrintFunction(text):
    for everyCharacter in text:
        seconds = float(str(0.0) + str(random.randrange( 1, 9, 1)))
        print(everyCharacter,end=''),time.sleep(seconds)

def gameExplainingFunction():
    
    printableText ="""\nHey! welcome to another game, 
    So, this is a Rock-Paper_scissor game. So I don't need to explain this to you.\n If you Don't know the how to play Rock-Paper_scissor than just die in the hell."""
     
    slowPrintFunction(printableText)

    text =str("So, what's your name ?\n")

    slowPrintFunction(text)
    
    name = input()
     

def OBJFunction():
    rock_Paper_Scissors_List = ['Rock','Paper','Scissors']
    randomGenerator_Variable = random.choice(rock_Paper_Scissors_List)
    
    
    text = "So, let's start the game" + "\n(Type 'a' for paper ; 's' for scissors ; 'd' for rock) "

    slowPrintFunction(text)

    def counter():
        print('\n\n3')
        time.sleep(1)
        print('\n2')
        time.sleep(1)
        print('\n1\n') 
        time.sleep
    counter()

    

OBJFunction() 