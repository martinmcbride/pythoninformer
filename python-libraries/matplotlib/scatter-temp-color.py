import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2009 = [x[0] for x in csv_reader]

with open("2010-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2010 = [x[0] for x in csv_reader]

plt.scatter(temperature_2009[0:90], temperature_2010[0:90],
            color="c", label="winter")
plt.scatter(temperature_2009[90:181], temperature_2010[90:181],
            color="g", label="spring")
plt.scatter(temperature_2009[181:273], temperature_2010[181:273],
            color="y", label="summer")
plt.scatter(temperature_2009[273:365], temperature_2010[273:365],
            color="m", label="autumn")
plt.title("Temperature 2009 vs 2010")
plt.xlabel("2009")
plt.ylabel("2010")
plt.legend(loc="upper left")
plt.savefig("scatter-temp-color.png")
plt.show()

