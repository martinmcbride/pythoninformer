import matplotlib.pyplot as plt
import csv

with open("2009-temp-daily.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

n = [0]*6

for x in temperature:
    bin_id = int(x//5)
    n[bin_id] += 1

centres = [i*5 + 2.5 for i in range(6)]

plt.bar(centres, n, 5, edgecolor='black')
plt.title("Temperature histogram 2009")
plt.xlabel("Temperature")
plt.ylabel("Number of days")
plt.savefig("histogram-temperatures-bins.png")
plt.show()
