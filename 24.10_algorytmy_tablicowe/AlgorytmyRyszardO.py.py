print("---Algorytmy---")

def max_elem(tab):
    max = tab[0]
    
    for i in range(0,10):
        if tab[i] > max:
            max = tab[i]
        if tab[i] < max:
            max = max
    return max
def min_elem(tab):
    min = tab[0]
    
    for i in range(0,10):
        if tab[i] < min:
            min = tab[i]
        if tab[i] > min:
            min = min
    return min
def sort_tab(tab):
    for i in range(0,9):
        for i in range(0,9):
            if tab[i] > tab[i+1]:
                temp = tab[i]
                tab[i]= tab[i+1]
                tab[i+1]= temp
    return tab



t=[0,6,5,7,9,1,3,4,8,9]
print("Max element")
print(max_elem(t))
print("Min element")
print(min_elem(t))            
print("Tablica")
print(sort_tab(t))          
