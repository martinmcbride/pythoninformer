import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly-list.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature = list(csv_reader)

month_names = ["J", "F", "M", "A", "M", "J",
               "J", "A", "S", "O", "N", "D"]

months = range(12)

plt.title("Temperature box plot 2009")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.boxplot(temperature, positions=months)
plt.xticks(months, month_names)
plt.savefig("boxplot-temperatures.png")
plt.show()
