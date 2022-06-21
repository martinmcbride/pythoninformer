import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2009 = [x[0] for x in csv_reader]

with open("2010-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_2010 = [x[0] for x in csv_reader]

plt.scatter(temperature_2009, temperature_2010)
plt.title("Temperature 2009 vs 2010")
plt.xlabel("2009")
plt.ylabel("2010")
plt.savefig("scatter-temp.png")
plt.show()

