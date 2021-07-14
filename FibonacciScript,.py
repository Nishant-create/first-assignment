# 0,1,1,2,3,5,8,13,21,34,55,89,144,
# f(n) = f(n-1) + f(n-2)
# write a function which prints fibonacci series upto (n)th index where n can be any integer.
def fibonacciScript():
    print("Upto how many indexes you want to print")
    ranger = input()
    ranger = int(ranger)
    ranger = int(ranger) + 1
    thisList = 0
    a = 0
    b = 1
    fibonacciList = [0,1]
    
    for thisList in range(1, ranger):
    
        returnList = fibonacciList[a] + fibonacciList[b]
        fibonacciList.append(returnList)
        a = a + 1
        b = b + 1
        print(fibonacciList) 

fibonacciScript()