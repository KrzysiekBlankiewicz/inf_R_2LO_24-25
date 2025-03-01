import math


def is_prime(n: int) -> bool:  # int - "integer" - całkowite
    # Sprawdza, czy liczba n jest liczbą pierwszą (dla n w zakresie 0–10000).
    # Liczby mniejsze niż 2 (0 i 1) nie są pierwsze
    if n < 2:
        return False
    # 2 jest jedyną parzystą liczbą pierwszą
    if n == 2:
        return True
    # Eliminacja liczb parzystych większych od 2
    if n % 2 == 0:
        return False
    # Sprawdzanie tylko nieparzystych dzielników od 3 do sqrt(n)
    max_divisor = int(math.isqrt(n))  # math.isqrt(n) zwraca floora pierwiastka z n
    for divisor in range(3, max_divisor + 1, 2):
        if n % divisor == 0:
            return False
    # Jeśli żaden dzielnik nie został znaleziony, liczba jest pierwsza
    return True


def are_digit_similar(a, b):
    # print(set(a))
    # print(set(b))

    return set(str(a)) == set(str(b))


# Funkcja do obliczenia odległości euklidesowej
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Funkcja klasyfikująca punkt
def classify_point(x, y):
    # Definicja zakresu
    side_length = 10000
    half_side = side_length // 2

    if -half_side + 1 <= x <= half_side - 1 and -half_side + 1 <= y <= half_side - 1:
        return "inside"
    elif ((x == -half_side or x == half_side) and (-half_side <= y <= half_side)) or (
        (y == -half_side or y == half_side) and (-half_side <= x <= half_side)
    ):
        return "boundary"
    else:
        return "outside"


def out_4_1():
    out = []

    with open("punkty.txt", "r") as file:
        for line in file:
            line_numbers = []

            for num in line.split():
                line_numbers.append(int(num))

            if is_prime(line_numbers[0]) and is_prime(line_numbers[1]):
                out.append(line_numbers)

    out_count = len(out)

    print(
        f"Punkty, gdzie obie współrzędne są liczbami pierwszymi: {out}. Jest ich {out_count}."
    )


def out_4_2():
    out = []

    with open("punkty.txt", "r") as file:
        for line in file:
            line_numbers = []

            for num in line.split():
                line_numbers.append(int(num))

            if are_digit_similar(line_numbers[0], line_numbers[1]):
                out.append(line_numbers)

    out_count = len(out)

    print(
        f"Punkty, gdzie obie współrzędne są liczbami 'cyfropodobne': {out}. Jest ich {out_count}."
    )


def out_4_3():
    points = []

    with open("punkty.txt", "r") as file:
        for line in file:
            line_numbers = []

            for num in line.split():
                line_numbers.append(int(num))

            points.append(line_numbers)

    max_distance = 0
    farthest_points = None

    # Iteracja po wszystkich parach punktów
    for i in range(len(points)):
        for j in range(i + 1, len(points)):  # Unikam powtórzeń
            p1 = points[i]
            p2 = points[j]
            distance = euclidean_distance(p1, p2)
            if distance > max_distance:
                max_distance = distance
                farthest_points = (p1, p2)

    # Zaokrąglenie odległości do liczby całkowitej
    rounded_distance = round(max_distance)

    print(
        f"Punkty najbardziej oddalone: {farthest_points}. Odległość między tymi punktami (zaokrąglona do liczby całkowitej) {rounded_distance}."
    )


def out_4_4():
    points = []

    inside_count = 0
    boundary_count = 0
    outside_count = 0

    with open("punkty.txt", "r") as file:
        for line in file:
            line_numbers = []

            for num in line.split():
                line_numbers.append(int(num))

            points.append(line_numbers)

    for point in points:
        x, y = point[0], point[1]

        category = classify_point(x, y)
        if category == "inside":
            inside_count += 1
        elif category == "boundary":
            boundary_count += 1
        else:
            outside_count += 1

    print(f"Liczba punktów wewnątrz kwadratu (bez boków): {inside_count}.")
    print(f"Liczba punktów na bokach kwadratu: {boundary_count}.")
    print(f"Liczba punktów na zewnątrz kwadratu (bez boków): {outside_count}.")


out_4_1()
out_4_2()
out_4_3()
out_4_4()