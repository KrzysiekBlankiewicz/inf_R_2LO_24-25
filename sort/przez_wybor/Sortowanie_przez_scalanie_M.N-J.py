def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    środek = len(lista) // 2
    lewa_strona = merge_sort(lista[:środek])
    prawa_strona = merge_sort(lista[środek:])


    return scal(lewa_strona, prawa_strona)

def scal(lewa, prawa):
    wynik = []
    i = j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1

    wynik.extend(lewa[i: ])
    wynik.extend(prawa[j: ])

    return wynik

lista = [38, 27, 43, 3, 9, 82, 10]

posortowana_liczba = merge_sort(lista)
print(posortowana_liczba)

