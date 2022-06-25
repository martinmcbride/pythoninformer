import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

plt.hist(temperature, edgecolor='black')
plt.title("Temperature histogram 2009")
plt.xlabel("Temperature")
plt.ylabel("Number of days")
plt.savefig("histogram-temperatures.png")
plt.show()
