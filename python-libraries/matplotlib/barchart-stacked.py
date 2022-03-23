# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2021#2, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 5)
y1 = x*2 + 1
y2 = 6 - x

labels = ["red", "orange", "yellow", "green", "blue"]

plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)
plt.xticks(x, labels)
plt.savefig("barchart-stacked.png")
plt.show()
