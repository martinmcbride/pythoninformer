import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

with open("2009-rain-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    rain = [x[0] for x in csv_reader]

plt.scatter(temperature, rain)
plt.title("Temperature vs rainfall 2009")
plt.xlabel("Temperature")
plt.ylabel("Rain")
plt.savefig("scatter-temp-rain.png")
plt.show()

