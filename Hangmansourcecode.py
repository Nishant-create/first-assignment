import time 
import random
import secrets


global Hangman_ascii_easy
Hangman_ascii_easy = ['''\  
+=========+
         |
         |
         |
         |
         |
         |
         |
         |
         |
         |
       _===_\n''','''\
+=========+
O        |
         |
         |
         |
         |
         |
         |
         |
         |
       _===_\n''','''\
       +========+
       O       |
      /        |
               |
               |
               |
               |
               |
               |
               |
             _===_\n''','''
       +========+
       O       |
      / \      |
               |
               |
               |
               |
               |
               |
               |
             _===_\n''','''\
             +========+
             O       |
            /|\      |
                     |
                     |
                     |
                     |
                     |
                     |
                     |
                     |
                   _===_\n''','''\
                   +==========+
                   O         |
                  /|\        |
                  /          |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                           _===_\n''','''
                   +==========+
                   O         |
                  /|\        |
                  / \        |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                           _===_\n''',]

def IntroFunction():
# This Function will let the player know that what program even is this. 
    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guess a word letter by letter, a hanging man will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    # this thing or you can say FOR loop will make the text appear like anyone is typing it superfast.
    for c in text:
        sec = "0.0" + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    pri = ("""\nSo, lets start with some basic game things.
    What's your name ?:-""")
    # you will see it after every "string" variable.
    for c in pri:
        sec = "0.0" + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)    

    global name
    name = input()
#  You can't understand it because its written in Spanish.
    Text = ("Bonito Nombre niño ")
    for c in Text:
        sec = "0." + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

def SettingsFunction():
    # This Function will let the player choose his difficulty. 
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write full name of difficulty, and don't toggle the case of letters. \n"""
    for c in text:
        sec = "0.0" + str(random.randrange(1, 5, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    global answer
    answer = input()
    if (answer == 'easy') or (answer == 'Easy') or (answer == 'EASY'):
        EasyFunction()
    elif (answer == 'intermediate') or (answer == 'Intermediate') or (answer == 'INTERMEDIATE'):
        print('done')
    elif (answer == 'hard') or (answer == 'Hard') or (answer == 'HARD'):
        print('done')
    elif (answer == 'pro') or (answer == 'Pro') or (answer == 'PRO'):
        print('done')
    elif (answer == 'master') or (answer == 'Master') or (answer == 'MASTER'):
        print('done')

    elif (answer != 'easy') or (answer != 'Easy') or (answer != 'EASY') or (answer != 'intermediate') or (answer != 'Intermediate') or (answer != 'INTERMEDIATE') or (answer != 'hard') or (answer != 'Hard') or (answer != 'HARD') or (answer != 'pro') or (answer != 'Pro') or (answer != 'PRO') or (answer != 'master') or (answer != 'Master') or (answer != 'MASTER'):
        prit = "((Error)Invalid input) please read the note written with the question."
        for c in prit:
            sec = "0.0" + str(random.randrange(1, 5, 1))
            sec = float(sec)
            print(c,end=''),time.sleep(sec)

        LoopFunction()

def LoopFunction():

    global answer

    while:(answer != 'easy') and (answer != 'Easy') and (answer != 'EASY') and (answer != 'intermediate') and (answer != 'Intermediate') and (answer != 'INTERMEDIATE') and (answer != 'hard') and (answer != 'Hard') and (answer != 'HARD') and (answer != 'pro') and (answer != 'Pro') and (answer != 'PRO') and (answer != "master") and (answer != 'Master') and (answer != 'MASTER'):
        SettingsFunction() 

def EasyFunction():

    numberofguesses = 0

    global answer
    
    text = "So, let's start your game."
    for c in text:
        sec = "0.0" + str(random.randrange(1, 5, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    wordslist = ['cap','ant','fun','run','man','rub','fur','two','one','gun','pig','cow','sit','fit','lit','kit','hot','mop','lot','war','top','don','cod','net','wet','rat','mop']
    selectedword = (random.choice(wordslist))
    print("\n")
    for c in range(0,len(selectedword)):
        print("_",end=' ')
    
    printstatement = "\n\n\nGuess a letter\n "

    for c in printstatement:
        sec = "0.0" + str(random.randrange(1, 5, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    for numberofguesses in range(0,len(Hangman_ascii_easy)):

        guessofplayer = input()


        if guessofplayer  :
            WrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers ","no es la respuesta correcta","nu răspunsul corect","正しい答えではありません","不正确的答案","정답이 아니다","niet het juiste antwoord","pas la bonne réponse","όχι η σωστή απάντηση","non è la risposta giusta","не правильный ответ","ليس الجواب الصحيح","صحیح جواب نہیں","ਸਹੀ ਜਵਾਬ ਨਹੀਂ","सही उत्तर नहीं","ius responsum non"]
            WrongAnswerVaraiable = print(secrets.choice(WrongAnswerList)),range(0, 1)
            # also have to draw the hangman but don't know how to draw it
        for c in WrongAnswerVaraiable:
            sec = "0.0" + str(random.randrange( 1, 5 ,1))
            sec = float(sec)
            print(c,end=''),time.sleep(sec)


SettingsFunction()
EasyFunction()


















