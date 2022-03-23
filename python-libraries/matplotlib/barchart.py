# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2021#2, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 5)
y = x*2 + 1

plt.bar(x, y)
plt.savefig("barchart.png")
plt.show()
