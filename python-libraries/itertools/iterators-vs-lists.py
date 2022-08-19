import itertools

"""
Simple illustration of lazy iterators vs lists
"""

r = itertools.repeat(5, 3)  # Repeat the value 5, three times

print(r)  # r is a repeat object (an iterable)

for i in r:   # Looping over the iterator calculates its value
    print(i)

r = itertools.repeat(5, 3)  # Repeat the value 5, three times

print(list(r))              # The list function "realises" the iterator

