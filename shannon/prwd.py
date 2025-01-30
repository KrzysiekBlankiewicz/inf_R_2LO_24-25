file = open("lorem.txt")

string = file.read()

licznik = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g =0 
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q =0 
r = 0
s = 0 
t = 0
u = 0
v=0
w=0
x=0
y=0
z=0
kropa = 0
spacja = 0
przecinek = 0

for znak in string:
	licznik += 1
print(licznik)

for znak in string:
	if znak == 'a' or znak == 'A': 
		a += 1
	elif znak == 'b' or znak == 'B': 
		b += 1
	elif znak == 'c' or znak == 'C': 
		c += 1
	elif znak == 'd' or znak == 'D': 
		d += 1
	elif znak == 'e' or znak == 'E': 
		e += 1
	elif znak == 'f' or znak == 'F': 
		f += 1
	elif znak == 'g' or znak == 'G': 
		g += 1
	elif znak == 'h' or znak == 'H': 
		h += 1
	elif znak == 'i' or znak == 'I': 
		i += 1
	elif znak == 'j' or znak == 'J': 
		j += 1
	elif znak == 'k' or znak == 'K': 
		k += 1
	elif znak == 'l' or znak == 'L': 
		l += 1
	elif znak == 'm' or znak == 'M': 
		m += 1
	elif znak == 'n' or znak == 'N': 
		n += 1
	elif znak == 'o' or znak == 'O': 
		o += 1
	elif znak == 'p' or znak == 'P':
		p += 1
	elif znak == 'q' or znak == 'Q': 
		q += 1
	elif znak == 'r' or znak == 'R': 
		r += 1
	elif znak == 's' or znak == 'S': 
		s += 1
	elif znak == 't' or znak == 'T': 
		t += 1
	elif znak == 'u' or znak == 'U': 
		u += 1
	elif znak == 'v' or znak == 'V': 
		v += 1
	elif znak == 'w' or znak == 'W': 
		w += 1
	elif znak == 'x' or znak == 'X': 
		x += 1
	elif znak == 'y' or znak == 'Y': 
		y += 1
	elif znak == 'z' or znak == 'Z': 
		z += 1
	elif znak == ' ' or znak == ' ': 
		spacja += 1
	elif znak == ',' or znak == ',': 
		przecinek += 1
	elif znak == '.' or znak == '.': 
		kropa += 1
prwd_a = a / licznik
prwd_b = b / licznik
prwd_c = c / licznik
prwd_d = d / licznik
prwd_e = e / licznik
prwd_f = f / licznik
prwd_g = g / licznik
prwd_h = h / licznik
prwd_i = i / licznik
prwd_j = j / licznik
prwd_k = k / licznik
prwd_l = l / licznik
prwd_m = m / licznik
prwd_n = n / licznik
prwd_o = o / licznik
prwd_p = p / licznik
prwd_q = q / licznik
prwd_r = r / licznik
prwd_s = s / licznik
prwd_t = t / licznik
prwd_u = u / licznik
prwd_v = v / licznik
prwd_w = w / licznik
prwd_x = x / licznik
prwd_y = y / licznik
prwd_z = z / licznik
prwd_spacja = spacja/licznik
prwd_kropa = kropa/licznik
prwd_przecinek = przecinek/licznik

print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}, g: {g}, h: {h}, i: {i}, j: {j}, k: {k}, l: {l}, m: {m}, n: {n}, o: {o}, p: {p}, q: {q}, r: {r}, s: {s}, t: {t}, u: {u}, v: {v}, w: {w}, x: {x}, y: {y}, z: {z}, spacja: {spacja}, kropa:{kropa}, przeciek:{przecinek}")
print(f"prwd_a: {prwd_a}, prwd_b: {prwd_b}, prwd_c: {prwd_c}, prwd_d: {prwd_d}, prwd_e: {prwd_e}, prwd_f: {prwd_f}, prwd_g: {prwd_g}, prwd_h: {prwd_h}, prwd_i: {prwd_i}, prwd_j: {prwd_j}, prwd_k: {prwd_k}, prwd_l: {prwd_l}, prwd_m: {prwd_m}, prwd_n: {prwd_n}, prwd_o: {prwd_o}, prwd_p: {prwd_p}, prwd_q: {prwd_q}, prwd_r: {prwd_r}, prwd_s: {prwd_s}, prwd_t: {prwd_t}, prwd_u: {prwd_u}, prwd_v: {prwd_v}, prwd_w: {prwd_w}, prwd_x: {prwd_x}, prwd_y: {prwd_y}, prwd_z: {prwd_z}, prwd_kropa:{prwd_kropa}, prwd_przecinek:{prwd_przecinek}, prwd_spacja:{prwd_spacja}")