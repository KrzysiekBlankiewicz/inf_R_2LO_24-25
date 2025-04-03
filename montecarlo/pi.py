import random
import math
def pi(n):
    wew = 0
    y = 1000
    x = 1000
    for i in range(1,n):
        a = random.randint(1,1000)
        b = random.randint(1,1000)
        if math.sqrt((500-a)**2+(500-b)**2) <= 500:
            wew += 1
    print(wew/n*4)
pi(200000)
    
