a1 = ("podaj a1")
a2 = ("podaj a2")
b1 = ("podaj b1")
b2 = ("podaj b2")
def platforma(x):
    if a2 < b1:
        print("NIE")
    if a2 == b1:
        print("0")
    if a2 > b1 and a2 < b2:
        c = a2 - b1
        print(c)
    if a2 < b1 and a2 > b2:
        f = b2 - a1
        print(f)
    if a1 > b1 and a2 < b2:
        d = b2 - b1
        print(d)
    if a1 < b1 and a2 > b2:
        e = a2 - a1
        print(e)
                       
     
