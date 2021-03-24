import random
import os
import time

def GameExplainingFunction():
    PrintableText ="""\nHey! welcome to another game, yeah I know still hangman isn't completed.
    We are getting away from our topic. So, this is a Rock-Paper_scissor game. So I don't need to explain this to you."""
     
    for EveryCharacter in PrintableText:
        seconds = float("0.0" + str(random.randrange( 1, 5 , 1)))
        print(EveryCharacter,end=''),time.sleep(seconds)

    Text =str("So, what's your name ?")

    for EveryCharacter in Text:
        seconds = float("0.0" + str(random.randrange( 1, 5, 1)))    
        print(EveryCharacter,end=''),time.sleep(seconds) 

       
def RandomGenerator():
