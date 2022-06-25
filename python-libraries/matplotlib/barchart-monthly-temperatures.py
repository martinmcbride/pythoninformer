import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

months = range(12)

plt.title("Monthly temperature 2009")
plt.xlabel("Month")
plt.ylabel("Temperature")

plt.bar(months, temperature)
plt.savefig("barchart-monthly-temperatures.png")
plt.show()
