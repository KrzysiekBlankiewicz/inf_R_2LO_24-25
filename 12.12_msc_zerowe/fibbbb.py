def fibb(n):
    if n==0 or n==1:
        return 1
    return (fibb(n-1) + fibb(n-2))
print(2**50)
print(fibb(50))
