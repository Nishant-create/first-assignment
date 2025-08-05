import random
import time

def slowPrint(text):
    for char in text:
        sec = "0.0" + str(random.randint(1, 100))
        sec = float(sec)
        print(char,end='', flush =True),time.sleep(sec)

text = "this is a demo text."
slowPrint(text)

printStatement = "\nThis another demo test to check."
slowPrint(printStatement) 