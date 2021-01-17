
import time

print("Hello World again.")
time.sleep(2)

print("See who's here!, actually Don't know who you are?")
time.sleep(1)

print("Hii, me [BoT] and you??")
name = input(str)
print("Hmmmm....")
time.sleep(3)

print("Nice name " + name )
time.sleep(1.1)

def function_1():
    print("What do you Like Tea or coffee")
    desire = input(str)
    if(desire == 'tea'):
        print("Ramukaka 2 chaylana, jalddi")
        time.sleep(2)
        print("Abhi lay rahain he. ")
    
    elif(desire == 'coffee'):
        print("Sam, 2 cup of Coffees plz")   
        time.sleep(1.5)
        print("fasst") 

function_1()

while(desire != 'tea' and 'coffee' ):
    print("No, you have to take something")  
    time.sleep(1.7)

    function_1()  

print("")



