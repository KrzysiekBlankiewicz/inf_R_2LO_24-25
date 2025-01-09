limit = 122

def znakcezar(zn,n):
    x = ord(zn)
    x += n
    if x > limit:
        print(chr(x-26))
    else:
        print(chr(x))
        
def slowocezar(sl,n):
    for i in sl:
        znakcezar(i,n)

    
slowocezar("xxx",46)
