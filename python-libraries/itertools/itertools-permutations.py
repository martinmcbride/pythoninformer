import itertools

# Permutations of 4 items
k = ["A", "B", "C", "D"]
perms = itertools.permutations(k)
for t in perms:
    print(t)

# Pretty print the result
k = ["A", "B", "C", "D"]
for i, t in enumerate(itertools.permutations(k)):
    print(t, end="\n" if (i % 4)==3 else " ")

# Permutations of any 2 items from as set of 4
k = ["A", "B", "C", "D"]
perms = itertools.permutations(k, r=2)
for t in perms:
    print(t)

# Pretty print the result
k = ["A", "B", "C", "D"]
for i, t in enumerate(itertools.permutations(k, r=2)):
    print(t, end="\n" if (i % 4)==3 else " ")

# Permutations with replacement
k = range(10)
perms = itertools.product(k, repeat=4)
for t in perms:
    print(t)

