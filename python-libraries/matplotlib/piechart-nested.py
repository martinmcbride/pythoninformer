# Author:  Martin McBride
# Created: 2022-03-29
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt

v1 = [2, 5, 3, 1, 4]
labels1 = ["A", "B", "C", "D", "E"]
v2 = [4, 1, 3, 4, 1]
labels2 = ["V", "W", "X", "Y", "Z"]
width = 0.3
wedge_properties = {"width":width, "edgecolor":"w",'linewidth': 2}

plt.pie(v1, labels=labels1, labeldistance=0.85,
        wedgeprops=wedge_properties)
plt.pie(v2, labels=labels2, labeldistance=0.75,
        radius=1-width, wedgeprops=wedge_properties)
plt.savefig("piechart-nested.png")
plt.show()
