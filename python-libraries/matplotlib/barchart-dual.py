# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y1 = x*2 + 1
y2 = 6 - x

labels = ["red", "orange", "yellow", "green", "blue"]

width = 0.4
plt.bar(x-width/2, y1, width)
plt.bar(x+width/2, y2, width)
plt.xticks(x, labels)
plt.savefig("barchart-dual.png")
plt.show()
