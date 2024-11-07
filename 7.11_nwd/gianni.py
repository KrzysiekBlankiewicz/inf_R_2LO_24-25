def nwd(a,b):
    v = 0
    if a < b:
        limit = a
    else:
        limit = b
    for i in range(1,limit + 1):
        if a % i == 0 and b % i == 0:
            v = i
    return v

print("podaj a")
a = int(input())

print("podaj b")
b = int(input())


x = nwd(a,b)
print(x)
