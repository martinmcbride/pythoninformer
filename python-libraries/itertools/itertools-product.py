import itertools

# Using the product function to combine the sets  [1, 2, 3] and ["a", "b", "c", "d"]

a = [1, 2, 3]
b = ["a", "b", "c", "d"]

prod = itertools.product(a, b)

print(prod)
print(list(prod))

# Using the product function to combine the sets  ["square", "circle", "triangle"] and ["red", "yellow", "green", "blue"]

shapes = ["square", "circle", "triangle"]
colors = ["red", "yellow", "green", "blue"]

prod = itertools.product(shapes, colors)

print(list(prod))

# Using the product function to combine two dice throws

dice1 = range(1, 7)
dice2 = range(1, 7)

prod = itertools.product(dice1, dice2)

print(list(prod))

# Using the product function to combine the sets  ["square", "circle", "triangle"], ["red", "yellow", "green", "blue"], and ["big", "small"]

shapes = ["square", "circle", "triangle"]
colors = ["red", "yellow", "green", "blue"]
size = ["big", "small"]

prod = itertools.product(shapes, colors, size)

print(list(prod))

