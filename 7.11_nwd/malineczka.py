def nwd(a, b):
    licznik = 0
    if a < b:
        a, b = b, a
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            max_dzielnik = i
            licznik += 1
            break
    return [max_dzielnik, licznik]

x = int(input())
y = int(input())
print(nwd(x, y))



def nwd(a, b):
    licznik = 0
    while b != 0:
        a, b = b, a % b
        licznik += 1
    return a, licznik


x = int(input())
y = int(input())
nwd_result, iterations = nwd(x, y)
print(f"NWD: {nwd_result}, Iteracje: {iterations}")
