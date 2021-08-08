from pythonping import ping
import random

while 1:
     d1 = (random.randrange(0,255))
     d2 = (random.randrange(0,255))
     d3 = (random.randrange(0,255))
     d4 = (random.randrange(0,255))
     d5 = (random.randrange(0,9))
     d6 = (random.randrange(0,9))
     d7 = (random.randrange(0,9))
     d8 = (random.randrange(0,9))
     d9 = (random.randrange(0,9))
     d10 = (random.randrange(0,9))
     p = (".")
     h = f'{d1}.{d2}.{d3}.{d4}'
     ping(h, verbose=True)