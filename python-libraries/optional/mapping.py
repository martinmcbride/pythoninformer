from optional import Optional
import math

# Create a filled and empty Optional for testing
f = Optional.of(100)
e = Optional.empty()

# Exercise the map method
def add_1(val):
    print("Map example", val)
    return val + 1

def mul_2(val):
    print("Map example2", val)
    return val*2

x = f.map(add_1).map(mul_2)
print(x)
x = e.map(add_1).map(mul_2)
print(x)

# Exercise the flap_map method
def add_2_opt(val):
    print("Flat map example", val)
    return Optional.of(val + 2)

x = f.map(add_2_opt)
print(x)
x = f.flat_map(add_2_opt)
print(x)
x = e.flat_map(add_2_opt)
print(x)

