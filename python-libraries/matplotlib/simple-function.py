# Author:  Martin McBride
# Created: 2022-06-10
# Copyright (C) 2022, Martin McBride
# License: MIT

from matplotlib import pyplot as plt
import math

xa = []
ya = []

for i in range(100):
    xa.append(i*12/100)

for x in xa:
    ya.append(math.sin(x)*math.exp(-x/4))

plt.plot(xa, ya)
plt.savefig("simple-function.png")
plt.show()
