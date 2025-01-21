import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euklides(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m

def keys(p, q):
    e = 2
    n = p * q
    phi = (p-1)*(q-1)
    while gcd(e, phi) != 1:
        e = e + 1
    d = euklides(e, phi)
    priv_key = (d, e)
    public_key = (e, n)
    return (priv_key, public_key)

def encode(message, public_key):
    e = public_key[0]
    n = public_key[1]

    code =
    return code

def decode(code, priv_key):
    message =
    return message

(priv, public) = keys(?,?)
m = input("podaj liczbe")
c = encode(m, publc)
print(c)
x = decode(c, priv)
print(x)