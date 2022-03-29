# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = x*2 + 1
errors = [0.5, 2, 1.5, 4, 3]

labels = ["red", "orange", "yellow", "green", "blue"]

plt.bar(x, y, yerr=errors)
plt.xticks(x, labels)
plt.savefig("barchart-errorbars.png")
plt.show()
