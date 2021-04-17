import random
import time

def slowPrint(text):
    for char in text:
        sec = "0.0" + str(random.randrange( 1, 5, 1))
        sec = float(sec)
        print(char,end=''),time.sleep(sec)


text = "this is a demo text."
slowPrint(text)

printStatement = "\nThis another demo test to check."
slowPrint(printStatement) 