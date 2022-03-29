# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

y = np.arange(5)
x = y*2 + 1

labels = ["red", "orange", "yellow", "green", "blue"]

plt.barh(y, x)
plt.yticks(y, labels)
plt.savefig("barchart-horizontal.png")
plt.show()
