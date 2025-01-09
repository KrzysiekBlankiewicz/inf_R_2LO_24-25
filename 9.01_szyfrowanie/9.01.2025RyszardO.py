znak = input()
word = input()
n = 46
limit = 122
m = 96

## ZNAK CEZAR

def cezar_znak(znak,m,n,limit):
    x = ord(znak)
    x = x+n
    if x > limit:
        x = (x - limit) + m
    return chr(x)

## SLOWO CEZAR

def cezar_word(word,n,limit):
    for i in word:
        y = cezar_znak(i,m,n,limit)
        print(y)
print(cezar_znak(znak,m,n,limit))
print(cezar_word(word,n,limit))
