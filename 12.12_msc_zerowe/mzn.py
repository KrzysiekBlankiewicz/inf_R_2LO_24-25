def funkw(a,b,c,x):
    return (a*x*x + b*x + c)
q = funkw(1,2,3,5)
print (q)
"""
def mz(a,b,c,p,k,e):
    sr = (p+k)/2
    d = b*b - 4*a*c
    if d >= 0 and p < k and
    if abs(funkw(a,b,c,sr)) <= e:
        return sr
    else:
        while abs(funkw(a,b,c,sr)) > e:
            if funkw(a,b,c,sr) > 0:
                k = sr
                sr = (p+k)/2
            if funkw(a,b,c,sr) < 0:
                p = sr
                sr = (p+k)/2
        return sr

print (mz(1,-2,0,0,100,0.01))
"""
def mz(a,b,c,p,k,e):
    sr = (p+k)/2
    d = (b*b) - 4*a*c
    if d < 0 or p > k:
        return ("ni ma")
    if abs(funkw(a,b,c,sr)) <= e:
        return sr
    if funkw(a,b,c,sr)* funkw(a,b,c,p) < 0:
        return mz(a,b,c,p,sr,e)
    else:
        return mz(a,b,c,sr,k,e)

print (mz(1,4,-1,0,100,0.01))
