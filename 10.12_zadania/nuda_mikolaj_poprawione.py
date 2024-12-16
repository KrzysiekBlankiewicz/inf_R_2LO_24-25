k = int(input("$ w pierszej linii: "))
n = int(input("Podaj liczbę wszystkich $: "))
if n < k:
	print("Błąd.")
else:	
	licznik = 0
	while n > 0:
		if n >= k:	
			print("$ " * k + f" ({k})")
			n -= k
			licznik += k
			k += 2
		else:	
			print("$ " * n + f" ({n})")
			licznik += n
			n = 0  
	print(f"Razem wypisano: {licznik} symboli.")