# 0,1,1,2,3,5,8,13,21,34,55,89,144,
# f(n) = f(n-1) + f(n-2)
# write a function which prints fibonacci series upto (n)th index where n can be any integer.
def fib():
    a = 0
    b = 1
    fibonacciList = [0,1]
    
    while True != False:
    
        returnList = fibonacciList[a] + fibonacciList[b]
        fibonacciList.append(returnList)
        a = a + 1
        b = b + 1
        print(fibonacciList)
# returnlist = [0,1]
# a = returnlist[0] + returnlist[1]
# returnlist.append(a)
# a = returnlist[1]+ returnlist[2]
# returnlist.append(a)
# a = returnlist[2] + returnlist[3]
# returnlist.append(a)
# a = returnlist[3] + returnlist[4]
# returnlist.append(a)
fib()