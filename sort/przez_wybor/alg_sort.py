import time

x = time.time()
y = time.time()


tab = [4,3, 8, 6, 1, 0]

def m(tab):
    minv = tab[0]
    mini = 0
    for i in (0, len(tab)):
        if tab[1] < minv:
            minv = tab[i]
            mini = i
    return mini
        

def sort(tab):
    n = len(tab) - 1
    for i in range(0, n):
        tabn = tab[i:n]
        j = m(tabn)
        if i!= j:
            t = tab[i]
            tab[i] = j
            j = t
            

sort(tab)
print(tab)
