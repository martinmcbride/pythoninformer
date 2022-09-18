# Author:  Martin McBride
# Created: 2022-09-16
# Copyright (C) 2022, Martin McBride
# License: MIT

from itertools import zip_longest

# Loop over 2 lists using loop counter (not recommended)

colors = ["red", "green", "blue"]
shapes = ["circle", "square", "triangle"]

print("Loop over 2 lists using loop counter")
for i in range(len(colors)):
    print(colors[i], shapes[i])

# Loop over 2 lists using zip

print("Loop over 2 lists using zip")
for c, s in zip(colors, shapes):
    print(c, s)

# How zip works 1

print("How zip works 1")
for t in zip(colors, shapes):
    print(t)

# How zip works 2

print("How zip works 2")
for t in zip(colors, shapes):
    c, s = t
    print(c, s)

# Zip 3 sequences

print("Zip 3 sequences")
count = [2, 10, 5]
for c, s, n in zip(colors, shapes, count):
    print(c, s, n)

# Zip sequences unequal length

print("Zip sequences unequal length")
count = [2, 10, 5, 7]
for c, n in zip(colors, count):
    print(c, n)

# Zip longest

print("Zip longest")
count = [2, 10, 5, 7]
for c, n in zip_longest(colors, count):
    print(c, n)


# Unzip

print("Unzip")
zipped = [("red", "circle"), ("green", "square"), ("blue", "triangle")]
colors2, shapes2 = zip(*zipped)
print(colors2, shapes2)

