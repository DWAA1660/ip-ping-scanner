from pythonping import ping
import random

while 1:
     d1 = (random.randrange(1,255))
     d2 = (random.randrange(1,255))
     d3 = (random.randrange(1,255))
     d4 = (random.randrange(1,255))
     h = f'{d1}.{d2}.{d3}.{d4}'
     try:
         ping(h, verbose=True)
     except:
         print("invalid ip")