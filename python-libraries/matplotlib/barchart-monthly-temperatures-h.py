import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

months = range(12)

month_names = ["J", "F", "M", "A", "M", "J",
               "J", "A", "S", "O", "N", "D"]

plt.title("Monthly temperature 2009")
plt.xlabel("Temperature")
plt.ylabel("Month")
plt.yticks(months, month_names)

plt.barh(months, temperature)
plt.savefig("barchart-monthly-temperatures-h.png")
plt.show()
