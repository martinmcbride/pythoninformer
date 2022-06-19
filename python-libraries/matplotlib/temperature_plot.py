import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

days = range(365)
plt.plot(days, temperature)
plt.savefig("temperature-plot.png")
plt.show()

