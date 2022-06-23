import matplotlib.pyplot as plt
import csv

with open("2009-temp-monthly-list.csv") as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    temperature_lists = list(csv_reader)

month_names = ["J", "F", "M", "A", "M", "J",
               "J", "A", "S", "O", "N", "D"]

months = range(12)

temperature = [sum(k)/len(k) for k in temperature_lists]
errors = [(max(k)-min(k))/2 for k in temperature_lists]

plt.title("Temperature bar chart 2009")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.bar(months, temperature, yerr=errors)
plt.xticks(months, month_names)
plt.savefig("barchart-error-bars.png")
plt.show()
