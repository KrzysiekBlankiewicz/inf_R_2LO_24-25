def funkcja(a,b,c,x):
    funk = a*x**2 + b*x + c
    return funk

def miejsce_zerowe(a,b,c,p,k,e):
    srodek = (p+k)/2

    delta = b**2 - 4*a*c
    if delta >= 0:
        pass
    else:
        return print("funkcja nie ma miejsc zerowych")

    if abs(funkcja(a,b,c,srodek)) < e:
        return srodek

    while abs(funkcja(a,b,c,srodek)) < e:
        if funkcja(a,b,c,srodek) > 0:
            k = srodek
        else:
            p = srodek
            srodek = (p+k)/2
    return srodek

print(miejsce_zerowe(1,-2,0,0,17,00.1))
