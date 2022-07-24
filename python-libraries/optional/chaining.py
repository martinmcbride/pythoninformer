from optional import Optional
import math

# Create a filled and empty Optional for testing
f = Optional.of(100)
e = Optional.empty()

# Excercise the if_present method
def do_something(val):
    print("If present example", val)
    return -1

x = f.if_present(do_something)
print(x)
x = e.if_present(do_something)
print(x)

# Excercise the or_else method

def supplier():
    print("In supplier")
    return -2

x = f.or_else(supplier)
print(x)
x = e.or_else(supplier)
print(x)

# if_present and or_else combined
x = f.if_present(lambda x: print(x*2)).or_else(lambda : -3)
print(x)
x = e.if_present(lambda x: print(x*2)).or_else(lambda : -3)
print(x)
