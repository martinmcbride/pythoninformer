import matplotlib.pyplot as plt

x = [n/4 for n in range(20)]
y1 = [n*n for n in x]
y2 = [25 - n*n for n in x]

plt.plot(x, y1, "m")
plt.plot(x, y2, "-.r")
plt.savefig("linestyles-string.png")
plt.show()

plt.plot(x, y1, color="cadetblue", linewidth=4)
plt.plot(x, y2, color="#ff8000", linewidth=6,
         linestyle=(0, (4, 2, 1, 2)), dash_capstyle="round")
plt.savefig("linestyles-parameters.png")
plt.show()