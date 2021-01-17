def deaf():
    if(ans == 'Tea')or(ans == 'tea'):
        print("Ramukaka 2 chay lana")
        print('Jalddi')
    elif(ans == 'Coffee')or(ans == 'coffee'):
        print("Steve 2 Coffees,please!")
        print("Fast")
    else:
         print("No you have to take something")
print("Hello! what's your name?")
name = input()
print("Nice to meet you " + name)
print("Who are you?")
print("A.HUMAN B.ALIEN")
answer = input()
def fun():
    if(answer == 'HUMAN'):
        print("Very glad to see a human here")
        print("What would you like a Tea or a Coffee")
        ans = input()    
    elif(answer == 'ALIEN'):
        print("You Alien Get Out Of Here")
    while((ans != 'Tea'and ans != 'Coffee')):
        print("Invalid input plz try again")
        ans = input()
        deaf
while((answer != 'HUMAN'and answer != 'ALIEN')):
    print('Invalid input plz try again')
    answer = input()
    fun()
