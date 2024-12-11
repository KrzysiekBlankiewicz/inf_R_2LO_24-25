
def nuda(a,b):
    line = ""
    wydruk = 0
    while wydruk < b:
        ile = min(a, b - wydruk)
        line = "$ " * ile
        wydruk += ile
        a+=2
        print(line)
    return "Koniec"

print("Wprowadź a:")
a = int(input())
print("Wprowadź b:")
b = int(input())
if a <= 1 or a >= b or a >= 10^6:
    print("Zła liczba a")
if b <= 1 or a <= a or b >= 10^6:
    print("Zła liczba b")
print(nuda(a , b))
