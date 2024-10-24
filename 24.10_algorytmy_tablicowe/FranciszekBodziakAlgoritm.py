def max_elem(t):
    max = t[0]
    for i in range (1,10):
        if t[i] > max:
            max = t[i]
    return max

def min_elem(t):
    min = t[0]
    for i in range (1,10):
        if t[i] < min:
            min = t[i]
    return min

def move_max_r(t):
    for i in range(0,9):
        for i in range(0,9):
            if t[i] > t[i+1]:
                temp = t[i]
                t[i] = t[i+1]
                t[i+1] = temp
    return t

t=[30,18,9,45,61,12,73,16,42,31]



print(max_elem(t))
print(min_elem(t))
print(move_max_r(t))
