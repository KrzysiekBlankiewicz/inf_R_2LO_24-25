def fun(a, b, c, x):
    return a*x**2 + b*x + c

def msc_zerowe(a, b, c, p, k, e):
    srodek = (p+k)/2
    
    #co tutaj jeszcze powinienem sprawdzić?
    #-czy delta >= 0
    #-czy p < k
    #-czy fun(p) albo fun(k) = 0

    if abs(fun(a, b, c, srodek)) < e:
           return srodek
    
    while abs(fun(a, b, c, srodek)) > e:
        if fun(a, b, c, srodek) > 0:
            k = srodek
        else:
            p = srodek
        srodek = (p+k)/2
        
    return srodek


print(msc_zerowe(1, 0, -1, -10, 0, 0.01))
