import time
import string
import random
# This is my personal kinda program for my minecraft world, others can also use it!
# I actually doesn't really know how to complete it

main_list = []


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
           [co-ordinates] for example (12 90 -145)

show: it will show you the name and serial no. of everything you have saved 
    usage: [keyword] press enter

delete: it will delete the saved variable for that place (please remember that serial no. of that thing again)
    usage: [keyword] press enter
           [co-ordinates](type 'nul' in place of co-ordinates and it will delete everything)

help: it will just simply show this thing again
    usage: help {press enter}\n"""
    print(text)

    while True:
        # slow_print('Invalid input, please try again\n')
        command = input('debug')

        if command == 'edit':
            edit_function()

            exit

        if command == 'show':
            show_function()

            exit

        if command == 'delete':
            del_function()

            exit

        if command =='help':
            slow_print(text)

        if command == 'nothing':
            return command


def edit_function():

    slow_print('Do you want to add or edit existing\n:')
    add_or_edit = input()

    if add_or_edit == 'add':
        ask = input('input, what would you like to\n')
        index = 1
        main_list.append(ask)
        print(main_list)





    pass
















































introduction()
