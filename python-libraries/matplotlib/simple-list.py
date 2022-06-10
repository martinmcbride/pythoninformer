# Author:  Martin McBride
# Created: 2022-06-10
# Copyright (C) 2022, Martin McBride
# License: MIT

from matplotlib import pyplot as plt

xa = [0, 1, 2, 3]
ya = [1, 3, 2, 5]

plt.plot(xa, ya)
plt.savefig("simple-list.png")
plt.show()
