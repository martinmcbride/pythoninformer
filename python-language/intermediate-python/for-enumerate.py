# Author:  Martin McBride
# Created: 2022-09-16
# Copyright (C) 2022, Martin McBride
# License: MIT

# Enumerated list using loop counter (not recommended)

colors = ["red", "green", "blue"]

print("Enumerated list using loop counter")
for i in range(len(colors)):
    print(i, colors[i])

# Enumerated list using separate counter (not recommended)

print("Enumerated list using separate counter")
i = 0
for c in colors:
    print(i, c)
    i += 1

# Enumerated list using enumerate

print("Enumerated list using enumerate")
for i, c in enumerate(colors):
    print(i, c)

# Mark an item as selected

print("Mark an item as selected")
selected = 1
for i, c in enumerate(colors):
    if i == selected:
        print("=>", c)
    else:
        print(c)

# How it works 1

print("How it works 1")
for t in enumerate(colors):
    print(t)

# How it works 2

print("How it works 2")
for t in enumerate(colors):
    i, c = t
    print(i, c)

# Start value

print("Start value")
for i, c in enumerate(colors, 1):
    print(i, c)

# Enumerated list with tuples 1

pairs = [("A", "X"), ("B", "Y"), ("C", "Z")]

print("Enumerated list with tuples 1")
for t in enumerate(pairs):
    print(t)

# Enumerated list with tuples 2 (fails)

print("Enumerated list with tuples 2")
#for i, a, b in enumerate(pairs):
#    print(i, a, b)

# Enumerated list with tuples 3

print("Enumerated list with tuples 2")
for i, (a, b) in enumerate(pairs):
    print(i, a, b)

# zip example

shapes = ["circle", "square", "triangle"]

print("zip example")
for c, s in zip(colors, shapes):
    print(c, s)

# zip with enumerate

shapes = ["circle", "square", "triangle"]

print("zip with enumerate")
for i, (c, s) in enumerate(zip(colors, shapes)):
    print(i, c, s)
