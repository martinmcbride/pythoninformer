# Author:  Martin McBride
# Created: 2022-03-29
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt

v = [2, 5, 3, 1, 4]
labels = ["A", "B", "C", "D", "E"]
explode = [0, 0.1, 0, 0.2, 0]

plt.pie(v, labels=labels, explode=explode)
plt.savefig("piechart-explode.png")
plt.show()
