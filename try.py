# try
import time
import random

text = "Hello, this is a test ."
for char in text:
    sec = "0." + str(random.randrange(1, 4, 1))
    sec = float(sec)
    print (char,end='I am at end'),time.sleep(sec)