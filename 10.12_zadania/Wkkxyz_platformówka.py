def segment_intersection(a1, a2, b1, b2):
    if not (-(10**18) <= a1 < a2 <= 10**18 and -(10**18) <= b1 < b2 <= 10**18):
        print(
            f"Dane wejściowe nie spełniają warunków: {-(10**18)} <= {a1} < {a2} <= {10**18} and {-(10**18)} <= {b1} < {b2} <= {10**18} ???"
        )
        return

    left = max(a1, b1)  # Maksymalna wartość lewego końca wspólnego przedziału
    right = min(a2, b2)  # Minimalna wartość prawego końca wspólnego przedziału

    if left > right:
        print("NIE")  # Brak części wspólnej
    else:
        print(right - left)  # Długość części wspólnej (może być 0)


segment_intersection(a1=1, a2=8, b1=50, b2=10)
segment_intersection(a1=3, a2=8, b1=9, b2=10)
segment_intersection(a1=8, a2=10, b1=3, b2=8)
