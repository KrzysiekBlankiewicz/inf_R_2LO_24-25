znak = input()
n = int(input())
odp = ""
limit = 122
pocz¹tek = 96

    
def cezar_z(znak, n):
    x = ord(znak)
    x = x + n
    if x > limit:
        x = pocz¹tek + (x - limit)
    return(chr(x))
for i in range(0, len(znak)):
    x = cezar_z(znak[i], n)
    odp += x

print(odp)
