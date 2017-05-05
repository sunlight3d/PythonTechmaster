from pprint import pprint
from random import randrange, uniform

# randrange gives you an integral value
irand = randrange(0, 10)
pprint("random integer = "+str(irand))
# uniform gives you a floating-point value
frand = uniform(0, 10)
frand = round(frand, 2)
pprint("random float = "+str(frand))