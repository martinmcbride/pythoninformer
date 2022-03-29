# Author:  Martin McBride
# Created: 2022-03-29
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt

v = [2, 5, 3, 1, 4]
labels = ["A", "B", "C", "D", "E"]
colors = ["#1abc9c", "#2c3e50", "#e67e22", "#8e44ad", "#c0392b"]
explode = [0, 0, 0.1, 0, 0]
wedge_properties = {"edgecolor":"k",'linewidth': 2}

plt.pie(v, labels=labels, explode=explode, colors=colors, startangle=30,
           counterclock=False, shadow=True, wedgeprops=wedge_properties,
           autopct="%1.1f%%", pctdistance=0.7)
plt.title("Color pie chart")
plt.savefig("piechart-styling.png")
plt.show()
