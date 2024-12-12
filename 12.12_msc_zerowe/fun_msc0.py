import math



def fun(a, b, c, x):
    return a*x**2+b*x+c

def msc0(a, b, c, p, k, e):
    srodek = (p+k) / 2

    if fun(a, b, c, srodek) < e:
        return srodek
        
    if fun(a, b, c, srodek)*fun(a,b,c,p) < 0:
            return msc0(a,b,c,p,srodek,e)
    else:
            return msc0(a,b,c,k,srodek,e)
    return(srodek)
print(msc0(1,0,-1,0,10,0.01))

