import random
import math
import time

n = time.time()
points = []
amount = 10000000

def distans(point):
    x = point[0]
    y = point[1]
    return math.sqrt((500-x)**2 + (500-y)**2)

    
for i in range (0, amount):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    points.append([x,y])
    
inside = 0

for p in points:
    if distans(p) < 500:
        inside += 1

pi = (inside/ amount)*4

print("pi =", pi)
m = time.time()
print(m-n)
