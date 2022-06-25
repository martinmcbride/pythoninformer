import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

with open("2009-rain-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    rain = [x[0] for x in csv_reader]

days = range(365)

plt.subplot(2, 1, 1)
plt.plot(days, temperature)
plt.ylabel("Temperature")
plt.subplot(2, 1, 2)
plt.plot(days, rain)
plt.xlabel("Day")
plt.ylabel("Rain")
plt.suptitle("2009 weather")
plt.savefig("2plot-temp-rain.png")
plt.show()

