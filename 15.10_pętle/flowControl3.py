print("elementy tablicy:")
tablica = [2, 4, 6, 7]
print(tablica[0])
print(tablica[1])
print(tablica[2])
print(tablica[3])

# możemy wykonać pewien fragment kodu "dla każdego" elementu tablicy
# używamy pętli, którą wprowadzamy za pomocą słowa kluczowego for

print("elementy tablicy za pomocą pętli:")
for element in tablica:
    print(element)

# zmienna element przyjmuje wartość kolejnych elementów tablicy
# oczywiście moglibyśmy nazwać tę zmienną dowolnie

print("nazwa zmiennej wewnętrznej nie ma znaczenia...")
for a in tablica:
    print(a)

# podobnie jak w przypadku argumwntów funkcji
# zmienna a oznacza lokalną zmienną w ramach pętli

print("...może nawet przysłonić nazwę zmiennej globalnej")
x = 14

for x in tablica:
    print(x)

# ZADANIE:
# ...
