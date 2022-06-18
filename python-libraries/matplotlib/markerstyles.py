import matplotlib.pyplot as plt

x = [n/4 for n in range(20)]
y1 = [n*n for n in x]
y2 = [25 - n*n for n in x]

plt.plot(x, y1, "sk")
plt.plot(x, y2, "^:c")
plt.savefig("markerstyles-string.png")
plt.show()

plt.plot(x, y1, color="#00ff40", linewidth=2, marker="h",
         markersize=8, markeredgecolor="indigo",
         markeredgewidth=2)
plt.plot(x, y2, color="goldenrod", linewidth=4, marker="D",
         markersize=10, markerfacecolor="midnightblue",
         markeredgewidth=2, markevery=4)
plt.savefig("markerstyles-parameters.png")
plt.show()