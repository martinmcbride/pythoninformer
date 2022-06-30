# Author:  Martin McBride
# Created: 2022-03-23
# Copyright (C) 2022, Martin McBride
# License: MIT

import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2009 = [x[0] for x in csv_reader]

with open("2010-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2010 = [x[0] for x in csv_reader]

month_names = ["J", "F", "M", "A", "M", "J",
               "J", "A", "S", "O", "N", "D"]

width = 0.4
months0 = range(12)
months1 = [x + width for x in range(12)]

plt.title("Monthly temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")

plt.bar(months0, temperature_2009, width, label="2009")
plt.bar(months1, temperature_2010, width, label="2010")
plt.xticks(months0, month_names)

plt.legend(loc="upper left")

plt.savefig("2year-barchart-monthly-temperatures.png")
plt.show()
