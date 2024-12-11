def nuda(k,n):
    line = ""
    wydruk = 0
    while wydruk < n:
        ile = min(k, n - wydruk)
        line = "$ " * ile
        wydruk += ile
        k+=2
        print(line)
    return "Koniec"

print("Wprowadź K:")
k = int(input())
print("Wprowadź N:")
n = int(input())
if k <= 1 or k >= n or k >= 10^6:
    print("Zła liczba K")
if n <= 1 or n <= k or n >= 10^6:
    print("Zła liczba N")
print(nuda(k , n))
