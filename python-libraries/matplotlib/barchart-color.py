# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = x*2 + 1

labels = ["A", "B", "C", "D", "E"]


plt.bar(x, y, color='cadetblue', edgecolor='k', linewidth=2)
plt.xticks(x, labels)
plt.savefig("barchart-color.png")
plt.show()

colors = ['g' if n < 4 else 'r' for n in y]

plt.bar(x, y, color=colors)
plt.xticks(x, labels)
plt.savefig("barchart-multicolor.png")
plt.show()
