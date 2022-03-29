# Author:  Martin McBride
# Created: 2022-03-29
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt

v = [2, 5, 3, 1, 4]
labels = ["A", "B", "C", "D", "E"]

plt.pie(v, labels=labels)
plt.savefig("piechart.png")
plt.show()
