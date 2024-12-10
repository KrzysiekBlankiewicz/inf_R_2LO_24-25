import random
a1 = random.randint(-1000000000000000000,1000000000000000000)
a2 = random.randint(a1,1000000000000000000)
b1 = random.randint(-1000000000000000000,1000000000000000000)
b2 = random.randint(b1,1000000000000000000)
poz = [a1,a2,b1,b2]
print(poz)
d1 = a2 - a1
d2 = b2 - b1
def pokrywanie(poz):
    if b1 > a2 or a1 > b2:
        print("Nie")
    if b2 == a1 or a2 == b1:
        print("0, styk")
    if b2 >= a1 and b1 <= a1:
        print(b2 - a1)
    if b1 <= a2 and b2 >= a2:
        print(a2 - b1)
    if b1 >= a1 and b2 <= a2:
        print("blok b wew blok a " + str( d2))
    if b2 >= a2 and b1 <= a1:
        print("blok a wew blok b " + str( d1))
pokrywanie(poz)
