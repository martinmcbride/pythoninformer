# Author:  Martin McBride
# Created: 2022-03-29
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt

v1 = [2, 5, 3, 1, 4]
labels1 = ["A", "B", "C", "D", "E"]
width = 0.3
wedge_properties = {"width":width}

plt.pie(v1, labels=labels1, wedgeprops=wedge_properties)
plt.savefig("piechart-donut.png")
plt.show()
