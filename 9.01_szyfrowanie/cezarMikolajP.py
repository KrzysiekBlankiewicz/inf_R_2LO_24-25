znak = input()
n = int(input())
odp = ""
limit = 122
poczštek = 96
 
    
def skidbi(znak, n):
    x = ord(znak)
    x = x + n
    if x > limit:
        x = początek + (x - limit)
    return(chr(x))
for i in range(0, len(znak)):
    x = skidbi(znak[i], n)
    odp += x
 
print(odp)
 
 
 
 
znak = input()
n = int(input())
 
odp = ""
limit = 122
poczatek = 96
 
def skibidi(znak, n):
    x = ord(znak)
    x = x - n 
    if x < ord('a'):
        x = limit - (ord('a') - x - 1)
    return chr(x)
 
for i in range(0, len(znak)):
    x = skibidi(znak[i], n)
    odp += x
 
print(odp)
