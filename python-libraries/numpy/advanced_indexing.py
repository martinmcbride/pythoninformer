# Author:  Martin McBride
# Created: 2022-05-15
# Copyright (C) 2022, Martin McBride
# License: MIT

import numpy as np

# Vectorisation example
print("Vectorisation example")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
u = np.sqrt(a)
v = a + b
print(u, v)

# Fancy indexing
print("index parameter")
a = np.array([-1.0, 2.0, -3.0, 4.0])
idx = np.array([2, 1, 1, 0, 3])
r = a[idx]
print(r)

# Fancy indexing loop equival
print("index loop equivalent")
a = np.array([-1.0, 2.0, -3.0, 4.0])
idx = np.array([2, 1, 1, 0, 3])
r = np.empty_like(idx, dtype=a.dtype)
for i in range(idx.size):
    r[i] = a[idx[i]]
print(r)

# Fancy indexing multi-dimensional a
print("index multi-dimensional a")
a = np.array([[0, 1], [10, 11], [100, 110]])
idx = np.array([2, 0, 1])
idx2 = np.array([1, 0, 1])
r = a[idx, idx2]
print(r)

# Fancy indexing multi-dimensional idx
print("index multi-dimensional idx")
a = np.array([-1.0, 2.0, -3.0, 4.0])
idx = np.array([[2, 0, 1], [3, 3, 0]])
r = a[idx]
print(r)

# Fancy indexing boolean
print("boolean index parameter")
a = np.array([-1.0, 2.0, -3.0, 4.0])
idx = np.array([True, False, False, True])
r = a[idx]
print(r)

# Fancy indexing boolean, 2D
print("boolean index parameter 2D")
a = np.array([[-1.0, 2.0, -3.0, 4.0], [-10.0, 20.0, -30.0, 40.0]])
idx = np.array([[True, False, False, True], [True, False, False, True]])
r = a[idx]
print(r)

# where parameter of ufunc
print("where parameter")
a = np.array([-1.0, 2.0, -3.0, 4.0])
t = a>0
r = np.sqrt(a, where=t)
print(r)

# where parameter of ufunc with prefilled array
print("where parameter prefilled")
a = np.array([-1.0, 2.0, -3.0, 4.0])
r= np.full_like(a, -1.0)
np.sqrt(a, where=a>0, out=r)
print(r)

# where parameter of add with prefilled array and filter array
print("where parameter filter")
a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8])
t = np.array([True, False, True, True])
r= np.full_like(a, -1.0)
np.add(a, b, where=t, out=r)
print(r)

# at parameter of ufunc
print("at parameter")
a = np.array([-1.0, 2.0, -3.0, 4.0])
idx = [1, 3]
np.sqrt.at(a, idx)
print(a)
