def maluch(dar):
    for i in range(len(dar) - 1):
        if dar[i] > dar[i + 1]:
            dar[i], dar[i + 1] = dar[i + 1], dar[i]
    
    return dar

t = [3, 5, 2, 9, 1]
nt = maluch(t)
print(nt)
