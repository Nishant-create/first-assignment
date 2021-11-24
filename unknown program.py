import time
import string
import random
# This is my personal kinda program for my minecraft world, others can also use it!
# I actually doesn't really know how to complete it

def slowPrint(anything):

	for char in anything:
		sec = "0.000" + str(random.randrange( 1, 20, 1))
		sec = float(sec)
		print(char,end=''),time.sleep(sec)

def introduction():
	
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
	slowPrint(text)
	
	global command
	command = input('What can I do for you?')

	if command == 'edit':

		global TexT
		TexT = 'sorry not completed the code yet'
		slowPrint(TexT)

	if command == 'show':
		slowPrint(TexT)

	if command == 'delete':
		slowPrint(TexT)

	elif command =='help':
		slowPrint(text)

	else:
		TEXT = 'Error: invalid input'
		slowPrint(TEXT)

introduction()