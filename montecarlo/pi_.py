import random

n = 1000000

def pi_(n):
    punkty = 0
    r = 500

    for i in range(n):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)

        x -= 500
        y -= 500

        if x**2 + y**2 <= r**2:
            punkty += 1

    pi = 4 * punkty / n
    return pi

print(pi_(n))
