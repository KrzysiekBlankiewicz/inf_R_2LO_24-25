import math
def r_prime(x, y):
    return math.gcd(x, y) == 1
d = 0
def keys(p, q):
    n = p*q
    fn = (p-1)*(q-1)
    for i in range(2, fn):
        if r_prime(i, fn) == 1:
            e = i
    while False:
        if (d*e % fn == 1):
            d = d+1
    priv_keys = (d, n)
    publ_keys = (e, n)
    return (priv_keys, publ_keys)

def encode(mes, publ_code):
    e = publ_cod[0]
    n = publ_code[1]
    
    code = mes^e % n
    return code

def decode(priv_keys, code):
    d = priv_keys[0]
    n = priv_keys[1]
    
