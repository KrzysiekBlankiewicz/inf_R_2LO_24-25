print("Podaj liczbę k:")
k = int(input())
print("Podaj liczbę n:")
n = int(input())
t = 0
while n > 0:
    x = min(k, n)
    print('$ ' * x)
    n -= x
    k += 2
