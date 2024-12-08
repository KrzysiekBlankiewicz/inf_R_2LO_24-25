def punktA(x):
    return (x-1)*(x-1)

def punktB(x):
    return (x+1)*4-4

print("Podaj dlugosc boku:")

x = int(input())

print(f"Liczba punktow wewnatrz kwadratu: {punktA(x)}")

print(f"Liczba punktow na krawedziach kwadratu: {punktB(x)}")
