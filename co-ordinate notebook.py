import time
import string
import random
# This is my personal kinda program for my minecraft world, others can also use it!
# I actually doesn't really know how to complete it

def slow_print(anything):

    for char in anything:
        sec = "0.000" + str(random.randrange( 1, 20, 1))
        sec = float(sec)
        print(char,end=''),time.sleep(sec)

def introduction():
    
    global text
    text =  """Hello! I'll be helping you through this program.   
This program will show you your minecraft world co-ordinates as you have entered them
keywords:

edit: you can edit the co-ordinates you have entered for a place (please remeber the serial no. of those things) 
    usage: [keyword] then press enter
           [serial no. of thing] again press enter
           [co-ordinates] for example |12 90 -145|

show: it will show you the name and serial no. of everything you have saved 
    usage: [keyword] press enter

delete: it will delete the saved variable for that place (please remember that serial no. of that thing again)
    usage: [keyword] press enter
           [serial no. of the thing] again press enter (type 'nul' in place of serial no. and it will delete everything)
           
help: it will just simply show this thing again
    usage: help {press enter}\n"""
    slow_print(text)

    global command
    command = input('What can I do for you?\n:')

    while command != 'edit' and command != 'show' and command != 'delete' and command != 'help':
        
        slow_print('Invalid input, please try again\n')
        command = input()

    if command == 'edit':
        global TexT
        TexT = 'sorry not completed the code yet'
        slow_print(TexT)

    if command == 'show':
        slow_print(TexT)

    if command == 'delete':
        slow_print(TexT)

    if command =='help':
        slow_print(text)

    slow_print('Invalid input, try again')

def storage_place():
    


    introduction()
