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
      /|\      |
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
             |       |
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
                  /|\        |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                           _===_\n''']

def IntroFunction():

    text = ("""\n Hey! its Game Time,\nToday we are going to play a game known as HANGMAN. Its a bit high level game from our Guessnumber game.\nIn this game you have to guess a word letter by letter, a hanging man will be drawn side by side on your every incorrect guess.\nand you will lose when the hanging man is completely drawn unless you have guessed the word.\nSo, GooD Luck and enjoy the game """)
    
    for c in text:
        sec = "0.0" + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    pri = ("""\nSo, lets start with some basic game things.
    What's your name ?:-""")
    for c in pri:
        sec = "0.0" + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)    

    global name
    name = input()

    int = ("Bonito Nombre niño ")
    for c in int:
        sec = "0." + str(random.randrange(1, 3, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

def SettingsFunction():
    
    text = """
    Choose Difficulty:-\n(a) Easy\n(b) Intermediate\n(c) Hard\n(d) Pro\n(e) Master\n
    Note:- Please write only a single word like a,b,c,d,e. Don't write brackets or the full name of difficulty\n"""
    for c in text:
        sec = "0.0" + str(random.randrange(1, 5, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    global answer
    answer = input()
    if (answer == 'a'):
        EasyFunction()
    elif (answer == 'b'):
        print('done')
    elif (answer == 'c'):
        print('done')
    elif (answer == 'd'):
        print('done')
    elif (answer == 'e'):
        print('done')

    else:
        prit = "((Error)Invalid input) please read the note written with the question."
        for c in prit:
            sec = "0.0" + str(random.randrange(1, 5, 1))
            sec = float(sec)
            print(c,end=''),time.sleep(sec)

        LoopFunction()

def LoopFunction():

    global answer

    while(answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd' and answer != 'e'):
        SettingsFunction() 

def EasyFunction():
    numberofguesses = 0
    text = "So, let's start the game"
    for c in text:
        sec = "0.0" + str(random.randrange(1, 5, 1))
        sec = float(sec)
        print(c,end=''),time.sleep(sec)

    wordslist = ['cape','ant','fun','run','man','rush','ruby','four','two','one','rub','gun','lion','wolf','pig','cow','sit','fit','lit','knit','shot','mop','lot','node','word','pass','top','down','cold','net','wet','rat','mop','vote']
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


        if guessofplayer :
            WrongAnswerList = ["Wrong guess","nononononono!","Nope this is not the right answer","Error not the input required","Its not that easy man!","Hey! you, don't give wrong answers ","no es la respuesta correcta","nu răspunsul corect","正しい答えではありません","不正确的答案","정답이 아니다","niet het juiste antwoord","pas la bonne réponse","όχι η σωστή απάντηση","non è la risposta giusta","не правильный ответ","ليس الجواب الصحيح","صحیح جواب نہیں","ਸਹੀ ਜਵਾਬ ਨਹੀਂ","सही उत्तर नहीं","ius responsum non"]
            print(secrets.choice(WrongAnswerList)),range(0, 1)
            # also have to draw the hangman but don't know how to draw it
    
EasyFunction()


















