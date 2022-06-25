import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = [x[0] for x in csv_reader]

month_names = ["J", "F", "M", "A", "M", "J",
               "J", "A", "S", "O", "N", "D"]

months = range(12)

plt.title("Monthly temperature 2009")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.xticks(months, month_names)

plt.stem(months, temperature)
plt.savefig("stemplot-monthly-temperatures-names.png")
plt.show()