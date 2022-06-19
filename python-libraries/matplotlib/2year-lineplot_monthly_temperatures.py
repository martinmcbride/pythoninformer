import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2009 = [x[0] for x in csv_reader]

with open("2010-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2010 = [x[0] for x in csv_reader]

months = range(12)

plt.xlabel("Month")
plt.ylabel("Temperature")

plt.plot(months, temperature_2009, label="2009")
plt.plot(months, temperature_2010, label="2010")
plt.legend(loc="upper left")
plt.savefig("2year-lineplot-monthly-temperatures.png")
plt.show()
