import string

selw = 'wOb'
d = input()
d = str(d)
a = d.upper()
pos = selw.find(d)
print(pos)
dan = int(pos)
if(dan == int(-1)):
    print(dan)