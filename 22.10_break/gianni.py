
def przerywana_petla(y):
  for i in range(0, 100000):
    y = 2*y
    print(y)
    if y >= 100000:
      break
    print(i)
    
x = int( input() )
if x < 20 and x > 0:
  przerywana_petla(x)
