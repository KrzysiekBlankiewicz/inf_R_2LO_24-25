def draw_line(row_len):
    print(" ".join(["$"] * row_len))


def draw_dollars(k, n):
    if not (1 <= k <= n <= 10**6):
        print(f"Dane wejściowe nie spełniają warunków: 1 <= {k} <= {n} <= {10**6} ???")
        return

    total_printed = 0  # Licznik wydrukowanych sztuk
    current_row_len = k  # Liczba znaków w bieżącym wierszu

    while total_printed < n:
        # Sprawdzenie, czy jesteśmy w ostatniej linii
        # oraz obliczenie ile znaków ma w niej być, żeby nie przekroczyć n.
        if total_printed + current_row_len > n:
            current_row_len = n - total_printed

        draw_line(current_row_len)

        total_printed += current_row_len
        current_row_len += 2  # Zwiększenie liczby $ w następnym wierszu


draw_dollars(k=100, n=50)
