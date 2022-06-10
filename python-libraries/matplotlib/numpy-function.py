# Author:  Martin McBride
# Created: 2022-06-10
# Copyright (C) 2022, Martin McBride
# License: MIT

from matplotlib import pyplot as plt
import numpy as np

xa = np.linspace(0, 12, 100)
ya = np.sin(xa)*np.exp(-xa/4)

plt.plot(xa, ya)
plt.savefig("numpy-function.png")
plt.show()
